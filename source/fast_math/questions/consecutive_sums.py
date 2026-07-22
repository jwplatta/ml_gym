import random

from source.fast_math.models import GeneratedQuestion, GradingSpec


def sum_odd_nums_up_to_n(rng: random.Random) -> GeneratedQuestion:
    limit = rng.choice([20, 30, 40, 50, 60, 70, 80, 90])
    count = (limit + 1) // 2
    answer = count * count
    return GeneratedQuestion(
        question_type="sum_odd_nums_up_to_n",
        topic="consecutive-sums",
        effort="low",
        subtopic="consecutive-sums",
        prompt=f"What is the sum of all odd numbers from 1 up to {limit}?",
        answer=str(answer),
        answer_display=str(answer),
        hint="The sum of the first n odd numbers is n^2.",
        grading=GradingSpec.numeric(),
        metadata={"limit": limit},
    )


def sum_of_nums_from_x_to_y(rng: random.Random) -> GeneratedQuestion:
    start = rng.randint(10, 60)
    stop = rng.randint(start + 15, start + 90)
    count = stop - start + 1
    answer = count * (start + stop) // 2
    return GeneratedQuestion(
        question_type="sum_of_nums_from_x_to_y",
        topic="consecutive-sums",
        effort="medium",
        subtopic="consecutive-sums",
        prompt=f"What is the sum of all integers from {start} to {stop} inclusive?",
        answer=str(answer),
        answer_display=str(answer),
        hint="Use arithmetic series: count x (first + last) / 2.",
        grading=GradingSpec.numeric(),
        metadata={"start": start, "stop": stop},
    )


GENERATORS = [
    sum_odd_nums_up_to_n,

]
