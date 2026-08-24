import math
import random

from source.fast_math.models import GeneratedQuestion, GradingSpec


_CF_HINT = "Multiply and divide by a common factor to make the problem easier."


def _is_single_digit_power_of_10(n: int) -> bool:
    """Return True for numbers like 10, 20, 300, 4000 — a single non-zero digit times a power of 10."""
    while n % 10 == 0:
        n //= 10
    return n < 10

_CF_MEDIUM_SHAPES = [(2, 2), (2, 3), (3, 3)]
_CF_HIGH_SHAPES = [(2, 4), (3, 4), (4, 4)]

# Simple numbers that make good "reduced" factors after dividing by k.
# These are the values a factor becomes AFTER the technique is applied.
_SIMPLE_TARGETS = list(range(2, 13)) + [15, 20, 25, 30, 40, 50, 75, 100, 110, 125, 150, 200]


def _gen_cf_pair(rng: random.Random, shapes: list) -> tuple:
    """Generate (a, b, k) for the multiply/divide by common factor technique.

    One of (a, b) equals simple_target * k, where simple_target is a "nice"
    number the user should reduce to by dividing by k. The other is a free
    number of the appropriate digit count.
    """
    for _ in range(200):
        da, db = rng.choice(shapes)
        k = rng.randint(2, 10)

        # The "complex" factor (shown in question) = simple_target * k,
        # and must have da digits.
        lo_a = 10 ** (da - 1) if da > 1 else 1
        hi_a = 10 ** da - 1
        lo_s = math.ceil(lo_a / k)
        hi_s = hi_a // k
        candidates = [s for s in _SIMPLE_TARGETS if lo_s <= s <= hi_s]
        if not candidates:
            continue

        simple = rng.choice(candidates)
        complex_factor = simple * k

        # The free factor has db digits.
        lo_b = 10 ** (db - 1) if db > 1 else 1
        hi_b = 10 ** db - 1
        free = rng.randint(lo_b, hi_b)

        # Randomly assign which position is complex vs free.
        a, b = (complex_factor, free) if rng.random() < 0.5 else (free, complex_factor)
        # Reject if either factor is a single digit times a power of 10 (e.g. 20, 300, 4000)
        # — multiplying by those is trivial (just scale and append zeros).
        if _is_single_digit_power_of_10(a) or _is_single_digit_power_of_10(b):
            continue
        return a, b, k

    raise RuntimeError("_gen_cf_pair failed to find valid pair")


def fast_mult_by_9(rng: random.Random) -> GeneratedQuestion:
    value = rng.randint(11, 999)
    answer = value * 9
    return GeneratedQuestion(
        question_type="fast_mult_by_9",
        topic="multiplication",
        effort="low",
        prompt=f"{value} x 9 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Multiply by 10, then subtract the original number.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "multiplier": 9},
    )


def fast_mult_by_teen(rng: random.Random) -> GeneratedQuestion:
    value = rng.randint(11, 999)
    mult = rng.randint(11, 19)
    answer = value * mult
    return GeneratedQuestion(
        question_type="fast_mult_by_teen",
        topic="multiplication",
        effort="medium",
        prompt=f"{value} x {mult} =",
        answer=str(answer),
        answer_display=str(answer),
        hint=f"Multiply each digit by {str(mult)[-1]} and add it to its neighbor from right to left.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "multiplier": mult},
    )

def fast_mult_by_25(rng: random.Random) -> GeneratedQuestion:
    value = rng.randint(4, 400)
    answer = value * 25
    return GeneratedQuestion(
        question_type="fast_mult_by_25",
        topic="multiplication",
        effort="low",
        prompt=f"{value} x 25 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Multiply by 100, then divide by 4.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "multiplier": 25},
    )


def fast_mult_by_125(rng: random.Random) -> GeneratedQuestion:
    value = rng.randint(8, 200)
    answer = value * 125
    return GeneratedQuestion(
        question_type="fast_mult_by_125",
        topic="multiplication",
        effort="medium",
        prompt=f"{value} x 125 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Multiply by 500, then divide by 4.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "multiplier": 125},
    )


