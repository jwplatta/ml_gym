import random

from source.fast_math.models import GeneratedQuestion, GradingSpec

_DIGIT_RANGES = {1: (1, 9), 2: (10, 99), 3: (100, 999)}
_SHAPES = [(3, 2), (3, 3), (2, 2)]


def _rand_n_digits(rng: random.Random, digits: int) -> int:
    lo, hi = _DIGIT_RANGES[digits]
    return rng.randint(lo, hi)


def _rand_decimal(rng: random.Random, digits: int, decimal_places: int) -> float:
    integer_part = _rand_n_digits(rng, digits)
    fractional_part = rng.randint(1, 10 ** decimal_places - 1)
    return round(integer_part + fractional_part / (10 ** decimal_places), decimal_places)


def _fmt(value: float) -> str:
    return f"{value:.2f}".rstrip("0").rstrip(".")


def _has_carrying(a: float, b: float) -> bool:
    a_cents = round(a * 100)
    b_cents = round(b * 100)
    carry = 0
    for _ in range(7):
        col_sum = (a_cents % 10) + (b_cents % 10) + carry
        if col_sum >= 10:
            return True
        carry = col_sum // 10
        a_cents //= 10
        b_cents //= 10
    return False


def _has_borrowing(a: int, b: int) -> bool:
    """True if subtracting b from a requires borrowing in any column."""
    while a > 0 or b > 0:
        if (a % 10) < (b % 10):
            return True
        a //= 10
        b //= 10
    return False


def _has_int_carrying(a: int, b: int) -> bool:
    carry = 0
    while a > 0 or b > 0:
        col_sum = (a % 10) + (b % 10) + carry
        if col_sum >= 10:
            return True
        carry = col_sum // 10
        a //= 10
        b //= 10
    return False


# ── Integer addition ───────────────────────────────────────────────────────────

