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


def _split_compound(value: str) -> tuple[str, str] | None:
    """Split a compound answer into two parts on the first comma."""
    parts = value.split(",", maxsplit=1)
    if len(parts) != 2:
        return None
    return parts[0].strip(), parts[1].strip()


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
    if kind == "compound_fraction_numeric":
        parts = _split_compound(user_answer)
        if parts is None:
            return ""
        frac_part, num_part = parts
        frac = normalize_fraction(frac_part)
        num = normalize_numeric(num_part)
        if frac is None or num is None:
            return ""
        num_str = format(num.normalize(), "f")
        if "." in num_str:
            num_str = num_str.rstrip("0").rstrip(".")
        return f"{frac.numerator}/{frac.denominator},{num_str or '0'}"
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

    if kind == "compound_fraction_numeric":
        exp_parts = _split_compound(question.answer)
        usr_parts = _split_compound(user_answer)
        if exp_parts is None or usr_parts is None:
            return False, normalized
        exp_frac = normalize_fraction(exp_parts[0])
        act_frac = normalize_fraction(usr_parts[0])
        exp_num = normalize_numeric(exp_parts[1])
        act_num = normalize_numeric(usr_parts[1])
        if exp_frac is None or act_frac is None or exp_num is None or act_num is None:
            return False, normalized
        frac_ok = exp_frac == act_frac
        tolerance = question.grading.tolerance
        if tolerance is None:
            num_ok = exp_num == act_num
        else:
            num_ok = abs(exp_num - act_num) <= Decimal(str(tolerance))
        return frac_ok and num_ok, normalized

    return normalize_text(question.answer) == normalized, normalized
