import random
from fractions import Fraction

from source.fast_math.models import GeneratedQuestion, GradingSpec


# ── Constants ──────────────────────────────────────────────────────────────────

_FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
_PLANETS = list("MVEMJSUN")
_DAYS = list("MTWTFSS")
_MONTHS = list("JFMAMJJASOND")
_ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def _seq_prompt(seq) -> str:
    return ", ".join(str(x) for x in seq) + ", ___"


# ── Raw Sequences ───────────────────────────────────────────────────────────────

def seq_arithmetic(rng: random.Random) -> GeneratedQuestion:
    """Constant difference (arithmetic) sequence."""
    start = rng.randint(-20, 50)
    d = rng.choice([x for x in range(-10, 11) if x != 0])
    length = rng.choice([5, 6])
    seq = [start + i * d for i in range(length)]
    answer = seq[-1] + d
    return GeneratedQuestion(
        question_type="seq_arithmetic",
        topic="sequences",
        effort="low",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Look at the differences between consecutive terms.",
        grading=GradingSpec.numeric(),
        metadata={"start": start, "d": d},
    )


def seq_geometric(rng: random.Random) -> GeneratedQuestion:
    """Constant ratio (geometric) sequence."""
    start = rng.randint(1, 5)
    ratio = rng.choice([2, 3, -2, -3])
    length = rng.choice([5, 6])
    seq = [start * (ratio ** i) for i in range(length)]
    answer = seq[-1] * ratio
    return GeneratedQuestion(
        question_type="seq_geometric",
        topic="sequences",
        effort="low",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Look at the ratios between consecutive terms.",
        grading=GradingSpec.numeric(),
        metadata={"start": start, "ratio": ratio},
    )


def seq_diff_second_order(rng: random.Random) -> GeneratedQuestion:
    """Second differences are constant (quadratic sequence)."""
    a0 = rng.randint(-10, 30)
    d0 = rng.choice([x for x in range(-6, 7) if x != 0])
    d2 = rng.choice([-3, -2, -1, 1, 2, 3])
    length = 5
    seq = [a0]
    current_diff = d0
    for _ in range(length - 1):
        seq.append(seq[-1] + current_diff)
        current_diff += d2
    answer = seq[-1] + current_diff
    return GeneratedQuestion(
        question_type="seq_diff_second_order",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Look at the differences between terms, then the differences of those.",
        grading=GradingSpec.numeric(),
        metadata={"a0": a0, "d0": d0, "d2": d2},
    )


def seq_diff_geometric(rng: random.Random) -> GeneratedQuestion:
    """Differences between terms form a geometric sequence."""
    start = rng.randint(0, 20)
    first_diff = rng.randint(1, 4)
    ratio = rng.choice([2, 3])
    length = 5
    seq = [start]
    d = first_diff
    for _ in range(length - 1):
        seq.append(seq[-1] + d)
        d *= ratio
    answer = seq[-1] + d
    return GeneratedQuestion(
        question_type="seq_diff_geometric",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Look at the differences — do they follow a ratio pattern?",
        grading=GradingSpec.numeric(),
        metadata={"start": start, "first_diff": first_diff, "ratio": ratio},
    )


def seq_ratio_alternating(rng: random.Random) -> GeneratedQuestion:
    """Consecutive ratios alternate between two values."""
    start = rng.randint(1, 5)
    r1 = rng.choice([2, 3])
    r2 = rng.choice([x for x in [2, 3] if x != r1])
    length = 6
    seq = [start]
    for i in range(length - 1):
        r = r1 if i % 2 == 0 else r2
        seq.append(seq[-1] * r)
    # Next multiplication step is (length-1), alternating from r1,r2,r1,...
    next_r = r1 if (length - 1) % 2 == 0 else r2
    answer = seq[-1] * next_r
    return GeneratedQuestion(
        question_type="seq_ratio_alternating",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Look at the ratios between consecutive terms — do they alternate?",
        grading=GradingSpec.numeric(),
        metadata={"start": start, "r1": r1, "r2": r2},
    )


def seq_double_even_odd(rng: random.Random) -> GeneratedQuestion:
    """Two interleaved arithmetic sequences at odd and even positions (1-indexed).

    Show 6 terms; ask for the 7th (next odd-indexed term).
    """
    nonzero = [x for x in range(-8, 9) if x != 0]
    start_odd = rng.randint(1, 15)
    diff_odd = rng.choice(nonzero)
    start_even = rng.randint(-5, 20)
    diff_even = rng.choice([x for x in nonzero if x != diff_odd])

    # i=0,2,4 → odd-indexed positions; i=1,3,5 → even-indexed positions
    seq = []
    for i in range(6):
        k = i // 2
        if i % 2 == 0:
            seq.append(start_odd + k * diff_odd)
        else:
            seq.append(start_even + k * diff_even)

    answer = start_odd + 3 * diff_odd  # 4th odd-indexed term
    return GeneratedQuestion(
        question_type="seq_double_even_odd",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Try reading every other term separately.",
        grading=GradingSpec.numeric(),
        metadata={"start_odd": start_odd, "diff_odd": diff_odd,
                  "start_even": start_even, "diff_even": diff_even},
    )


