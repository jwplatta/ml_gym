#!/usr/bin/env python3
"""Generate a blank quant practice notebook.

Creates a Jupyter notebook with a single header cell describing the
date, topics, and number of questions. Questions are appended later.
"""

import argparse
from datetime import date
from pathlib import Path

import nbformat


def slugify(value):
    return "".join(c if c.isalnum() else "_" for c in value.lower()).strip("_")


def build_header(topics, count):
    today = date.today().isoformat()
    topics_display = ", ".join(topics) if topics else "Mixed"
    header = (
        "# Quant Practice\n\n"
        f"Date: {today}\n\n"
        f"Topics: {topics_display}\n\n"
        f"Questions: {count}\n"
    )
    return header


def main():
    parser = argparse.ArgumentParser(description="Generate a blank quant practice notebook.")
    parser.add_argument(
        "--topics",
        type=str,
        default="",
        help="Comma-separated list of topics (e.g. returns,portfolio,signals).",
    )
    parser.add_argument(
        "--count", type=int, required=True, help="Number of questions to generate."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="./notebooks/practice",
        help="Output directory for the notebook.",
    )
    args = parser.parse_args()

    topics = [t.strip() for t in args.topics.split(",") if t.strip()]

    nb = nbformat.v4.new_notebook()
    nb.cells.append(nbformat.v4.new_markdown_cell(build_header(topics, args.count)))

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    today = date.today().strftime("%Y%m%d")
    topic_slug = slugify("_".join(topics)) if topics else "mixed"
    filename = f"quant_practice_{topic_slug}_{today}.ipynb"
    output_path = output_dir / filename

    _, nb = nbformat.validator.normalize(nb)
    with open(output_path, "w") as f:
        nbformat.write(nb, f)

    print(str(output_path))


if __name__ == "__main__":
    main()