def flip_percent(rng: random.Random) -> GeneratedQuestion:
    # base must be small so that "base% of percent" is easy mental math
    base = rng.choice([2, 4, 5, 8, 16, 20, 25, 40, 50])
    percent = rng.choice([p for p in [24, 32, 36, 48, 64, 72, 96, 120, 144, 200, 250] if p > base])
    answer = percent * base / 100
    prompt = f"{percent}% of {base} ="
    hint = "Flip it: x% of y equals y% of x."
    answer_text = str(int(answer)) if float(answer).is_integer() else f"{answer:.2f}".rstrip("0").rstrip(".")
    return GeneratedQuestion(
        question_type="flip_percent",
        topic="multiplication",
        effort="low",
        prompt=prompt,
        answer=answer_text,
        answer_display=answer_text,
        hint=hint,
        grading=GradingSpec.numeric(),
        metadata={"percent": percent, "base": base},
    )


def mult_large_3x3(rng: random.Random) -> GeneratedQuestion:
    a = rng.randint(100, 999)
    b = rng.randint(100, 999)
    answer = a * b
    return GeneratedQuestion(
        question_type="mult_large_3x3",
        topic="multiplication",
        effort="high",
        prompt=f"{a} x {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Try: multiply by a common factor, adjust to simpler numbers and add/subtract, use common grounds, or difference of squares.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def mult_large_3x4(rng: random.Random) -> GeneratedQuestion:
    a = rng.randint(100, 999)
    b = rng.randint(1000, 9999)
    if rng.random() < 0.5:
        a, b = b, a
    answer = a * b
    return GeneratedQuestion(
        question_type="mult_large_3x4",
        topic="multiplication",
        effort="high",
        prompt=f"{a} x {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Try: multiply by a common factor, adjust to simpler numbers and add/subtract, use common grounds, or difference of squares.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def mult_large_4x4(rng: random.Random) -> GeneratedQuestion:
    a = rng.randint(1000, 9999)
    b = rng.randint(1000, 9999)
    answer = a * b
    return GeneratedQuestion(
        question_type="mult_large_4x4",
        topic="multiplication",
        effort="high",
        prompt=f"{a} x {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Try: multiply by a common factor, adjust to simpler numbers and add/subtract, use common grounds, or difference of squares.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def mult_large_3x5(rng: random.Random) -> GeneratedQuestion:
    a = rng.randint(100, 999)
    b = rng.randint(10000, 99999)
    if rng.random() < 0.5:
        a, b = b, a
    answer = a * b
    return GeneratedQuestion(
        question_type="mult_large_3x5",
        topic="multiplication",
        effort="high",
        prompt=f"{a} x {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Try: multiply by a common factor, adjust to simpler numbers and add/subtract, use common grounds, or difference of squares.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def mult_large_5x5(rng: random.Random) -> GeneratedQuestion:
    a = rng.randint(10000, 99999)
    b = rng.randint(10000, 99999)
    answer = a * b
    return GeneratedQuestion(
        question_type="mult_large_5x5",
        topic="multiplication",
        effort="high",
        prompt=f"{a} x {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Try: multiply by a common factor, adjust to simpler numbers and add/subtract, use common grounds, or difference of squares.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


def mult_large_5x4(rng: random.Random) -> GeneratedQuestion:
    a = rng.randint(10000, 99999)
    b = rng.randint(1000, 9999)
    if rng.random() < 0.5:
        a, b = b, a
    answer = a * b
    return GeneratedQuestion(
        question_type="mult_large_5x4",
        topic="multiplication",
        effort="high",
        prompt=f"{a} x {b} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Try: multiply by a common factor, adjust to simpler numbers and add/subtract, use common grounds, or difference of squares.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b},
    )


_CG_HINT = "Use common grounds: find a shared anchor a near both numbers, then apply (a+b)(a+c) = a² + (b+c)a + bc."
_DOS_HINT = "Use difference of squares: find the midpoint a and distance b, then compute a² - b²."

# Multiples of 5 as anchors (includes multiples of 10)
_CG_MEDIUM_ANCHORS = list(range(20, 100, 5))    # 20, 25, ..., 95
_CG_HIGH_ANCHORS = list(range(100, 1000, 5))    # 100, 105, ..., 995

# Multiples of 10 as anchors for diff of squares (easier to square)
_DOS_MEDIUM_ANCHORS = list(range(20, 100, 10))   # 20, 30, ..., 90
_DOS_HIGH_ANCHORS = list(range(100, 1000, 5))    # 100, 105, ..., 995


def _gen_cg_pair(rng: random.Random, anchors: list, max_offset: int) -> tuple:
    while True:
        a = rng.choice(anchors)
        b = rng.randint(-max_offset, max_offset)
        c = rng.randint(-max_offset, max_offset)
        # b==0 or c==0: one factor equals anchor (too obvious); b==c: squaring
        if b == 0 or c == 0 or b == c:
            continue
        x, y = a + b, a + c
        if x > 0 and y > 0:
            return x, y, a, b, c


def mult_common_grounds(rng: random.Random) -> GeneratedQuestion:
    x, y, a, b, c = _gen_cg_pair(rng, _CG_MEDIUM_ANCHORS, 9)
    return GeneratedQuestion(
        question_type="mult_common_grounds",
        topic="multiplication",
        effort="medium",
        prompt=f"{x} x {y} =",
        answer=str(x * y),
        answer_display=str(x * y),
        hint=_CG_HINT,
        grading=GradingSpec.numeric(),
        metadata={"x": x, "y": y, "anchor": a, "b": b, "c": c},
    )


def mult_common_grounds_hard(rng: random.Random) -> GeneratedQuestion:
    x, y, a, b, c = _gen_cg_pair(rng, _CG_HIGH_ANCHORS, 9)
    return GeneratedQuestion(
        question_type="mult_common_grounds_hard",
        topic="multiplication",
        effort="high",
        prompt=f"{x} x {y} =",
        answer=str(x * y),
        answer_display=str(x * y),
        hint=_CG_HINT,
        grading=GradingSpec.numeric(),
        metadata={"x": x, "y": y, "anchor": a, "b": b, "c": c},
    )


def mult_diff_squares(rng: random.Random) -> GeneratedQuestion:
    a = rng.choice(_DOS_MEDIUM_ANCHORS)
    b = rng.randint(1, 9)
    x, y = a - b, a + b
    return GeneratedQuestion(
        question_type="mult_diff_squares",
        topic="multiplication",
        effort="medium",
        prompt=f"{x} x {y} =",
        answer=str(x * y),
        answer_display=str(x * y),
        hint=_DOS_HINT,
        grading=GradingSpec.numeric(),
        metadata={"x": x, "y": y, "anchor": a, "b": b},
    )


def mult_diff_squares_hard(rng: random.Random) -> GeneratedQuestion:
    a = rng.choice(_DOS_HIGH_ANCHORS)
    b = rng.randint(1, 15)
    x, y = a - b, a + b
    return GeneratedQuestion(
        question_type="mult_diff_squares_hard",
        topic="multiplication",
        effort="high",
        prompt=f"{x} x {y} =",
        answer=str(x * y),
        answer_display=str(x * y),
        hint=_DOS_HINT,
        grading=GradingSpec.numeric(),
        metadata={"x": x, "y": y, "anchor": a, "b": b},
    )


def mult_common_factor(rng: random.Random) -> GeneratedQuestion:
    a, b, factor = _gen_cf_pair(rng, _CF_MEDIUM_SHAPES)
    return GeneratedQuestion(
        question_type="mult_common_factor",
        topic="multiplication",
        effort="medium",
        prompt=f"{a} x {b} =",
        answer=str(a * b),
        answer_display=str(a * b),
        hint=_CF_HINT,
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b, "factor": factor},
    )


def mult_common_factor_hard(rng: random.Random) -> GeneratedQuestion:
    a, b, factor = _gen_cf_pair(rng, _CF_HIGH_SHAPES)
    return GeneratedQuestion(
        question_type="mult_common_factor_hard",
        topic="multiplication",
        effort="high",
        prompt=f"{a} x {b} =",
        answer=str(a * b),
        answer_display=str(a * b),
        hint=_CF_HINT,
        grading=GradingSpec.numeric(),
        metadata={"a": a, "b": b, "factor": factor},
    )


GENERATORS = [
    fast_mult_by_9,
    fast_mult_by_teen,
    fast_mult_by_25,
    fast_mult_by_125,
    flip_percent,
    mult_common_grounds,
    mult_common_grounds_hard,
    mult_diff_squares,
    mult_diff_squares_hard,
    mult_common_factor,
    mult_common_factor_hard,
    mult_large_3x3,
    mult_large_3x4,
    mult_large_4x4,
    mult_large_3x5,
    mult_large_5x5,
    mult_large_5x4,
]
