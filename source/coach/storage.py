from __future__ import annotations

import json
from pathlib import Path

from source.coach.models import QuizAttemptRecord

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / ".coach"
QUIZ_HISTORY_PATH = DATA_DIR / "quiz_history.jsonl"


def ensure_data_dir() -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR


def append_quiz_attempt(record: QuizAttemptRecord) -> Path:
    ensure_data_dir()
    with QUIZ_HISTORY_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record.to_dict()) + "\n")
    return QUIZ_HISTORY_PATH


def load_quiz_history() -> list[dict]:
    if not QUIZ_HISTORY_PATH.exists():
        return []
    records: list[dict] = []
    with QUIZ_HISTORY_PATH.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records