def seq_double_fractional(rng: random.Random) -> GeneratedQuestion:
    """Fraction sequence where numerator and denominator each follow arithmetic progressions.

    Fractions are shown in their 'pattern' form (not always simplified) so the
    pattern is visible; the canonical answer is the fully reduced fraction.
    """
    num0 = rng.choice([3, 5, 7, 9])
    den0 = rng.choice([4, 6, 8, 9, 10, 12])
    diff_num = rng.choice([1, 2])
    diff_den = rng.choice([2, 3])
    length = 4

    seq_strs = [f"{num0 + i * diff_num}/{den0 + i * diff_den}" for i in range(length)]
    n_ans = num0 + length * diff_num
    d_ans = den0 + length * diff_den
    frac = Fraction(n_ans, d_ans)
    answer = f"{frac.numerator}/{frac.denominator}"

    return GeneratedQuestion(
        question_type="seq_double_fractional",
        topic="sequences",
        effort="medium",
        prompt=", ".join(seq_strs) + ", ___",
        answer=answer,
        answer_display=answer,
        hint="Track numerators and denominators separately.",
        grading=GradingSpec.fraction(),
        metadata={"num0": num0, "den0": den0, "diff_num": diff_num, "diff_den": diff_den},
    )


def seq_triplet(rng: random.Random) -> GeneratedQuestion:
    """Three interleaved arithmetic sequences, one at each residue mod 3.

    Shows 12 terms (4 per sub-sequence); asks for the 13th.
    """
    nonzero = [x for x in range(-5, 6) if x != 0]
    starts = [rng.randint(-10, 20) for _ in range(3)]
    diffs = [rng.choice(nonzero) for _ in range(3)]

    n_complete = 4  # 4 terms per sub-sequence
    length = n_complete * 3
    seq = [starts[i % 3] + (i // 3) * diffs[i % 3] for i in range(length)]

    # 13th term: index 12, residue 0
    answer = starts[0] + n_complete * diffs[0]
    return GeneratedQuestion(
        question_type="seq_triplet",
        topic="sequences",
        effort="high",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Try reading every 3rd term: positions 1,4,7,... then 2,5,8,... then 3,6,9,...",
        grading=GradingSpec.numeric(),
        metadata={"starts": starts, "diffs": diffs},
    )


def seq_grouped(rng: random.Random) -> GeneratedQuestion:
    """Groups of 3 terms; within each group the step is constant, but that step
    changes by +1 between groups.  The first terms of each group also decrease
    by a fixed amount.

    Shows all complete groups plus the first element of the next group; asks for
    the second element of that final group.
    """
    n_groups_complete = rng.choice([3, 4])
    first_start = rng.randint(10, 40)
    group_start_diff = rng.choice([-3, -4, -5])
    first_within_d = rng.choice([-8, -7, -6, -5])
    delta = 1  # within-group step increases by 1 each group

    seq = []
    for g in range(n_groups_complete + 1):
        g_start = first_start + g * group_start_diff
        g_d = first_within_d + g * delta
        if g < n_groups_complete:
            seq.extend(g_start + j * g_d for j in range(3))
        else:
            seq.append(g_start)  # only show first element of final group

    last_start = first_start + n_groups_complete * group_start_diff
    last_d = first_within_d + n_groups_complete * delta
    answer = last_start + last_d
    return GeneratedQuestion(
        question_type="seq_grouped",
        topic="sequences",
        effort="high",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Find the groups of 3. What's the pattern of differences within and between groups?",
        grading=GradingSpec.numeric(),
        metadata={"first_start": first_start, "group_start_diff": group_start_diff,
                  "first_within_d": first_within_d},
    )


def seq_linear_diff_prior2(rng: random.Random) -> GeneratedQuestion:
    """Each term equals the difference of the two terms before it: a[n] = a[n-2] - a[n-1]."""
    a0 = rng.randint(5, 20)
    a1 = rng.randint(5, 20)
    length = 5
    seq = [a0, a1]
    for _ in range(length - 2):
        seq.append(seq[-2] - seq[-1])
    answer = seq[-2] - seq[-1]
    return GeneratedQuestion(
        question_type="seq_linear_diff_prior2",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Each term is the difference of the two before it.",
        grading=GradingSpec.numeric(),
        metadata={"a0": a0, "a1": a1},
    )


def seq_linear_mult_plus_c(rng: random.Random) -> GeneratedQuestion:
    """Each term equals the previous term multiplied by r, then add c: a[n] = a[n-1]*r + c."""
    start = rng.randint(1, 8)
    r = rng.choice([2, 3])
    c = rng.randint(1, 8)
    length = rng.choice([4, 5])
    seq = [start]
    for _ in range(length - 1):
        seq.append(seq[-1] * r + c)
    answer = seq[-1] * r + c
    return GeneratedQuestion(
        question_type="seq_linear_mult_plus_c",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Look for a pattern of the form: multiply by a constant, then add a constant.",
        grading=GradingSpec.numeric(),
        metadata={"start": start, "r": r, "c": c},
    )


def seq_cumulative_product(rng: random.Random) -> GeneratedQuestion:
    """Each term is the product of the two terms before it."""
    a0 = rng.choice([2, 3])
    a1 = rng.choice([2, 3])
    length = 5
    seq = [a0, a1]
    for _ in range(length - 2):
        seq.append(seq[-2] * seq[-1])
    answer = seq[-2] * seq[-1]
    return GeneratedQuestion(
        question_type="seq_cumulative_product",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Each term is the product of the two before it.",
        grading=GradingSpec.numeric(),
        metadata={"a0": a0, "a1": a1},
    )


# ── Latent Sequences ────────────────────────────────────────────────────────────

def seq_latent_fibonacci(rng: random.Random) -> GeneratedQuestion:
    """Fibonacci values at odd positions (1-indexed); geometric sequence at even positions.

    Shows 8 terms; asks for the 9th (next odd-indexed term = next Fibonacci value).
    """
    k = rng.randint(0, 3)           # Fibonacci start index
    r = rng.choice([2, 5, 10])      # even-position ratio
    start_e = rng.randint(2, 10)    # even-position starting value

    seq = []
    for i in range(8):
        if i % 2 == 0:
            seq.append(_FIBONACCI[k + i // 2])
        else:
            seq.append(start_e * (r ** (i // 2)))

    answer = _FIBONACCI[k + 4]
    return GeneratedQuestion(
        question_type="seq_latent_fibonacci",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Try reading the odd-position and even-position terms separately.",
        grading=GradingSpec.numeric(),
        metadata={"fib_start_idx": k, "even_start": start_e, "even_ratio": r},
    )


def seq_latent_prime_squared(rng: random.Random) -> GeneratedQuestion:
    """Each term is the square of a consecutive prime number."""
    i = rng.randint(0, 4)
    length = 5
    seq = [_PRIMES[i + j] ** 2 for j in range(length)]
    answer = _PRIMES[i + length] ** 2
    return GeneratedQuestion(
        question_type="seq_latent_prime_squared",
        topic="sequences",
        effort="low",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="These look like perfect squares — of what numbers?",
        grading=GradingSpec.numeric(),
        metadata={"start_prime_idx": i},
    )


def seq_latent_power_in_diffs(rng: random.Random) -> GeneratedQuestion:
    """Sequence where the differences between consecutive terms are powers of a base."""
    base = rng.choice([2, 3])
    start_exp = rng.choice([0, 1])
    start_val = rng.randint(1, 20)
    n_diffs = rng.choice([4, 5])

    seq = [start_val]
    for i in range(n_diffs):
        seq.append(seq[-1] + base ** (start_exp + i))

    answer = seq[-1] + base ** (start_exp + n_diffs)
    return GeneratedQuestion(
        question_type="seq_latent_power_in_diffs",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Look at the differences between consecutive terms.",
        grading=GradingSpec.numeric(),
        metadata={"base": base, "start_exp": start_exp, "start_val": start_val},
    )


def seq_latent_alphabetic(rng: random.Random) -> GeneratedQuestion:
    """Letter sequence: either first letters of an ordered set (planets, days, months)
    or an every-nth-letter pattern in the alphabet."""
    strategy = rng.choice(["ordered_list", "every_nth"])

    if strategy == "ordered_list":
        source, hint_text = rng.choice([
            (_PLANETS, "Think about what these letters could stand for."),
            (_DAYS, "Think about what these letters could stand for."),
            (_MONTHS, "Think about what these letters could stand for."),
        ])
        max_start = len(source) - 6
        start_idx = rng.randint(0, max(0, max_start))
        seq = source[start_idx:start_idx + 5]
        answer = source[start_idx + 5]
    else:
        k = rng.choice([1, 2])          # skip k letters between each shown letter
        step = k + 1
        max_start = 25 - 5 * step
        start_idx = rng.randint(0, max_start)
        seq = [_ALPHABET[start_idx + j * step] for j in range(5)]
        answer = _ALPHABET[start_idx + 5 * step]
        hint_text = "Look for a skip pattern in the alphabet."

    return GeneratedQuestion(
        question_type="seq_latent_alphabetic",
        topic="sequences",
        effort="low",
        prompt=", ".join(seq) + ", ___",
        answer=answer,
        answer_display=answer,
        hint=hint_text,
        grading=GradingSpec.text(),
        metadata={"strategy": strategy},
    )


GENERATORS = [
    seq_arithmetic,
    seq_geometric,
    seq_diff_second_order,
    seq_diff_geometric,
    seq_ratio_alternating,
    seq_double_even_odd,
    seq_double_fractional,
    seq_triplet,
    seq_grouped,
    seq_linear_diff_prior2,
    seq_linear_mult_plus_c,
    seq_cumulative_product,
    seq_latent_fibonacci,
    seq_latent_prime_squared,
    seq_latent_power_in_diffs,
    seq_latent_alphabetic,
]
