from __future__ import annotations

import pandas as pd


def build_attempts_dataframe(history: list[dict]) -> pd.DataFrame:
    rows: list[dict] = []
    for quiz in history:
        for question in quiz.get("questions", []):
            rows.append(
                {
                    "quiz_id": quiz["quiz_id"],
                    "completed_at": pd.to_datetime(quiz["completed_at"], utc=True),
                    "date": pd.to_datetime(quiz["completed_at"], utc=True).date(),
                    "question_type": question["question_type"],
                    "topic": question["topic"],
                    "is_correct": bool(question["is_correct"]),
                    "response_time_seconds": float(question["response_time_seconds"]),
                }
            )
    if not rows:
        return pd.DataFrame(
            columns=[
                "quiz_id",
                "completed_at",
                "date",
                "question_type",
                "topic",
                "is_correct",
                "response_time_seconds",
            ]
        )
    return pd.DataFrame(rows)


def summarize_history(history: list[dict]) -> dict[str, float | int]:
    attempts = build_attempts_dataframe(history)
    if attempts.empty:
        return {
            "quizzes_completed": 0,
            "questions_answered": 0,
            "accuracy_pct": 0.0,
            "practice_days": 0,
        }
    return {
        "quizzes_completed": len(history),
        "questions_answered": int(len(attempts)),
        "accuracy_pct": round(float(attempts["is_correct"].mean() * 100.0), 2),
        "practice_days": int(attempts["date"].nunique()),
    }


def daily_question_counts(history: list[dict]) -> pd.DataFrame:
    attempts = build_attempts_dataframe(history)
    if attempts.empty:
        return pd.DataFrame(columns=["date", "questions_completed"])
    daily = (
        attempts.groupby("date")
        .size()
        .reset_index(name="questions_completed")
        .sort_values("date")
    )
    return daily


def daily_question_counts_by_type(history: list[dict]) -> pd.DataFrame:
    attempts = build_attempts_dataframe(history)
    if attempts.empty:
        return pd.DataFrame(columns=["date", "question_type", "questions_completed"])
    daily = (
        attempts.groupby(["date", "question_type"])
        .size()
        .reset_index(name="questions_completed")
        .sort_values(["date", "question_type"])
    )
    return daily


def accuracy_by_field(history: list[dict], field: str) -> pd.DataFrame:
    attempts = build_attempts_dataframe(history)
    if attempts.empty:
        return pd.DataFrame(columns=[field, "accuracy_pct", "questions_answered"])
    summary = (
        attempts.groupby(field)
        .agg(
            accuracy_pct=("is_correct", lambda values: round(float(values.mean() * 100.0), 2)),
            questions_answered=("is_correct", "size"),
        )
        .reset_index()
        .sort_values(["accuracy_pct", "questions_answered"], ascending=[False, False])
    )
    return summary


def score_trend(history: list[dict]) -> pd.DataFrame:
    if not history:
        return pd.DataFrame(columns=["completed_at", "score_pct", "question_count"])
    rows = [
        {
            "completed_at": pd.to_datetime(quiz["completed_at"], utc=True),
            "score_pct": float(quiz["score_pct"]),
            "question_count": len(quiz.get("questions", [])),
        }
        for quiz in history
    ]
    return pd.DataFrame(rows).sort_values("completed_at")