def integer_addition_easy(rng: random.Random) -> GeneratedQuestion:
    """No carrying required."""
    digits_a, digits_b = rng.choice(_SHAPES)
    a, b = 0, 0
    for _ in range(50):
        a = _rand_n_digits(rng, digits_a)
        b = _rand_n_digits(rng, digits_b)
        if not _has_int_carrying(a, b):
            break
    answer = a + b
    return GeneratedQuestion(
        question_type="integer_addition_easy",
        topic="addition-subtraction",
        subtopic="addition",
        effort="low",
        prompt=f"{a} + {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Add each column right to left.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def integer_addition_carrying(rng: random.Random) -> GeneratedQuestion:
    """Carrying required in at least one column."""
    digits_a, digits_b = rng.choice([(3, 2), (3, 3)])
    a, b = 0, 0
    for _ in range(50):
        a = _rand_n_digits(rng, digits_a)
        b = _rand_n_digits(rng, digits_b)
        if _has_int_carrying(a, b):
            break
    answer = a + b
    return GeneratedQuestion(
        question_type="integer_addition_carrying",
        topic="addition-subtraction",
        subtopic="addition",
        effort="low",
        prompt=f"{a} + {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Add each column right to left, carrying when a column sums to 10 or more.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


# ── Integer subtraction ────────────────────────────────────────────────────────

def integer_subtraction_easy(rng: random.Random) -> GeneratedQuestion:
    """No borrowing required, a > b."""
    digits_a, digits_b = rng.choice(_SHAPES)
    a, b = _rand_n_digits(rng, digits_a), _rand_n_digits(rng, digits_b)
    for _ in range(100):
        a = _rand_n_digits(rng, digits_a)
        b = _rand_n_digits(rng, digits_b)
        if a > b and not _has_borrowing(a, b):
            break
    answer = a - b
    return GeneratedQuestion(
        question_type="integer_subtraction_easy",
        topic="addition-subtraction",
        subtopic="subtraction",
        effort="low",
        prompt=f"{a} - {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Subtract each column right to left.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def integer_subtraction_borrowing(rng: random.Random) -> GeneratedQuestion:
    """Borrowing required in at least one column, a > b."""
    digits_a, digits_b = rng.choice(_SHAPES)
    a, b = _rand_n_digits(rng, digits_a), _rand_n_digits(rng, digits_b)
    for _ in range(100):
        a = _rand_n_digits(rng, digits_a)
        b = _rand_n_digits(rng, digits_b)
        if a > b and _has_borrowing(a, b):
            break
    answer = a - b
    return GeneratedQuestion(
        question_type="integer_subtraction_borrowing",
        topic="addition-subtraction",
        subtopic="subtraction",
        effort="low",
        prompt=f"{a} - {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Subtract each column right to left, borrowing from the next column when needed.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


# ── Decimal subtraction (positive result) ─────────────────────────────────────

def decimal_subtraction_positive_easy(rng: random.Random) -> GeneratedQuestion:
    """Both operands have tenths only, positive result."""
    digits_a, digits_b = rng.choice(_SHAPES)
    a, b = _rand_decimal(rng, digits_a, 1), _rand_decimal(rng, digits_b, 1)
    for _ in range(100):
        a = _rand_decimal(rng, digits_a, 1)
        b = _rand_decimal(rng, digits_b, 1)
        if a > b:
            break
    answer = round(a - b, 2)
    return GeneratedQuestion(
        question_type="decimal_subtraction_positive_easy",
        topic="addition-subtraction",
        subtopic="subtraction",
        effort="low",
        prompt=f"{_fmt(a)} - {_fmt(b)} =",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint="Align the decimal points, then subtract column by column.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "b": b},
    )


def decimal_subtraction_positive_medium(rng: random.Random) -> GeneratedQuestion:
    """Mixed decimal places (tenths and hundredths), positive result."""
    digits_a, digits_b = rng.choice(_SHAPES)
    dp_a, dp_b = rng.choice([(1, 2), (2, 1)])
    a, b = _rand_decimal(rng, digits_a, dp_a), _rand_decimal(rng, digits_b, dp_b)
    for _ in range(100):
        dp_a, dp_b = rng.choice([(1, 2), (2, 1)])
        a = _rand_decimal(rng, digits_a, dp_a)
        b = _rand_decimal(rng, digits_b, dp_b)
        if a > b:
            break
    answer = round(a - b, 2)
    return GeneratedQuestion(
        question_type="decimal_subtraction_positive_medium",
        topic="addition-subtraction",
        subtopic="subtraction",
        effort="medium",
        prompt=f"{_fmt(a)} - {_fmt(b)} =",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint="Align the decimal points, pad the shorter number with a zero, then subtract column by column.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "b": b},
    )


# ── Decimal subtraction (negative result) ─────────────────────────────────────

def decimal_subtraction_negative_easy(rng: random.Random) -> GeneratedQuestion:
    """Both operands have tenths only, negative result (b > a)."""
    digits_b, digits_a = rng.choice(_SHAPES)  # swap so b gets the larger digit count
    a, b = _rand_decimal(rng, digits_a, 1), _rand_decimal(rng, digits_b, 1)
    for _ in range(100):
        a = _rand_decimal(rng, digits_a, 1)
        b = _rand_decimal(rng, digits_b, 1)
        if b > a:
            break
    answer = round(a - b, 2)
    return GeneratedQuestion(
        question_type="decimal_subtraction_negative_easy",
        topic="addition-subtraction",
        subtopic="subtraction",
        effort="medium",
        prompt=f"{_fmt(a)} - {_fmt(b)} =",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint="Align the decimal points, compute b - a, then negate the result.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "b": b},
    )


def decimal_subtraction_negative_medium(rng: random.Random) -> GeneratedQuestion:
    """Mixed decimal places (tenths and hundredths), negative result (b > a)."""
    digits_b, digits_a = rng.choice(_SHAPES)  # swap so b gets the larger digit count
    dp_a, dp_b = rng.choice([(1, 2), (2, 1)])
    a, b = _rand_decimal(rng, digits_a, dp_a), _rand_decimal(rng, digits_b, dp_b)
    for _ in range(100):
        dp_a, dp_b = rng.choice([(1, 2), (2, 1)])
        a = _rand_decimal(rng, digits_a, dp_a)
        b = _rand_decimal(rng, digits_b, dp_b)
        if b > a:
            break
    answer = round(a - b, 2)
    return GeneratedQuestion(
        question_type="decimal_subtraction_negative_medium",
        topic="addition-subtraction",
        subtopic="subtraction",
        effort="medium",
        prompt=f"{_fmt(a)} - {_fmt(b)} =",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint="Align the decimal points, pad the shorter number with a zero, compute b - a, then negate.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "b": b},
    )


# ── Decimal addition with carrying ────────────────────────────────────────────

def decimal_addition_carrying_easy(rng: random.Random) -> GeneratedQuestion:
    """Both operands have tenths only, at least one carry required."""
    digits_a, digits_b = rng.choice(_SHAPES)
    a, b = 0.0, 0.0
    for _ in range(50):
        a = _rand_decimal(rng, digits_a, 1)
        b = _rand_decimal(rng, digits_b, 1)
        if _has_carrying(a, b):
            break
    answer = round(a + b, 2)
    return GeneratedQuestion(
        question_type="decimal_addition_carrying_easy",
        topic="addition-subtraction",
        subtopic="addition",
        effort="low",
        prompt=f"{_fmt(a)} + {_fmt(b)} =",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint="Align the decimal points, then add column by column carrying when a column sums to 10 or more.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "b": b},
    )


def decimal_addition_carrying_medium(rng: random.Random) -> GeneratedQuestion:
    """Mixed decimal places (tenths and hundredths), at least one carry required."""
    digits_a, digits_b = rng.choice(_SHAPES)
    a, b = 0.0, 0.0
    for _ in range(50):
        dp_a, dp_b = rng.choice([(1, 2), (2, 1)])
        a = _rand_decimal(rng, digits_a, dp_a)
        b = _rand_decimal(rng, digits_b, dp_b)
        if _has_carrying(a, b):
            break
    answer = round(a + b, 2)
    return GeneratedQuestion(
        question_type="decimal_addition_carrying_medium",
        topic="addition-subtraction",
        subtopic="addition",
        effort="medium",
        prompt=f"{_fmt(a)} + {_fmt(b)} =",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint="Align the decimal points, pad with a zero where needed, then add column by column carrying when a column sums to 10 or more.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "b": b},
    )


GENERATORS = [
    integer_addition_easy,
    integer_addition_carrying,
    integer_subtraction_easy,
    integer_subtraction_borrowing,
    decimal_subtraction_positive_easy,
    decimal_subtraction_positive_medium,
    decimal_subtraction_negative_easy,
    decimal_subtraction_negative_medium,
    decimal_addition_carrying_easy,
    decimal_addition_carrying_medium,
]
