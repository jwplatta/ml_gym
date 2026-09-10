import random
from fractions import Fraction
from math import gcd

from source.fast_math.models import GeneratedQuestion, GradingSpec

_DENOMS = [2, 3, 4, 5, 6, 8, 10, 12]


def _fmt(f: Fraction) -> str:
    if f.denominator == 1:
        return str(f.numerator)
    return f"{f.numerator}/{f.denominator}"


def _frac_distractors(rng: random.Random, correct: Fraction, n: int = 3) -> list:
    seen = {correct}
    candidates = []

    # Strategy 1: same denominator, nudge numerator by +-1 or +-2
    for delta in [-2, -1, 1, 2]:
        num = correct.numerator + delta
        if num > 0:
            f = Fraction(num, correct.denominator)
            if f not in seen:
                seen.add(f)
                candidates.append(f)

    # Strategy 2: same numerator, nudge denominator by +-1
    for delta in [-1, 1]:
        denom = correct.denominator + delta
        if denom >= 1:
            f = Fraction(correct.numerator, denom)
            if f not in seen:
                seen.add(f)
                candidates.append(f)

    # Strategy 3: nearby whole number
    for v in [int(correct), int(correct) + 1]:
        if v > 0:
            f = Fraction(v)
            if f not in seen:
                seen.add(f)
                candidates.append(f)

    # Strategy 4: double or half
    for f in [correct * 2, correct / 2]:
        if f.numerator > 0:
            if f not in seen:
                seen.add(f)
                candidates.append(f)

    rng.shuffle(candidates)
    result = candidates[:n]

    # Fallback: keep bumping numerator
    offset = 3
    while len(result) < n:
        num = correct.numerator + offset
        if num > 0:
            f = Fraction(num, correct.denominator)
            if f not in seen:
                seen.add(f)
                result.append(f)
        offset += 1

    return result


def _int_distractors(rng: random.Random, correct: int, n: int = 3) -> list:
    pool = [correct + delta for delta in range(-15, 16) if delta != 0]
    pool = [v for v in pool if v > 0]
    rng.shuffle(pool)
    result = pool[:n]

    # Fallback
    offset = 16
    while len(result) < n:
        v = correct + offset
        if v > 0 and v != correct and v not in result:
            result.append(v)
        offset += 1

    return result


def _choices(rng: random.Random, correct: Fraction, distractors: list) -> list:
    items = [_fmt(correct)] + [_fmt(d) for d in distractors]
    rng.shuffle(items)
    return items


def frac_of_int(rng: random.Random) -> GeneratedQuestion:
    d = 2
    a = 1
    N = 2
    answer = 1

    for _ in range(200):
        d = rng.choice(_DENOMS)
        a = rng.randint(1, d - 1)
        step = d // gcd(a, d)
        max_steps = 100 // step
        if max_steps < 1:
            continue
        k = rng.randint(1, max_steps)
        N = k * step
        result = a * N // d
        if result < 1 or result > 30:
            continue
        answer = result
        break

    correct = Fraction(answer)
    distractors = [Fraction(v) for v in _int_distractors(rng, answer)]
    choices = _choices(rng, correct, distractors)

    return GeneratedQuestion(
        question_type="frac_of_int",
        topic="fractions",
        subtopic="of",
        effort="low",
        prompt=f"{a}/{d} of {N} = ?",
        answer=_fmt(correct),
        answer_display=_fmt(correct),
        hint=f"Multiply {a} x {N}, then divide by {d}.",
        grading=GradingSpec.fraction(),
        metadata={
            "a": a,
            "d": d,
            "N": N,
            "choices": choices,
        },
    )


def frac_times_int(rng: random.Random) -> GeneratedQuestion:
    b = 2
    a = 1
    N = 1
    correct = Fraction(1)

    for _ in range(200):
        b = rng.choice(_DENOMS)
        a = rng.randint(1, b - 1)
        N = rng.randint(1, 100)
        result = Fraction(a * N, b)
        if result.numerator > 30 or result.denominator > 12:
            continue
        correct = result
        break

    distractors = _frac_distractors(rng, correct)
    choices = _choices(rng, correct, distractors)

    return GeneratedQuestion(
        question_type="frac_times_int",
        topic="fractions",
        subtopic="multiplication",
        effort="low",
        prompt=f"{a}/{b} x {N} = ?",
        answer=_fmt(correct),
        answer_display=_fmt(correct),
        hint=f"Multiply {a} x {N} to get the numerator, keep {b} as the denominator, then reduce.",
        grading=GradingSpec.fraction(),
        metadata={
            "a": a,
            "b": b,
            "N": N,
            "choices": choices,
        },
    )


def frac_add_frac(rng: random.Random) -> GeneratedQuestion:
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    correct = f1 + f2

    for _ in range(200):
        d1 = rng.choice(_DENOMS)
        d2 = rng.choice(_DENOMS)
        n1 = rng.randint(1, d1 - 1)
        n2 = rng.randint(1, d2 - 1)
        candidate1 = Fraction(n1, d1)
        candidate2 = Fraction(n2, d2)
        result = candidate1 + candidate2
        if result.denominator > 24 or result.numerator > 30:
            continue
        f1, f2, correct = candidate1, candidate2, result
        break

    distractors = _frac_distractors(rng, correct)
    choices = _choices(rng, correct, distractors)

    return GeneratedQuestion(
        question_type="frac_add_frac",
        topic="fractions",
        subtopic="addition",
        effort="medium",
        prompt=f"{f1.numerator}/{f1.denominator} + {f2.numerator}/{f2.denominator} = ?",
        answer=_fmt(correct),
        answer_display=_fmt(correct),
        hint="Find a common denominator, add the numerators, then reduce.",
        grading=GradingSpec.fraction(),
        metadata={
            "f1": str(f1),
            "f2": str(f2),
            "choices": choices,
        },
    )


def frac_sub_frac(rng: random.Random) -> GeneratedQuestion:
    f1 = Fraction(3, 4)
    f2 = Fraction(1, 3)
    correct = f1 - f2

    for _ in range(200):
        d1 = rng.choice(_DENOMS)
        d2 = rng.choice(_DENOMS)
        n1 = rng.randint(1, d1 - 1)
        n2 = rng.randint(1, d2 - 1)
        candidate1 = Fraction(n1, d1)
        candidate2 = Fraction(n2, d2)
        if candidate1 <= candidate2:
            continue
        result = candidate1 - candidate2
        if result.denominator > 24 or result.numerator > 30 or result.numerator < 1:
            continue
        f1, f2, correct = candidate1, candidate2, result
        break

    distractors = _frac_distractors(rng, correct)
    choices = _choices(rng, correct, distractors)

    return GeneratedQuestion(
        question_type="frac_sub_frac",
        topic="fractions",
        subtopic="subtraction",
        effort="medium",
        prompt=f"{f1.numerator}/{f1.denominator} - {f2.numerator}/{f2.denominator} = ?",
        answer=_fmt(correct),
        answer_display=_fmt(correct),
        hint="Find a common denominator, subtract the numerators, then reduce.",
        grading=GradingSpec.fraction(),
        metadata={
            "f1": str(f1),
            "f2": str(f2),
            "choices": choices,
        },
    )


GENERATORS = [frac_of_int, frac_times_int, frac_add_frac, frac_sub_frac]
