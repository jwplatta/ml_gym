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
        prompt=f"{value}^2 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Use (a+b)^2 = a^2 + 2ab + b^2 around the nearest multiple of 10.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "base": base, "offset": offset},
    )


def two_digit_fives(rng: random.Random) -> GeneratedQuestion:
    tens = rng.randint(2, 19)
    value = tens * 10 + 5
    answer = value * value
    return GeneratedQuestion(
        question_type="two_digit_fives",
        topic="squaring",
        prompt=f"{value} x {value} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="For numbers ending in 5: n(n+1) followed by 25.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "tens": tens},
    )


def nearest_fives(rng: random.Random) -> GeneratedQuestion:
    base = rng.randint(4, 24) * 5
    offset = rng.choice([-3, -2, -1, 1, 2])
    value = base + offset
    answer = value * value
    return GeneratedQuestion(
        question_type="nearest_fives",
        topic="squaring",
        prompt=f"{value}^2 =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Find the nearest multiple of 5, write x = a + b, then use (a + b)^2.",
        grading=GradingSpec.numeric(),
        metadata={"value": value, "base": base, "offset": offset},
    )


def power_of_two(rng: random.Random) -> GeneratedQuestion:
    exponent = rng.randint(5, 12)
    answer = 2**exponent
    return GeneratedQuestion(
        question_type="power_of_two",
        topic="squaring",
        prompt=f"2^{exponent} =",
        answer=str(answer),
        answer_display=str(answer),
        hint="Build from repeated doubling.",
        grading=GradingSpec.numeric(),
        metadata={"base": 2, "exponent": exponent},
    )


GENERATORS = [
    square_n_nearest_tens,
    two_digit_fives,
    nearest_fives,
    power_of_two,
]
