from source.fast_math.questions.addition_subtraction import GENERATORS as ADDITION_SUBTRACTION_GENERATORS
from source.fast_math.questions.consecutive_sums import GENERATORS as CONSECUTIVE_SUMS_GENERATORS
from source.fast_math.questions.counting import GENERATORS as COUNTING_GENERATORS
from source.fast_math.questions.division import GENERATORS as DIVISION_GENERATORS
from source.fast_math.questions.games import GENERATORS as GAMES_GENERATORS
from source.fast_math.questions.multiplication import GENERATORS as MULTIPLICATION_GENERATORS
from source.fast_math.questions.probability import GENERATORS as PROBABILITY_GENERATORS
from source.fast_math.questions.squaring import GENERATORS as SQUARING_GENERATORS

ALL_GENERATORS = (
    *ADDITION_SUBTRACTION_GENERATORS,
    *COUNTING_GENERATORS,
    *DIVISION_GENERATORS,
    *GAMES_GENERATORS,
    *MULTIPLICATION_GENERATORS,
    *PROBABILITY_GENERATORS,
    *SQUARING_GENERATORS,
    *CONSECUTIVE_SUMS_GENERATORS
)

__all__ = [
    "ALL_GENERATORS",
    "ADDITION_SUBTRACTION_GENERATORS",
    "COUNTING_GENERATORS",
    "DIVISION_GENERATORS",
    "GAMES_GENERATORS",
    "MULTIPLICATION_GENERATORS",
    "PROBABILITY_GENERATORS",
    "SQUARING_GENERATORS",
    "CONSECUTIVE_SUMS_GENERATORS"
]
