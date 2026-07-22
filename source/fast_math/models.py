from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Literal
from uuid import uuid4


@dataclass(frozen=True)
class GradingSpec:
    kind: str
    tolerance: float | None = None

    @classmethod
    def numeric(cls, tolerance: float | None = None) -> "GradingSpec":
        return cls(kind="numeric", tolerance=tolerance)

    @classmethod
    def fraction(cls) -> "GradingSpec":
        return cls(kind="fraction")

    @classmethod
    def text(cls) -> "GradingSpec":
        return cls(kind="text")

    @classmethod
    def compound_fraction_numeric(cls, tolerance: float | None = None) -> "GradingSpec":
        """Two-part answer: a fraction followed by a numeric value, separated by a comma."""
        return cls(kind="compound_fraction_numeric", tolerance=tolerance)


@dataclass(frozen=True)
class GeneratedQuestion:
    question_type: str
    topic: str
    prompt: str
    answer: str
    answer_display: str
    hint: str | None
    grading: GradingSpec
    subtopic: str | None = None
    effort: Literal["low", "medium", "high"] = "medium"
    metadata: dict[str, Any] = field(default_factory=dict)
    question_id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["grader"] = payload.pop("grading")
        return payload


@dataclass(frozen=True)
class QuestionAttempt:
    question_id: str
    question_type: str
    topic: str
    subtopic: str | None
    prompt: str
    canonical_answer: str
    answer_display: str
    hint: str | None
    effort: str
    metadata: dict[str, Any]
    raw_user_answer: str
    normalized_user_answer: str
    is_correct: bool
    response_time_seconds: float
    submitted_at: str
    confidence: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class QuizAttemptRecord:
    quiz_id: str
    started_at: str
    completed_at: str
    selected_topics: list[str]
    requested_question_count: int
    hints_enabled: bool
    questions: list[QuestionAttempt]
    correct_count: int
    incorrect_count: int
    score_pct: float

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["questions"] = [question.to_dict() for question in self.questions]
        return payload


def utc_now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
