#!/usr/bin/env python3
"""Select example question files from the index.

Outputs a JSON array of question file paths.
"""

import argparse
import json
import random
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


def filter_questions(questions, topics):
    if not topics:
        return [q for q in questions if q.get("active", True)]
    topics = {t.lower() for t in topics}
    filtered = []
    for q in questions:
        if not q.get("active", True):
            continue
        q_topics = {t.lower() for t in q.get("topics", [])}
        if q_topics & topics:
            filtered.append(q)
    return filtered


def main():
    parser = argparse.ArgumentParser(description="Select example questions from index.json.")
    parser.add_argument(
        "--index",
        type=str,
        default=str(Path(__file__).resolve().parent.parent / "questions" / "index.json"),
        help="Path to index.json.",
    )
    parser.add_argument(
        "--topics",
        type=str,
        default="",
        help="Comma-separated list of topics to filter.",
    )
    parser.add_argument("--count", type=int, required=True, help="Number of questions.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed.")
    parser.add_argument(
        "--absolute",
        action="store_true",
        help="Return absolute paths instead of paths relative to questions dir.",
    )
    args = parser.parse_args()

    index_path = Path(args.index)
    questions = load_index(index_path)
    topics = [t.strip() for t in args.topics.split(",") if t.strip()]
    pool = filter_questions(questions, topics)

    if not pool:
        print("No questions matched the requested topics.", file=sys.stderr)
        sys.exit(1)
    if args.count > len(pool):
        print(
            f"Requested {args.count} questions but only {len(pool)} available.",
            file=sys.stderr,
        )
        sys.exit(1)

    rng = random.Random(args.seed)
    chosen = rng.sample(pool, args.count)

    base_dir = index_path.parent
    paths = []
    for q in chosen:
        path = base_dir / q["file"]
        paths.append(str(path.resolve()) if args.absolute else str(path))

    json.dump(paths, sys.stdout)


if __name__ == "__main__":
    main()
