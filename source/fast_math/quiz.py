from __future__ import annotations

import random
from dataclasses import dataclass
from time import monotonic
from uuid import uuid4

from source.fast_math.grading import is_correct_answer
from source.fast_math.models import GeneratedQuestion, QuestionAttempt, QuizAttemptRecord, utc_now_iso
from source.fast_math.registry import generators_by_topic


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


def build_quiz(
    *,
    selected_topics: list[str],
    question_count: int,
    hints_enabled: bool,
    seed: int | None = None,
) -> ActiveQuiz:
    topic_map = generators_by_topic()
    generators = [generator for topic in selected_topics for generator in topic_map.get(topic, [])]
    if not generators:
        raise ValueError("No question generators available for the selected topics.")

    rng = random.Random(seed)
    questions = [rng.choice(generators)(rng) for _ in range(question_count)]
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
        prompt=question.prompt,
        canonical_answer=question.answer,
        answer_display=question.answer_display,
        hint=question.hint,
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
