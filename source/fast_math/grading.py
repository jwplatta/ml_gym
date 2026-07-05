from __future__ import annotations

from decimal import Decimal, InvalidOperation
from fractions import Fraction

from source.fast_math.models import GeneratedQuestion


def normalize_text(value: str) -> str:
    return " ".join(value.strip().lower().split())


def normalize_numeric(value: str) -> Decimal | None:
    cleaned = value.strip().replace(",", "")
    if not cleaned:
        return None
    try:
        return Decimal(cleaned)
    except InvalidOperation:
        return None


def normalize_fraction(value: str) -> Fraction | None:
    cleaned = value.strip().replace(" ", "")
    if not cleaned:
        return None
    try:
        if "/" in cleaned:
            numerator, denominator = cleaned.split("/", maxsplit=1)
            return Fraction(int(numerator), int(denominator))
        return Fraction(Decimal(cleaned))
    except (ValueError, ZeroDivisionError, InvalidOperation):
        return None


def normalize_answer(question: GeneratedQuestion, user_answer: str) -> str:
    kind = question.grading.kind
    if kind == "numeric":
        value = normalize_numeric(user_answer)
        if value is None:
            return ""
        normalized = format(value.normalize(), "f")
        if "." in normalized:
            normalized = normalized.rstrip("0").rstrip(".")
        return normalized or "0"
    if kind == "fraction":
        value = normalize_fraction(user_answer)
        return "" if value is None else f"{value.numerator}/{value.denominator}"
    return normalize_text(user_answer)


def is_correct_answer(question: GeneratedQuestion, user_answer: str) -> tuple[bool, str]:
    kind = question.grading.kind
    normalized = normalize_answer(question, user_answer)
    if not normalized:
        return False, normalized

    if kind == "numeric":
        expected = normalize_numeric(question.answer)
        actual = normalize_numeric(user_answer)
        if expected is None or actual is None:
            return False, normalized
        tolerance = question.grading.tolerance
        if tolerance is None:
            return expected == actual, normalized
        return abs(expected - actual) <= Decimal(str(tolerance)), normalized

    if kind == "fraction":
        expected = normalize_fraction(question.answer)
        actual = normalize_fraction(user_answer)
        return expected == actual, normalized

    return normalize_text(question.answer) == normalized, normalized
