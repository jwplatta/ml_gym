import random
from math import gcd

from source.fast_math.models import GeneratedQuestion, GradingSpec


def _make_divisor_choices(min_divisor: int, max_divisor: int, excluded: set[int]) -> list[int]:
    return [d for d in range(min_divisor, max_divisor + 1) if d not in excluded]


# Powers of 10 and 1 to exclude as divisors
_EXCLUDED_DIVISORS = {1, 10, 100}

# All valid 1-2 digit divisors (2-99, excluding 1, 10, 100)
_DIVISORS_1_2_DIGIT = [d for d in range(2, 100) if d not in _EXCLUDED_DIVISORS]


def _random_exact_dividend(rng: random.Random, divisor: int, min_digits: int, max_digits: int) -> int:
    """Return a dividend that is exactly divisible by divisor, with digit count in [min_digits, max_digits]."""
    low = 10 ** (min_digits - 1)
    high = 10 ** max_digits - 1
    first_mult = ((low + divisor - 1) // divisor) * divisor
    last_mult = (high // divisor) * divisor
    if first_mult > last_mult:
        raise ValueError(f"No valid multiple of {divisor} in [{low}, {high}]")
    k = rng.randint(first_mult // divisor, last_mult // divisor)
    return k * divisor


def div_digit_method(rng: random.Random) -> GeneratedQuestion:
    """Digit method: 1-2 digit divisors, 2-4 digit dividends."""
    divisor = rng.choice(_DIVISORS_1_2_DIGIT)
    # Use 2-4 digit dividends; ensure quotient has at least 2 digits so the method is meaningful
    dividend = _random_exact_dividend(rng, divisor, 2, 4)
    quotient = dividend // divisor
    return GeneratedQuestion(
        question_type="div_digit_method",
        topic="division",
        prompt=f"{dividend} / {divisor} =",
        answer=str(quotient),
        answer_display=str(quotient),
        hint="Use digit method.",
        grading=GradingSpec.numeric(),
        metadata={"dividend": dividend, "divisor": divisor, "quotient": quotient},
    )


def div_simpler_method(rng: random.Random) -> GeneratedQuestion:
    """
    Simpler method:
    - Both even: divide dividend and divisor by 2 repeatedly
    - Both multiples of 5: double both, drop a zero
    """
    strategy = rng.choice(["both_even", "both_mult5"])

    if strategy == "both_even":
        even_divisors = [d for d in _DIVISORS_1_2_DIGIT if d % 2 == 0]
        divisor = rng.choice(even_divisors)
        dividend = _random_exact_dividend(rng, divisor, 2, 4)
        hint = "Use simpler method. Both even — divide both by 2."
    else:
        mult5_divisors = [d for d in _DIVISORS_1_2_DIGIT if d % 5 == 0]
        divisor = rng.choice(mult5_divisors)
        # Ensure dividend is also a multiple of 5
        dividend = _random_exact_dividend(rng, divisor * 5 // gcd(divisor, 5), 2, 4)
        # lcm(divisor, 5) guarantees dividend divisible by both divisor and 5
        hint = "Use simpler method. Both multiples of 5 — double both and drop a zero."

    quotient = dividend // divisor
    return GeneratedQuestion(
        question_type="div_simpler_method",
        topic="division",
        prompt=f"{dividend} / {divisor} =",
        answer=str(quotient),
        answer_display=str(quotient),
        hint=hint,
        grading=GradingSpec.numeric(),
        metadata={"dividend": dividend, "divisor": divisor, "quotient": quotient, "strategy": strategy},
    )


def div_search_method(rng: random.Random) -> GeneratedQuestion:
    """Search method: any 1-2 digit divisor, 2-4 digit dividend."""
    divisor = rng.choice(_DIVISORS_1_2_DIGIT)
    dividend = _random_exact_dividend(rng, divisor, 2, 4)
    quotient = dividend // divisor
    return GeneratedQuestion(
        question_type="div_search_method",
        topic="division",
        prompt=f"{dividend} / {divisor} =",
        answer=str(quotient),
        answer_display=str(quotient),
        hint="Use search method.",
        grading=GradingSpec.numeric(),
        metadata={"dividend": dividend, "divisor": divisor, "quotient": quotient},
    )


def div_reverse_fast_x11(rng: random.Random) -> GeneratedQuestion:
    """
    Reverse fast x11: divisor is always 11.
    Dividend is a 2–4 digit multiple of 11.
    """
    divisor = 11
    dividend = _random_exact_dividend(rng, divisor, 2, 4)
    quotient = dividend // divisor
    return GeneratedQuestion(
        question_type="div_reverse_fast_x11",
        topic="division",
        prompt=f"{dividend} / {divisor} =",
        answer=str(quotient),
        answer_display=str(quotient),
        hint="Use reverse fast x11 method.",
        grading=GradingSpec.numeric(),
        metadata={"dividend": dividend, "divisor": divisor, "quotient": quotient},
    )


GENERATORS = [
    div_digit_method,
    div_simpler_method,
    div_search_method,
    div_reverse_fast_x11,
]
