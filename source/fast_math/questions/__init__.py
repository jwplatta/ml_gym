from source.fast_math.questions.consecutive_sums import GENERATORS as CONSECUTIVE_SUMS_GENERATORS
from source.fast_math.questions.multiplication import GENERATORS as MULTIPLICATION_GENERATORS
from source.fast_math.questions.probability import GENERATORS as PROBABILITY_GENERATORS
from source.fast_math.questions.squaring import GENERATORS as SQUARING_GENERATORS

ALL_GENERATORS = (
    *MULTIPLICATION_GENERATORS,
    *PROBABILITY_GENERATORS,
    *SQUARING_GENERATORS,
    *CONSECUTIVE_SUMS_GENERATORS
)

__all__ = [
    "ALL_GENERATORS",
    "MULTIPLICATION_GENERATORS",
    "PROBABILITY_GENERATORS",
    "SQUARING_GENERATORS",
    "CONSECUTIVE_SUMS_GENERATORS"
]
