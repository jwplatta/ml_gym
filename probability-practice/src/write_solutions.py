#!/usr/bin/env python3
"""
Generate solutions for enriched probability questions using OpenRouter.
"""

from __future__ import annotations

import time
from collections.abc import Iterable

from tqdm import tqdm

from .openrouter_client import request_openrouter

# DEFAULT_MODEL = "openai/gpt-oss-120b:free"
# DEFAULT_MODEL = "meta-llama/llama-3.3-70b-instruct:free"
DEFAULT_MODEL = "qwen/qwen3-next-80b-a3b-instruct:free"


def build_prompt(question_text: str, solution_template: str | None = None) -> str:
    prompt = (
        "Write a solution in Markdown. Use LaTeX for all formulas "
        "and wrap every formula with dollar signs only: inline `$...$` "
        "and display `$$...$$` (do NOT use `\\[` `\\]`). "
        "Do not use Unicode math symbols or smart quotes.\n\n"
        "Examples (use this exact style):\n"
        "- Inline: $\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$\n"
        "- Display:\n"
        "$$\\frac{n!}{(n-r)!}$$\n"
        "$$\\frac{d}{dx}x^n = nx^{n-1}$$\n\n"
        f"Question:\n{question_text}"
    )
    if solution_template:
        prompt += f"\n\nUse this solution template as guidance:\n{solution_template}"
    return prompt


def request_solution(
    question_text: str,
    solution_template: str | None = None,
    *,
    model: str | None = DEFAULT_MODEL,
    timeout: int = 60,
) -> str:
    model_name = model or DEFAULT_MODEL
    output_text = request_openrouter(
        build_prompt(question_text, solution_template),
        model=model_name,
        timeout=timeout,
    )
    return sanitize_solution(output_text)


def sanitize_solution(text: str) -> str:
    text = text.replace('""', '"').replace("''", '"')
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2026": "...",
        "\u00a0": " ",
        "\u202f": " ",
        "\u2009": " ",
        "\u200b": "",
        "\u2003": " ",
        "\u2002": " ",
        "\u00ad": "",
        "\u2212": "-",
        "\u00d7": "*",
        "\u00f7": "/",
    }
    for src, dest in replacements.items():
        text = text.replace(src, dest)
    return text


def add_solutions(
    questions: Iterable[dict],
    *,
    model: str | None = DEFAULT_MODEL,
    timeout: int = 60,
    request_delay: float = 0.0,
) -> list[dict]:
    question_list = list(questions)
    enriched = []
    for question in tqdm(question_list, desc="Writing solutions", unit="question"):
        solution = request_solution(
            question_text=question["question"],
            solution_template=question.get("solution-template") or None,
            model=model,
            timeout=timeout,
        )
        updated = dict(question)
        updated["solution"] = solution
        enriched.append(updated)
        if request_delay:
            time.sleep(request_delay)

    return enriched
