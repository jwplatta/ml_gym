import random
from math import gcd

from source.fast_math.models import GeneratedQuestion, GradingSpec


# Powers of 10 and 1 to exclude as divisors/dividends
_EXCLUDED_DIVISORS = {1, 10, 100}
_POWERS_OF_10 = {10, 100, 1000, 10000}

# Easy shapes: (dividend_digits, divisor_digits)
_EASY_SHAPES = [(2, 2), (3, 2), (3, 3), (4, 1)]


def _rand_n_digits(rng: random.Random, digits: int) -> int:
    lo = 10 ** (digits - 1) if digits > 1 else 1
    hi = 10 ** digits - 1
    return rng.randint(lo, hi)


def _is_trivial_quotient(quotient: int) -> bool:
    """Quotients that are 1 (dividend == divisor) or powers of 10 are too obvious."""
    return quotient == 1 or quotient in _POWERS_OF_10


def _random_exact_dividend(rng: random.Random, divisor: int, digits: int) -> int:
    """Return a dividend that is exactly divisible by divisor with the given digit count."""
    low = 10 ** (digits - 1) if digits > 1 else 1
    high = 10 ** digits - 1
    first_mult = ((low + divisor - 1) // divisor) * divisor
    last_mult = (high // divisor) * divisor
    if first_mult > last_mult:
        raise ValueError(f"No valid multiple of {divisor} in [{low}, {high}]")
    k = rng.randint(first_mult // divisor, last_mult // divisor)
    return k * divisor


def _simplifiable(dividend: int, divisor: int) -> bool:
    """True if both are even or both are divisible by 5 (can shortcut via simplification)."""
    return (dividend % 2 == 0 and divisor % 2 == 0) or (dividend % 5 == 0 and divisor % 5 == 0)


def div_easy(rng: random.Random) -> GeneratedQuestion:
    """Easy division: 2d/2d, 3d/2d, 3d/3d, or 4d/1d.

    Avoids divisor 11 (covered by reverse fast x11), trivial quotients,
    and both-even / both-divisible-by-5 pairs for same-scale problems.
    """
    dividend_digits, divisor_digits = rng.choice(_EASY_SHAPES)
    same_scale = dividend_digits <= 3  # 4d/1d doesn't need the simplification filter
    while True:
        divisor = _rand_n_digits(rng, divisor_digits)
        if divisor in _EXCLUDED_DIVISORS or divisor == 11:
            continue
        dividend = _random_exact_dividend(rng, divisor, dividend_digits)
        quotient = dividend // divisor
        if _is_trivial_quotient(quotient):
            continue
        if same_scale and _simplifiable(dividend, divisor):
            continue
        break
    return GeneratedQuestion(
        question_type="div_easy",
        topic="division",
        effort="low",
        prompt=f"{dividend} / {divisor} =",
        answer=str(quotient),
        answer_display=str(quotient),
        hint="Use the digit or search method.",
        grading=GradingSpec.numeric(),
        metadata={"dividend": dividend, "divisor": divisor, "quotient": quotient,
                  "dividend_digits": dividend_digits, "divisor_digits": divisor_digits},
    )


_MEDIUM_SHAPES = [(4, 2), (4, 3)]


def div_medium(rng: random.Random) -> GeneratedQuestion:
    """Medium division: 4-digit dividend, 2- or 3-digit divisor."""
    dividend_digits, divisor_digits = rng.choice(_MEDIUM_SHAPES)
    while True:
        divisor = _rand_n_digits(rng, divisor_digits)
        if divisor in _EXCLUDED_DIVISORS or divisor == 11:
            continue
        dividend = _random_exact_dividend(rng, divisor, dividend_digits)
        quotient = dividend // divisor
        if _is_trivial_quotient(quotient):
            continue
        if _simplifiable(dividend, divisor):
            continue
        break
    return GeneratedQuestion(
        question_type="div_medium",
        topic="division",
        effort="medium",
        prompt=f"{dividend} / {divisor} =",
        answer=str(quotient),
        answer_display=str(quotient),
        hint="Use the digit or search method.",
        grading=GradingSpec.numeric(),
        metadata={"dividend": dividend, "divisor": divisor, "quotient": quotient,
                  "dividend_digits": dividend_digits, "divisor_digits": divisor_digits},
    )


_EVEN_DIVISORS_1_2 = [d for d in range(2, 100) if d % 2 == 0 and d not in _EXCLUDED_DIVISORS]
_MULT5_DIVISORS_1_2 = [d for d in range(5, 100) if d % 5 == 0 and d % 10 != 0 and d not in _EXCLUDED_DIVISORS]


def div_simpler_method(rng: random.Random) -> GeneratedQuestion:
    """
    Simpler method:
    - Both even: divide dividend and divisor by 2 repeatedly
    - Both multiples of 5: double both, drop a zero
    """
    strategy = rng.choice(["both_even", "both_mult5"])

    if strategy == "both_even":
        divisor = rng.choice(_EVEN_DIVISORS_1_2)
        dividend = _random_exact_dividend(rng, divisor, rng.randint(2, 4))
        hint = "Use simpler method. Both even — divide both by 2."
    else:
        while True:
            divisor = rng.choice(_MULT5_DIVISORS_1_2)
            dividend = _random_exact_dividend(rng, divisor * 5 // gcd(divisor, 5), rng.randint(2, 4))
            if dividend % 10 != 0:  # ends in 5, not 0
                break
        hint = "Use simpler method. Both multiples of 5 — double both and drop a zero."

    quotient = dividend // divisor
    return GeneratedQuestion(
        question_type="div_simpler_method",
        topic="division",
        effort="low",
        prompt=f"{dividend} / {divisor} =",
        answer=str(quotient),
        answer_display=str(quotient),
        hint=hint,
        grading=GradingSpec.numeric(),
        metadata={"dividend": dividend, "divisor": divisor, "quotient": quotient, "strategy": strategy},
    )


def div_reverse_fast_x11(rng: random.Random) -> GeneratedQuestion:
    """Reverse fast x11: divisor is always 11, dividend is a 2-4 digit multiple of 11."""
    divisor = 11
    dividend = _random_exact_dividend(rng, divisor, 3)
    quotient = dividend // divisor
    return GeneratedQuestion(
        question_type="div_reverse_fast_x11",
        topic="division",
        effort="low",
        prompt=f"{dividend} / {divisor} =",
        answer=str(quotient),
        answer_display=str(quotient),
        hint="Use reverse fast x11 method.",
        grading=GradingSpec.numeric(),
        metadata={"dividend": dividend, "divisor": divisor, "quotient": quotient},
    )


GENERATORS = [
    div_easy,
    div_medium,
    div_simpler_method,
    div_reverse_fast_x11,
]
