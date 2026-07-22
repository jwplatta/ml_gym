from __future__ import annotations

import math
import random
from dataclasses import dataclass
from time import monotonic
from uuid import uuid4

from source.fast_math.analytics import question_type_stats
from source.fast_math.grading import is_correct_answer
from source.fast_math.models import GeneratedQuestion, QuestionAttempt, QuizAttemptRecord, utc_now_iso
from source.fast_math.registry import QuestionGenerator, generators_by_topic


@dataclass
class ActiveQuiz:
    quiz_id: str
    started_at: str
    selected_topics: list[str]
    requested_question_count: int
    hints_enabled: bool
    questions: list[GeneratedQuestion]
    current_index: int = 0
    attempts: list[QuestionAttempt] | None = None
    question_started_at: float | None = None

    def __post_init__(self) -> None:
        if self.attempts is None:
            self.attempts = []
        if self.question_started_at is None:
            self.question_started_at = monotonic()

    @property
    def current_question(self) -> GeneratedQuestion | None:
        if self.current_index >= len(self.questions):
            return None
        return self.questions[self.current_index]

    @property
    def completed(self) -> bool:
        return self.current_index >= len(self.questions)


_EFFORT_LEVELS = ("low", "medium", "high")


def _probe(gen: QuestionGenerator) -> GeneratedQuestion:
    """Call a generator with a fixed seed to read its metadata without side effects."""
    return gen(random.Random(0))


def build_quiz(
    *,
    selected_topics: list[str],
    question_count: int,
    hints_enabled: bool,
    seed: int | None = None,
    history: list[dict] | None = None,
    use_weights: bool = False,
    allow_type_repeats: bool = False,
    selected_efforts: list[str] | None = None,
    effort_distribution: dict[str, float] | None = None,
) -> ActiveQuiz:
    """Build a quiz.

    Args:
        effort_distribution: Mapping of effort level to target proportion, e.g.
            {"low": 0.4, "medium": 0.4, "high": 0.2}. Values should sum to 1.0.
            When None, all effort levels are weighted equally.
        selected_efforts: Which effort levels to include. When None, all are included.
    """
    topic_map = generators_by_topic()
    generators = [generator for topic in selected_topics for generator in topic_map.get(topic, [])]

    # Filter by effort level
    if selected_efforts is not None:
        effort_set = set(selected_efforts)
        generators = [g for g in generators if _probe(g).effort in effort_set]

    if not generators:
        raise ValueError("No question generators available for the selected topics and effort levels.")

    rng = random.Random(seed)

    # Build effort weight lookup
    if effort_distribution:
        effort_weights = {k: float(v) for k, v in effort_distribution.items()}
    else:
        effort_weights = {level: 1.0 / len(_EFFORT_LEVELS) for level in _EFFORT_LEVELS}

    questions = []
    used_types: set[str] = set()
    available = list(generators)

    if use_weights and history:
        stats = question_type_stats(history)
    else:
        stats = {}

    while len(questions) < question_count:
        if not available:
            available = list(generators)
            used_types.clear()

        weights = []
        for gen in available:
            q = _probe(gen)
            effort_w = effort_weights.get(q.effort, 1.0 / len(_EFFORT_LEVELS))

            if stats:
                s = stats.get(q.question_type, {"seen": 0, "accuracy": 0.5, "avg_confidence": None})
                history_w = 1 / (s["seen"] + 1) + (1 - s["accuracy"])

                avg_conf = s.get("avg_confidence")
                if avg_conf is not None and not math.isnan(float(avg_conf)):
                    conf_penalty = (5.0 - float(avg_conf)) / 4.0
                else:
                    conf_penalty = 0.5
                history_w += conf_penalty
            else:
                history_w = 1.0

            weights.append(effort_w * history_w)

        gen = rng.choices(available, weights=weights, k=1)[0]

        question = gen(rng)
        questions.append(question)

        if not allow_type_repeats:
            qt = question.question_type
            used_types.add(qt)
            available = [g for g in generators if _probe(g).question_type not in used_types]
    return ActiveQuiz(
        quiz_id=str(uuid4()),
        started_at=utc_now_iso(),
        selected_topics=selected_topics,
        requested_question_count=question_count,
        hints_enabled=hints_enabled,
        questions=questions,
    )


def submit_answer(active_quiz: ActiveQuiz, user_answer: str) -> QuestionAttempt:
    question = active_quiz.current_question
    if question is None:
        raise ValueError("Quiz is already complete.")

    is_correct, normalized_answer = is_correct_answer(question, user_answer)
    attempt = QuestionAttempt(
        question_id=question.question_id,
        question_type=question.question_type,
        topic=question.topic,
        subtopic=question.subtopic,
        prompt=question.prompt,
        canonical_answer=question.answer,
        answer_display=question.answer_display,
        hint=question.hint,
        effort=question.effort,
        metadata=question.metadata,
        raw_user_answer=user_answer,
        normalized_user_answer=normalized_answer,
        is_correct=is_correct,
        response_time_seconds=round(monotonic() - (active_quiz.question_started_at or monotonic()), 3),
        submitted_at=utc_now_iso(),
    )
    active_quiz.attempts.append(attempt)
    active_quiz.current_index += 1
    active_quiz.question_started_at = monotonic()
    return attempt


def finalize_quiz(active_quiz: ActiveQuiz) -> QuizAttemptRecord:
    if not active_quiz.completed:
        raise ValueError("Quiz cannot be finalized until all questions are answered.")

    correct_count = sum(1 for attempt in active_quiz.attempts if attempt.is_correct)
    incorrect_count = len(active_quiz.attempts) - correct_count
    score_pct = (correct_count / len(active_quiz.attempts) * 100.0) if active_quiz.attempts else 0.0
    return QuizAttemptRecord(
        quiz_id=active_quiz.quiz_id,
        started_at=active_quiz.started_at,
        completed_at=utc_now_iso(),
        selected_topics=active_quiz.selected_topics,
        requested_question_count=active_quiz.requested_question_count,
        hints_enabled=active_quiz.hints_enabled,
        questions=list(active_quiz.attempts),
        correct_count=correct_count,
        incorrect_count=incorrect_count,
        score_pct=round(score_pct, 2),
    )
