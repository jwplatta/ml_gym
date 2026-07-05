import math
import random
from fractions import Fraction

from source.fast_math.models import GeneratedQuestion, GradingSpec


def even_or_prime_die_roll(rng: random.Random) -> GeneratedQuestion:
    answer = Fraction(4, 6)
    return GeneratedQuestion(
        question_type="even_or_prime_die_roll",
        topic="probability",
        prompt="What is the probability of rolling a fair six-sided die and getting an even number or a prime number? Give your answer as a simplified fraction.",
        answer="2/3",
        answer_display="2/3",
        hint="Use the union rule: P(A or B) = P(A) + P(B) - P(A and B).",
        grading=GradingSpec.fraction(),
        metadata={"sample_space": 6, "favorable_outcomes": [2, 3, 4, 6], "fraction": str(answer)},
    )


def equal_heads_three_flips(rng: random.Random) -> GeneratedQuestion:
    favorable = sum(math.comb(3, k) ** 2 for k in range(4))
    total = 8 * 8
    result = Fraction(favorable, total)
    return GeneratedQuestion(
        question_type="equal_heads_three_flips",
        topic="probability",
        prompt="You and your opponent each flip a fair coin 3 times. What is the probability that you get the same number of heads? Give a simplified fraction.",
        answer=f"{result.numerator}/{result.denominator}",
        answer_display=f"{result.numerator}/{result.denominator}",
        hint="Condition on the number of heads you get, then match the opponent.",
        grading=GradingSpec.fraction(),
        metadata={"favorable": favorable, "total": total},
    )


def torpedoes_destroy_ship(rng: random.Random) -> GeneratedQuestion:
    hit_probability = Fraction(1, 3)
    torpedoes = rng.choice([2, 3, 4])
    destroyed = 1 - (1 - hit_probability) ** torpedoes
    answer = f"{destroyed.numerator}/{destroyed.denominator}"
    return GeneratedQuestion(
        question_type="torpedoes_destroy_ship",
        topic="probability",
        prompt=f"A torpedo hits with probability 1/3 and destroys the ship if it hits. {torpedoes} torpedoes are fired independently. What is the probability the ship is destroyed? Give a simplified fraction.",
        answer=answer,
        answer_display=answer,
        hint="Compute the complement: ship survives only if every torpedo misses.",
        grading=GradingSpec.fraction(),
        metadata={"hit_probability": "1/3", "torpedoes": torpedoes},
    )


GENERATORS = [
    even_or_prime_die_roll,
    equal_heads_three_flips,
    torpedoes_destroy_ship,
]
