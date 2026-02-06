#!/usr/bin/env python3
"""Append a question and solution to a quant practice notebook."""

import argparse
from pathlib import Path

import nbformat


def read_text(path):
    with open(path) as f:
        return f.read().strip()


def next_question_number(nb):
    count = 0
    for cell in nb.cells:
        if cell.cell_type != "markdown":
            continue
        source = cell.source.lstrip()
        if source.startswith("### Question "):
            count += 1
    return count + 1


def build_solution_cell(solution_text):
    return (
        "<details>\n"
        "<summary><b>Solution</b></summary>\n\n"
        "```python\n"
        f"{solution_text}\n"
        "```\n\n"
        "</details>"
    )


def split_setup_from_question(text):
    lines = text.splitlines()
    setup_start = None
    for i, line in enumerate(lines):
        if line.strip().lower() == "## setup":
            setup_start = i
            break
    if setup_start is None:
        return text, ""

    code_start = None
    code_end = None
    for j in range(setup_start + 1, len(lines)):
        if lines[j].strip().startswith("```"):
            code_start = j
            break
    if code_start is None:
        return text, ""

    for k in range(code_start + 1, len(lines)):
        if lines[k].strip().startswith("```"):
            code_end = k
            break
    if code_end is None:
        return text, ""

    setup_code = "\n".join(lines[code_start + 1 : code_end]).strip()
    question_text = "\n".join(lines[:setup_start]).rstrip()
    if code_end + 1 < len(lines):
        tail = "\n".join(lines[code_end + 1 :]).lstrip()
        if tail:
            question_text = f"{question_text}\n\n{tail}"
    return question_text, setup_code


def main():
    parser = argparse.ArgumentParser(
        description="Append a question and solution to a Jupyter notebook."
    )
    parser.add_argument("--notebook", type=str, required=True, help="Path to notebook.")
    parser.add_argument("--question-text", type=str, help="Question prompt text.")
    parser.add_argument("--question-file", type=str, help="Path to a markdown question.")
    parser.add_argument("--solution-text", type=str, help="Solution text.")
    parser.add_argument("--solution-file", type=str, help="Path to solution text.")
    parser.add_argument(
        "--setup-code",
        type=str,
        default="",
        help="Optional setup code cell to insert after the question.",
    )
    parser.add_argument("--setup-file", type=str, help="Path to setup code.")
    args = parser.parse_args()

    if not args.question_text and not args.question_file:
        raise SystemExit("Provide --question-text or --question-file.")
    if not args.solution_text and not args.solution_file:
        raise SystemExit("Provide --solution-text or --solution-file.")

    question_text = args.question_text or read_text(args.question_file)
    setup_code = ""
    if args.setup_file:
        setup_code = read_text(args.setup_file)
    elif args.setup_code:
        setup_code = args.setup_code
    else:
        question_text, setup_code = split_setup_from_question(question_text)
    solution_text = args.solution_text or read_text(args.solution_file)

    notebook_path = Path(args.notebook)
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    q_num = next_question_number(nb)
    question_cell = nbformat.v4.new_markdown_cell(
        f"### Question {q_num}\n\n{question_text}"
    )
    nb.cells.append(question_cell)

    if setup_code:
        nb.cells.append(nbformat.v4.new_code_cell(setup_code))

    nb.cells.append(nbformat.v4.new_code_cell("# Your solution here\n"))
    nb.cells.append(nbformat.v4.new_markdown_cell(build_solution_cell(solution_text)))

    _, nb = nbformat.validator.normalize(nb)
    with open(notebook_path, "w") as f:
        nbformat.write(nb, f)


if __name__ == "__main__":
    main()
