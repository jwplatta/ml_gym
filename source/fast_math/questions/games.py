import random
from fractions import Fraction

from source.fast_math.models import GeneratedQuestion, GradingSpec


def proportional_allocation_game(rng: random.Random) -> GeneratedQuestion:
    prize = rng.choice([60, 80, 100, 120, 150, 200])
    # Nash equilibrium: each player bids prize/3
    answer = Fraction(prize, 3)
    answer_str = str(answer)

    return GeneratedQuestion(
        question_type="proportional_allocation_game",
        topic="games",
        subtopic="nash-equilibrium",
        prompt=(
            f"Two players each allocate any real number of points between 0 and {prize} into a machine. "
            f"The machine selects a player with probability proportional to their allocation. "
            f"The selected player wins {prize} minus the points they allocated. "
            "Both players play optimally. How many points should each player allocate? "
            "Give a simplified fraction."
        ),
        answer=answer_str,
        answer_display=answer_str,
        hint=(
            f"Your expected payoff is x/(x+y) * ({prize}-x). "
            "At Nash equilibrium both players play the same strategy (by symmetry), so set x=y. "
            f"Take the derivative with respect to x, set to 0, and solve: you get x = {prize}/3."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "prize": prize,
            "equilibrium": answer_str,
        },
    )


GENERATORS = [
    proportional_allocation_game,
]
