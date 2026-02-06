#!/usr/bin/env python3
"""Print a JSON array of unique topics from index.json."""

import argparse
import json
import sys
from pathlib import Path


def load_index(index_path):
    with open(index_path) as f:
        data = json.load(f)
    if isinstance(data, dict) and "questions" in data:
        return data["questions"]
    if isinstance(data, list):
        return data
    raise ValueError("index.json must be a list or a dict with 'questions'.")


def main():
    parser = argparse.ArgumentParser(description="List unique topics from index.json.")
    parser.add_argument(
        "--index",
        type=str,
        default=str(Path(__file__).resolve().parent.parent / "questions" / "index.json"),
        help="Path to index.json.",
    )
    parser.add_argument(
        "--only-active",
        action="store_true",
        help="Only include topics from active questions.",
    )
    args = parser.parse_args()

    try:
        questions = load_index(Path(args.index))
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)

    topics = set()
    for q in questions:
        if args.only_active and not q.get("active", True):
            continue
        for topic in q.get("topics", []):
            if topic:
                topics.add(topic)

    json.dump(sorted(topics), sys.stdout)


if __name__ == "__main__":
    main()
