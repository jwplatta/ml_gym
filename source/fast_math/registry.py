from __future__ import annotations

import random
from collections import defaultdict
from collections.abc import Callable

from source.fast_math.models import GeneratedQuestion
from source.fast_math.questions import ALL_GENERATORS

QuestionGenerator = Callable[[random.Random], GeneratedQuestion]


def get_question_generators() -> list[QuestionGenerator]:
    return list(ALL_GENERATORS)


def get_topics() -> list[str]:
    topics = {generator(random.Random(0)).topic for generator in ALL_GENERATORS}
    return sorted(topics)


def generators_by_topic() -> dict[str, list[QuestionGenerator]]:
    grouped: dict[str, list[QuestionGenerator]] = defaultdict(list)
    for generator in ALL_GENERATORS:
        grouped[generator(random.Random(0)).topic].append(generator)
    return dict(grouped)
