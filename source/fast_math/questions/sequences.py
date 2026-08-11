import random
from fractions import Fraction

from source.fast_math.models import GeneratedQuestion, GradingSpec


# ── Constants ──────────────────────────────────────────────────────────────────

_FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
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
    d = rng.choice([x for x in range(-10, 11) if abs(x) > 1])
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
        hint="Difference sequence.",
        grading=GradingSpec.numeric(),
        metadata={"start": start, "d": d},
    )


def seq_geometric(rng: random.Random) -> GeneratedQuestion:
    """Constant ratio (geometric) sequence."""
    start = rng.randint(1, 3)
    ratio = rng.choice([r for r in range(-20, 21) if abs(r) >= 2])
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
        hint="Ratio sequence.",
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
        hint="Difference sequence.",
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
        hint="Difference sequence.",
        grading=GradingSpec.numeric(),
        metadata={"start": start, "first_diff": first_diff, "ratio": ratio},
    )


def seq_ratio_alternating(rng: random.Random) -> GeneratedQuestion:
    """Consecutive ratios alternate between two values."""
    start = rng.randint(1, 3)
    r1 = rng.randint(2, 20)
    r2 = rng.choice([x for x in range(2, 21) if x != r1])
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
        hint="Ratio sequence.",
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
        hint="Double sequence.",
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
        hint="Double sequence.",
        grading=GradingSpec.fraction(),
        metadata={"num0": num0, "den0": den0, "diff_num": diff_num, "diff_den": diff_den},
    )


def seq_triplet(rng: random.Random) -> GeneratedQuestion:
    """Three interleaved arithmetic sequences, one at each residue mod 3.

    Shows 12 terms (4 per sub-sequence); asks for the 13th.
    """
    diff_pool = [x for x in range(-20, 21) if abs(x) >= 3]
    starts = [rng.randint(-30, 80) for _ in range(3)]
    diffs = rng.sample(diff_pool, 3)  # all three diffs are distinct

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
        hint="Triplet sequence.",
        grading=GradingSpec.numeric(),
        metadata={"starts": starts, "diffs": diffs},
    )


def _build_grouped_seq(rng, n_groups_complete, first_start, group_start_diff,
                        first_within_d, delta):
    seq = []
    for g in range(n_groups_complete + 1):
        g_start = first_start + g * group_start_diff
        g_d = first_within_d + g * delta
        if g < n_groups_complete:
            seq.extend(g_start + j * g_d for j in range(3))
        else:
            seq.append(g_start)
    last_start = first_start + n_groups_complete * group_start_diff
    last_d = first_within_d + n_groups_complete * delta
    answer = last_start + last_d
    return seq, answer


def seq_grouped(rng: random.Random) -> GeneratedQuestion:
    """Medium effort: groups of 3 with modest parameter ranges.

    Shows 3 complete groups plus the first element of a 4th; asks for the 2nd.
    """
    first_start = rng.randint(10, 60)
    group_start_diff = rng.choice([-6, -5, -4, -3, 3, 4, 5, 6])
    first_within_d = rng.choice([-8, -7, -6, -5, -4, 4, 5, 6, 7, 8])
    delta = rng.choice([-1, 1])
    seq, answer = _build_grouped_seq(rng, 3, first_start, group_start_diff,
                                     first_within_d, delta)
    return GeneratedQuestion(
        question_type="seq_grouped",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Grouped sequence.",
        grading=GradingSpec.numeric(),
        metadata={"first_start": first_start, "group_start_diff": group_start_diff,
                  "first_within_d": first_within_d, "delta": delta},
    )


def seq_grouped_hard(rng: random.Random) -> GeneratedQuestion:
    """Hard effort: groups of 3 with larger numbers and a wider range of patterns.

    Shows 4–5 complete groups plus the first element of the next; asks for the 2nd.
    """
    n_groups_complete = rng.choice([4, 5])
    first_start = rng.randint(20, 120)
    group_start_diff = rng.choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])
    first_within_d = rng.choice([-15, -12, -10, -9, -8, 8, 9, 10, 12, 15])
    delta = rng.choice([-2, -1, 1, 2])
    seq, answer = _build_grouped_seq(rng, n_groups_complete, first_start,
                                     group_start_diff, first_within_d, delta)
    return GeneratedQuestion(
        question_type="seq_grouped_hard",
        topic="sequences",
        effort="high",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Grouped sequence.",
        grading=GradingSpec.numeric(),
        metadata={"first_start": first_start, "group_start_diff": group_start_diff,
                  "first_within_d": first_within_d, "delta": delta},
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
        hint="Linear sequence.",
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
        hint="Linear sequence.",
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
        hint="Cumulative product sequence.",
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
        hint="Latent Fibonacci sequence.",
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
        hint="Latent prime sequence.",
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
        hint="Latent power sequence.",
        grading=GradingSpec.numeric(),
        metadata={"base": base, "start_exp": start_exp, "start_val": start_val},
    )


