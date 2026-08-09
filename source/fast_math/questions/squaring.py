import random

from source.fast_math.models import GeneratedQuestion, GradingSpec


def square_n_nearest_tens(rng: random.Random) -> GeneratedQuestion:
    base = rng.randint(2, 19) * 10
    offset = rng.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    value = base + offset
    answer = value * value
    return GeneratedQuestion(
        question_type="square_n_nearest_tens",
        topic="squaring",
        effort="medium",
        prompt=f"{value}^2 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Use (a+b)^2 = a^2 + 2ab + b^2 around the nearest multiple of 10.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "base": base, "offset": offset},
    )


def two_digit_fives(rng: random.Random) -> GeneratedQuestion:
    # 2-digit numbers ending in 5: 15, 25, ..., 95
    tens = rng.randint(1, 9)
    value = tens * 10 + 5
    answer = value * value
    n = tens  # the part before the 5
    return GeneratedQuestion(
        question_type="two_digit_fives",
        topic="squaring",
        effort="low",
        prompt=f"{value}^2 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Take the digits before the 5, multiply by the next integer, then append 25.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "n": n},
    )


def three_digit_fives(rng: random.Random) -> GeneratedQuestion:
    # 3-digit numbers ending in 5: 105, 115, ..., 995
    prefix = rng.randint(10, 99)
    value = prefix * 10 + 5
    answer = value * value
    n = prefix  # the part before the 5
    return GeneratedQuestion(
        question_type="three_digit_fives",
        topic="squaring",
        effort="medium",
        prompt=f"{value}^2 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Take the digits before the 5, multiply by the next integer, then append 25.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "n": n},
    )


def four_digit_fives(rng: random.Random) -> GeneratedQuestion:
    # 4-digit numbers ending in 5: 1005, 1015, ..., 9995
    prefix = rng.randint(100, 999)
    value = prefix * 10 + 5
    answer = value * value
    n = prefix  # the part before the 5
    return GeneratedQuestion(
        question_type="four_digit_fives",
        topic="squaring",
        effort="high",
        prompt=f"{value}^2 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Take the digits before the 5, multiply by the next integer, then append 25.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "n": n},
    )


def nearest_fives(rng: random.Random) -> GeneratedQuestion:
    base = rng.randint(4, 24) * 5
    offset = rng.choice([-3, -2, -1, 1, 2])
    value = base + offset
    answer = value * value
    return GeneratedQuestion(
        question_type="nearest_fives",
        topic="squaring",
        effort="medium",
        prompt=f"{value}^2 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Find the nearest multiple of 5, write x = a + b, then use (a + b)^2.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "base": base, "offset": offset},
    )


def power_of_two(rng: random.Random) -> GeneratedQuestion:
    exponent = rng.randint(3, 10)
    answer = 2**exponent
    return GeneratedQuestion(
        question_type="power_of_two",
        topic="squaring",
        effort="low",
        prompt=f"2^{exponent} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Memorize.",
        grading=GradingSpec.numeric(),
        metadata={"base": 2, "exponent": exponent},
    )


def fast_two_digits(rng: random.Random) -> GeneratedQuestion:
    num = rng.randint(20, 99)

    while num % 5 == 0 or num % 10 == 0:
        num = rng.randint(20, 99)

    ans = num ** 2

    return GeneratedQuestion(
        question_type="fast_two_digits",
        topic="squaring",
        effort="high",
        prompt=f"{num}^2 =",
        answer=str(ans),
        answer_display=str(ans),
        hint="1. Square the digits and place them next to each other.\n2. Then multiply them together, double them, add a zero.\n3. Then add the two results together.",
        grading=GradingSpec.numeric(),
        metadata={"base": num, "exponent": 2},
    )

_MEMORIZED_SQUARES = [n for n in range(11, 32) if n % 10 != 0]


def memorized_squares(rng: random.Random) -> GeneratedQuestion:
    value = rng.choice(_MEMORIZED_SQUARES)
    answer = value * value
    return GeneratedQuestion(
        question_type="memorized_squares",
        topic="squaring",
        effort="low",
        prompt=f"{value}^2 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Memorize.",
        grading=GradingSpec.numeric(),
        metadata={"value": value},
    )


def square_3_digit(rng: random.Random) -> GeneratedQuestion:
    value = rng.randint(100, 999)
    answer = value * value
    nearest_hundred = round(value / 100) * 100
    offset = value - nearest_hundred
    return GeneratedQuestion(
        question_type="square_3_digit",
        topic="squaring",
        effort="high",
        prompt=f"{value}^2 =",
        answer=str(answer),
        answer_display=str(answer),
        hint=f"Use (a+b)^2 around the nearest hundred ({nearest_hundred}): a^2 + 2ab + b^2 where b={offset:+d}.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "nearest_hundred": nearest_hundred, "offset": offset},
    )



def large_power_of_two(rng: random.Random) -> GeneratedQuestion:
    exponent = rng.randint(11, 20)
    answer = 2**exponent
    return GeneratedQuestion(
        question_type="large_power_of_two",
        topic="squaring",
        effort="high",
        prompt=f"2^{exponent} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Double from a known power of 2 you've memorized.",
        grading=GradingSpec.numeric(),
        metadata={"base": 2, "exponent": exponent},
    )


GENERATORS = [
    square_n_nearest_tens,
    two_digit_fives,
    three_digit_fives,
    four_digit_fives,
    power_of_two,
    fast_two_digits,
    memorized_squares,
    square_3_digit,
    large_power_of_two,
]
