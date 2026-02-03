#!/usr/bin/env python3
"""
Generate Jupyter notebooks from quiz JSON files.

Usage:
    python generate_notebook.py --quiz quizzes/sample.json --output practice.ipynb
    python generate_notebook.py --quiz quizzes/sample.json --output-dir notebooks
"""

import argparse
import json
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook


def load_quiz(quiz_path: Path) -> dict:
    with quiz_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if isinstance(data, list):
        return {"metadata": {}, "questions": data}

    if "questions" not in data:
        raise ValueError(f"Expected key 'questions' in {quiz_path}")

    return data


def format_question_body(question: dict) -> str:
    lines = [question.get("question", "").strip()]

    details = question.get("details")
    if details:
        lines.append("\n**Details:**\n")
        lines.append(str(details).strip())

    data = question.get("data")
    if data:
        lines.append("\n**Data:**\n")
        lines.append("```json")
        lines.append(json.dumps(data, indent=2))
        lines.append("```")

    return "\n".join(lines).strip()


def create_notebook(quiz: dict, title: str | None = None):
    """
    Create a Jupyter notebook from enriched questions.

    Args:
        questions: List of question dictionaries from question_randomizer
        title: Notebook title

    Returns:
        nbformat NotebookNode
    """
    nb = new_notebook()

    questions = quiz.get("questions", [])
    metadata = quiz.get("metadata", {})

    title_text = title or metadata.get("title", "Probability Practice Challenges")
    date_text = metadata.get("date") or metadata.get("generated_at")
    if not date_text:
        from datetime import datetime

        date_text = datetime.now().strftime("%Y-%m-%d")
    topics = metadata.get("topics") or []
    if isinstance(topics, list):
        topics_text = ", ".join(topics)
    else:
        topics_text = str(topics)
    count_text = metadata.get("count", len(questions))
    header_md = (
        f"# {title_text}\n\n"
        f"**Date:** {date_text}\n"
        f"**Questions:** {count_text}\n"
        f"**Topics:** {topics_text}\n"
    )
    nb.cells.append(new_markdown_cell(header_md))

    # Add each question
    for i, q in enumerate(questions, 1):
        question_md = f"## Question {i}\n\n{format_question_body(q)}"
        nb.cells.append(new_markdown_cell(question_md))

        nb.cells.append(new_code_cell("# Add your solution here\n"))

        solution_text = q.get("solution", "").strip() or "Solution not available."
        solution_md = (
            "<details>\n"
            "<summary><b>Solution</b> (click to expand)</summary>\n\n"
            f"{solution_text}\n\n"
            "</details>"
        )
        nb.cells.append(new_markdown_cell(solution_md))

    return nb


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate Jupyter notebooks from quiz JSON files"
    )
    parser.add_argument(
        "--quiz",
        required=True,
        help="Quiz JSON file path",
    )
    parser.add_argument(
        "--output",
        help="Output notebook file path (.ipynb). Overrides --output-dir if provided.",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory to write the notebook into (default: current directory)",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Notebook title (optional, overrides quiz metadata)",
    )

    args = parser.parse_args()

    quiz_path = Path(args.quiz)
    quiz = load_quiz(quiz_path)
    questions = quiz.get("questions", [])

    if args.output:
        output_path = Path(args.output)
    else:
        output_dir = Path(args.output_dir)
        output_path = output_dir / f"{quiz_path.stem}.ipynb"

    if output_path.suffix != ".ipynb":
        output_path = output_path.with_suffix(".ipynb")

    nb = create_notebook(quiz, title=args.title)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as handle:
        nbformat.write(nb, handle)

    print(f"\nCreated notebook with {len(questions)} questions: {output_path}")
    print(f"\nOpen with: jupyter notebook {output_path}")


if __name__ == '__main__':
    main()
