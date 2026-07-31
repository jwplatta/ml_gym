import random

from source.fast_math.models import GeneratedQuestion, GradingSpec

# Shapes: (digits_a, digits_b)
_SHAPES = [(3, 1), (3, 2), (3, 3), (2, 2), (2, 1)]

_DIGIT_RANGES = {1: (1, 9), 2: (10, 99), 3: (100, 999)}


def _rand_n_digits(rng: random.Random, digits: int) -> int:
    lo, hi = _DIGIT_RANGES[digits]
    return rng.randint(lo, hi)


def _near_round(rng: random.Random, digits: int) -> tuple[int, int]:
    """Return (value, adjustment) where value is within 1-4 of a round number."""
    if digits == 1:
        base = rng.choice([10, 20, 30])
    elif digits == 2:
        base = rng.choice([20, 30, 40, 50, 60, 70, 80, 90, 100])
    else:
        base = rng.choice([200, 300, 400, 500, 600, 700, 800, 900, 1000])
    adjustment = rng.randint(1, 4)
    direction = rng.choice([-1, 1])
    value = base + direction * adjustment
    # keep value positive and within digit range
    lo, hi = _DIGIT_RANGES[digits]
    value = max(lo, min(hi, value))
    actual_adjustment = value - base
    return value, actual_adjustment


def addition_rounding(rng: random.Random) -> GeneratedQuestion:
    digits_a, digits_b = rng.choice(_SHAPES)
    # at least one operand should be near a round number
    if rng.random() < 0.5:
        a, adj = _near_round(rng, digits_a)
        b = _rand_n_digits(rng, digits_b)
        round_a = a - adj
        hint = (
            f"Round {a} to {round_a} (adjust by {adj:+d}). "
            f"Compute {round_a} + {b}, "
            f"then correct by adding back the adjustment ({adj:+d})."
        )
    else:
        a = _rand_n_digits(rng, digits_a)
        b, adj = _near_round(rng, digits_b)
        round_b = b - adj
        hint = (
            f"Round {b} to {round_b} (adjust by {adj:+d}). "
            f"Compute {a} + {round_b}, "
            f"then correct by adding back the adjustment ({adj:+d})."
        )
    answer = a + b
    return GeneratedQuestion(
        question_type="addition_rounding",
        topic="addition-subtraction",
        subtopic="addition",
        effort="low",
        prompt=f"{a} + {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint=hint,
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def addition_digit_matching(rng: random.Random) -> GeneratedQuestion:
    digits_a, digits_b = rng.choice(_SHAPES)
    a = _rand_n_digits(rng, digits_a)
    b = _rand_n_digits(rng, digits_b)
    answer = a + b

    # Build matching breakdown hint
    a_digits = [(a // 100) % 10, (a // 10) % 10, a % 10]
    b_digits = [(b // 100) % 10, (b // 10) % 10, b % 10]
    multipliers = [100, 10, 1]
    steps = []
    for av, bv, mult in zip(a_digits, b_digits, multipliers, strict=True):
        if av == 0 and bv == 0:
            continue
        steps.append(f"{av * mult} + {bv * mult} = {(av + bv) * mult}")
    hint = "Add place by place, then sum the results: " + ", ".join(steps) + "."

    return GeneratedQuestion(
        question_type="addition_digit_matching",
        topic="addition-subtraction",
        subtopic="addition",
        effort="low",
        prompt=f"{a} + {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint=hint,
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def subtraction_rounding(rng: random.Random) -> GeneratedQuestion:
    digits_a, digits_b = rng.choice(_SHAPES)
    # ensure a > b so result is positive
    a = _rand_n_digits(rng, digits_a)
    b, adj = _near_round(rng, digits_b)
    # keep b < a
    b = min(b, a - 1)
    round_b = b - adj
    answer = a - b
    hint = (
        f"Round {b} to {round_b} (adjust by {adj:+d}). "
        f"Compute {a} - {round_b}, "
        f"then correct by subtracting the adjustment ({adj:+d})."
    )
    return GeneratedQuestion(
        question_type="subtraction_rounding",
        topic="addition-subtraction",
        subtopic="subtraction",
        effort="low",
        prompt=f"{a} - {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint=hint,
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def subtraction_digit_matching(rng: random.Random) -> GeneratedQuestion:
    digits_a, digits_b = rng.choice(_SHAPES)
    a = _rand_n_digits(rng, digits_a)
    b = _rand_n_digits(rng, digits_b)
    # ensure a > b
    if b >= a:
        a, b = max(a, b) + rng.randint(1, 10), min(a, b)
    answer = a - b

    a_digits = [(a // 100) % 10, (a // 10) % 10, a % 10]
    b_digits = [(b // 100) % 10, (b // 10) % 10, b % 10]
    multipliers = [100, 10, 1]
    steps = []
    for av, bv, mult in zip(a_digits, b_digits, multipliers, strict=True):
        if av == 0 and bv == 0:
            continue
        steps.append(f"{av * mult} - {bv * mult} = {(av - bv) * mult}")
    hint = "Subtract place by place, then sum the results: " + ", ".join(steps) + "."

    return GeneratedQuestion(
        question_type="subtraction_digit_matching",
        topic="addition-subtraction",
        subtopic="subtraction",
        effort="low",
        prompt=f"{a} - {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint=hint,
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def _rand_decimal(rng: random.Random, digits: int) -> float:
    """Return a positive decimal with 1–3 integer digits and 0–2 decimal places."""
    integer_part = _rand_n_digits(rng, digits)
    decimal_places = rng.randint(0, 2)
    if decimal_places == 0:
        return float(integer_part)
    fractional_part = rng.randint(1, 10 ** decimal_places - 1)
    return round(integer_part + fractional_part / (10 ** decimal_places), decimal_places)


def _fmt(value: float) -> str:
    """Format a decimal, stripping unnecessary trailing zeros."""
    return f"{value:.2f}".rstrip("0").rstrip(".")


def decimal_subtraction(rng: random.Random) -> GeneratedQuestion:
    digits_a, digits_b = rng.choice(_SHAPES)
    a = _rand_decimal(rng, digits_a)
    b = _rand_decimal(rng, digits_b)
    answer = round(a - b, 2)
    answer_str = _fmt(answer)
    return GeneratedQuestion(
        question_type="decimal_subtraction",
        topic="addition-subtraction",
        subtopic="subtraction",
        effort="low",
        prompt=f"{_fmt(a)} - {_fmt(b)} =",
        answer=answer_str,
        answer_display=answer_str,
        hint="Align the decimal points and subtract column by column.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "b": b},
    )


GENERATORS = [
    addition_rounding,
    addition_digit_matching,
    subtraction_rounding,
    subtraction_digit_matching,
    decimal_subtraction,
]
