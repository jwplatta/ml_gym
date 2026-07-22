import random

from source.fast_math.models import GeneratedQuestion, GradingSpec


def count_numbers_with_at_least_k_zeroes(upper_bound: int, minimum_zeroes: int) -> int:
    return sum(
        1
        for value in range(1, upper_bound + 1)
        if str(value).count("0") >= minimum_zeroes
    )


def integers_with_at_least_k_zeroes(rng: random.Random) -> GeneratedQuestion:
    while True:
        upper_bound = rng.choice([100, 1000, 10000, 100000])
        digits = len(str(upper_bound))
        max_zeroes = max(1, min(3, digits - 1))
        minimum_zeroes = rng.randint(1, max_zeroes)
        answer = count_numbers_with_at_least_k_zeroes(upper_bound, minimum_zeroes)
        if answer >= 10:
            break
    zero_word = "zero" if minimum_zeroes == 1 else "zeroes"

    return GeneratedQuestion(
        question_type="integers_with_at_least_k_zeroes",
        topic="counting",
        subtopic="combinations",
        prompt=(
            f"How many integers between 1 and {upper_bound}, inclusive, "
            f"contain at least {minimum_zeroes} {zero_word}?"
        ),
        answer=str(answer),
        answer_display=str(answer),
        hint=(
            "Count by digit length and use complement counting. "
            f"Subtract the numbers with fewer than {minimum_zeroes} {zero_word} from the total."
        ),
        grading=GradingSpec.numeric(),
        metadata={
            "upper_bound": upper_bound,
            "minimum_zeroes": minimum_zeroes,
            "fraction": str(answer),
        },
    )


GENERATORS = [
    integers_with_at_least_k_zeroes,
]
