import random

from source.fast_math.models import GeneratedQuestion, GradingSpec


def fast_mult_by_9(rng: random.Random) -> GeneratedQuestion:
    value = rng.randint(11, 999)
    answer = value * 9
    return GeneratedQuestion(
        question_type="fast_mult_by_9",
        topic="multiplication",
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
        prompt=prompt,
        answer=answer_text,
        answer_display=answer_text,
        hint=hint,
        grading=GradingSpec.numeric(),
        metadata={"percent": percent, "base": base},
    )


GENERATORS = [
    fast_mult_by_9,
    fast_mult_by_teen,
    fast_mult_by_25,
    fast_mult_by_125,
    flip_percent,
]
