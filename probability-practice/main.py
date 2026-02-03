#!/usr/bin/env python3
"""
CLI for generating probability quizzes and notebooks.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

import nbformat
from dotenv import load_dotenv
from src.generate_notebook import create_notebook
from src.question_randomizer import select_questions
from src.write_solutions import add_solutions


def build_quiz_filename(topics: list[str], timestamp: str) -> str:
    topics_slug = "_".join(topics)
    return f"{topics_slug}_{timestamp}.json"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate quiz JSON and a Jupyter notebook for probability practice."
    )
    parser.add_argument(
        "--topics",
        nargs="+",
        required=True,
        help="Topic names (e.g., combinations permutations probability_axioms)",
    )
    parser.add_argument(
        "--difficulty",
        choices=["easy", "medium", "hard"],
        help="Difficulty level filter (optional)",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Number of questions to generate (default: 10)",
    )
    parser.add_argument(
        "--quizzes-dir",
        default="probability-practice/quizzes",
        help="Directory to write quiz JSON files (default: probability-practice/quizzes)",
    )
    parser.add_argument(
        "--notebooks-dir",
        default="probability-practice/notebooks",
        help="Directory to write notebook files (default: probability-practice/notebooks)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducibility (optional)",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="OpenRouter model override (optional)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="OpenRouter request timeout in seconds (default: 60)",
    )
    parser.add_argument(
        "--request-delay",
        type=float,
        default=0.0,
        help="Delay (seconds) between OpenRouter requests (default: 0)",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Notebook title (optional)",
    )

    args = parser.parse_args()

    load_dotenv()

    questions = select_questions(
        topics=args.topics,
        count=args.count,
        difficulty=args.difficulty,
        seed=args.seed,
    )

    solutions = add_solutions(
        questions,
        model=args.model,
        timeout=args.timeout,
        request_delay=args.request_delay,
    )

    timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    quiz_filename = build_quiz_filename(args.topics, timestamp)
    quizzes_dir = Path(args.quizzes_dir)
    quizzes_dir.mkdir(parents=True, exist_ok=True)
    quiz_path = quizzes_dir / quiz_filename

    quiz_payload = {
        "metadata": {
            "topics": args.topics,
            "difficulty": args.difficulty,
            "count": len(solutions),
            "generated_at": timestamp,
        },
        "questions": solutions,
    }

    with quiz_path.open("w", encoding="utf-8") as handle:
        json.dump(quiz_payload, handle, indent=2, ensure_ascii=False)

    notebooks_dir = Path(args.notebooks_dir)
    notebooks_dir.mkdir(parents=True, exist_ok=True)
    notebook_path = notebooks_dir / f"{quiz_path.stem}.ipynb"

    notebook = create_notebook(quiz_payload, title=args.title)

    with notebook_path.open("w", encoding="utf-8") as handle:
        nbformat.write(notebook, handle)

    print(f"Wrote quiz JSON: {quiz_path}")
    print(f"Wrote notebook: {notebook_path}")


if __name__ == "__main__":
    main()
