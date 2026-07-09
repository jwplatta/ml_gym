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
        return pd.DataFrame(columns=["date", "topic", "questions_completed"])
    daily = (
        attempts.groupby(["date", "topic"])
        .size()
        .reset_index(name="questions_completed")
        .sort_values(["date", "topic"])
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


def slowest_question_types(history: list[dict], n: int = 5) -> pd.DataFrame:
    attempts = build_attempts_dataframe(history)
    if attempts.empty:
        return pd.DataFrame(columns=["question_type", "avg_seconds"])
    return (
        attempts.groupby("question_type")
        .agg(avg_seconds=("response_time_seconds", "mean"), count=("response_time_seconds", "size"))
        .reset_index()
        .query("count > 2")
        .sort_values("avg_seconds", ascending=False)
        .head(n)
    )


def question_type_stats(history: list[dict]) -> dict[str, dict]:
    attempts = build_attempts_dataframe(history)
    if attempts.empty:
        return {}
    return (
        attempts.groupby("question_type")
        .agg(seen=("is_correct", "size"), accuracy=("is_correct", "mean"))
        .to_dict("index")
    )


def score_distribution(history: list[dict]) -> pd.DataFrame:
    """Returns one row per quiz with score_pct and topic (all selected topics joined)."""
    if not history:
        return pd.DataFrame(columns=["score_pct", "topic"])
    rows = []
    for quiz in history:
        topics = sorted({q["topic"] for q in quiz.get("questions", [])})
        rows.append(
            {
                "score_pct": float(quiz["score_pct"]),
                "topic": ", ".join(topics) if topics else "unknown",
            }
        )
    return pd.DataFrame(rows)


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