def seq_latent_alphabetic(rng: random.Random) -> GeneratedQuestion:
    """Letter sequence: either first letters of an ordered set (planets, days, months)
    or an every-nth-letter pattern in the alphabet."""
    strategy = rng.choice(["ordered_list", "every_nth"])

    if strategy == "ordered_list":
        source, hint_text = rng.choice([
            (_PLANETS, "Alphabetic sequence."),
            (_DAYS, "Alphabetic sequence."),
            (_MONTHS, "Alphabetic sequence."),
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
        hint_text = "Alphabetic sequence."

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


def seq_cumulative_product_3(rng: random.Random) -> GeneratedQuestion:
    """Each term is the product of the three terms before it."""
    seeds = [-2, -1, 1, 2]
    a0 = rng.choice(seeds)
    a1 = rng.choice(seeds)
    # Ensure at least one seed is ±1 to prevent runaway growth
    if abs(a0) > 1 and abs(a1) > 1:
        a2 = rng.choice([-1, 1])
    else:
        a2 = rng.choice(seeds)
    length = 6
    seq = [a0, a1, a2]
    for _ in range(length - 3):
        seq.append(seq[-1] * seq[-2] * seq[-3])
    answer = seq[-1] * seq[-2] * seq[-3]
    return GeneratedQuestion(
        question_type="seq_cumulative_product_3",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Cumulative product sequence.",
        grading=GradingSpec.numeric(),
        metadata={"a0": a0, "a1": a1, "a2": a2},
    )


def seq_diff_prime(rng: random.Random) -> GeneratedQuestion:
    """Differences between consecutive terms are consecutive prime numbers."""
    direction = rng.choice([1, -1])
    start_prime_idx = rng.randint(0, 6)
    n_diffs = rng.choice([5, 6])
    start_val = rng.randint(-10, 30)
    seq = [start_val]
    for i in range(n_diffs):
        seq.append(seq[-1] + direction * _PRIMES[start_prime_idx + i])
    answer = seq[-1] + direction * _PRIMES[start_prime_idx + n_diffs]
    return GeneratedQuestion(
        question_type="seq_diff_prime",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Latent prime sequence.",
        grading=GradingSpec.numeric(),
        metadata={"direction": direction, "start_prime_idx": start_prime_idx, "start_val": start_val},
    )


def seq_linear_recurrence(rng: random.Random) -> GeneratedQuestion:
    """Each term: a[n] = r * a[n-1] + a[n-2]."""
    r = rng.choice([-3, -2, 2, 3])
    a0 = rng.randint(1, 5)
    a1 = rng.randint(1, 5)
    length = 6
    seq = [a0, a1]
    for _ in range(length - 2):
        seq.append(r * seq[-1] + seq[-2])
    answer = r * seq[-1] + seq[-2]
    return GeneratedQuestion(
        question_type="seq_linear_recurrence",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Linear sequence.",
        grading=GradingSpec.numeric(),
        metadata={"r": r, "a0": a0, "a1": a1},
    )


def seq_latent_prime_alternating(rng: random.Random) -> GeneratedQuestion:
    """Every 2nd or 3rd prime in the prime sequence."""
    step = rng.choice([2, 3])
    length = 5
    max_start = len(_PRIMES) - 1 - length * step
    start_idx = rng.randint(0, max_start)
    seq = [_PRIMES[start_idx + j * step] for j in range(length)]
    answer = _PRIMES[start_idx + length * step]
    return GeneratedQuestion(
        question_type="seq_latent_prime_alternating",
        topic="sequences",
        effort="low",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Latent prime sequence.",
        grading=GradingSpec.numeric(),
        metadata={"step": step, "start_idx": start_idx},
    )


def seq_cumulative_alt_ops(rng: random.Random) -> GeneratedQuestion:
    """Alternating ×/÷: even steps multiply prior two terms, odd steps divide earlier by later."""
    a0 = Fraction(rng.choice([2, 3, 4, 5, 6]))
    a1 = Fraction(rng.choice([2, 3, 5, 7]))
    while a1 == a0:
        a1 = Fraction(rng.choice([2, 3, 5, 7]))
    length = 6
    seq = [a0, a1]
    for i in range(length - 2):
        if i % 2 == 0:
            seq.append(seq[-1] * seq[-2])   # multiply
        else:
            seq.append(seq[-2] / seq[-1])   # divide earlier by later → produces fractions

    n = length - 2
    if n % 2 == 0:
        ans_frac = seq[-1] * seq[-2]
    else:
        ans_frac = seq[-2] / seq[-1]

    def fmt(f: Fraction) -> str:
        return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"

    seq_strs = [fmt(x) for x in seq]
    answer = fmt(ans_frac)
    return GeneratedQuestion(
        question_type="seq_cumulative_alt_ops",
        topic="sequences",
        effort="medium",
        prompt=", ".join(seq_strs) + ", ___",
        answer=answer,
        answer_display=answer,
        hint="Cumulative product sequence.",
        grading=GradingSpec.fraction(),
        metadata={"a0": str(a0), "a1": str(a1)},
    )


def seq_cyclic_ops(rng: random.Random) -> GeneratedQuestion:
    """Cyclic 3-op pattern: +c, ×r, ÷k repeating.

    r = k*d ensures the ÷k step always divides exactly.
    Shows 6 terms (2 full cycles), asks for the 7th.
    """
    k = rng.choice([2, 3, 4])
    d = rng.choice([2, 3, 4])
    r = k * d
    c = rng.randint(3, 15)
    start = rng.randint(5, 50)

    seq = [start]
    for i in range(6):
        op = i % 3
        if op == 0:
            seq.append(seq[-1] + c)
        elif op == 1:
            seq.append(seq[-1] * r)
        else:
            seq.append(seq[-1] // k)

    shown = seq[:6]
    answer = seq[6]
    return GeneratedQuestion(
        question_type="seq_cyclic_ops",
        topic="sequences",
        effort="high",
        prompt=_seq_prompt(shown),
        answer=str(answer),
        answer_display=str(answer),
        hint="Cyclic sequence.",
        grading=GradingSpec.numeric(),
        metadata={"c": c, "r": r, "k": k, "start": start},
    )


def seq_diff_fibonacci(rng: random.Random) -> GeneratedQuestion:
    """Differences between consecutive terms follow a Fibonacci-like pattern."""
    d0 = rng.randint(1, 5)
    d1 = rng.randint(1, 5)
    start_val = rng.randint(1, 20)
    n_terms = 6
    diffs = [d0, d1]
    for _ in range(n_terms - 1):
        diffs.append(diffs[-1] + diffs[-2])
    seq = [start_val]
    for d in diffs[:n_terms - 1]:
        seq.append(seq[-1] + d)
    answer = seq[-1] + diffs[n_terms - 1]
    return GeneratedQuestion(
        question_type="seq_diff_fibonacci",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Difference sequence.",
        grading=GradingSpec.numeric(),
        metadata={"d0": d0, "d1": d1, "start_val": start_val},
    )


def seq_diff_two_powers(rng: random.Random) -> GeneratedQuestion:
    """Differences are sums of two independent power sequences: b1^i + b2^i."""
    bases_pool = [2, 3, 4]
    b1 = rng.choice(bases_pool)
    b2 = rng.choice([b for b in bases_pool if b != b1])
    start_exp = rng.choice([0, 1])
    start_val = rng.randint(1, 20)
    n_diffs = rng.choice([4, 5])
    seq = [start_val]
    for i in range(n_diffs):
        seq.append(seq[-1] + b1 ** (start_exp + i) + b2 ** (start_exp + i))
    answer = seq[-1] + b1 ** (start_exp + n_diffs) + b2 ** (start_exp + n_diffs)
    return GeneratedQuestion(
        question_type="seq_diff_two_powers",
        topic="sequences",
        effort="high",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Latent power sequence.",
        grading=GradingSpec.numeric(),
        metadata={"b1": b1, "b2": b2, "start_exp": start_exp, "start_val": start_val},
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
    seq_grouped_hard,
    seq_linear_diff_prior2,
    seq_linear_mult_plus_c,
    seq_cumulative_product,
    seq_latent_fibonacci,
    seq_latent_prime_squared,
    seq_latent_power_in_diffs,
    seq_latent_alphabetic,
    seq_cumulative_product_3,
    seq_diff_prime,
    seq_linear_recurrence,
    seq_latent_prime_alternating,
    seq_cumulative_alt_ops,
    seq_cyclic_ops,
    seq_diff_fibonacci,
    seq_diff_two_powers,
]
