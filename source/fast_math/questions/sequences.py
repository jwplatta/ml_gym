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


def _fmt_frac_latex(n: int, d: int) -> str:
    """Format n/d as an inline LaTeX fraction; plain integer when d == 1."""
    if d == 1:
        return str(n)
    return f"$\\frac{{{n}}}{{{d}}}$"


def _fmt_frac_plain(f: Fraction) -> str:
    """Format a Fraction as plain n/d — used for the answer field that the grader parses."""
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


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


def _build_second_order_seq(rng, d2_choices):
    a0 = rng.randint(-10, 30)
    d0 = rng.choice([x for x in range(-6, 7) if x != 0])
    d2 = rng.choice(d2_choices)
    length = 5
    seq = [a0]
    current_diff = d0
    for _ in range(length - 1):
        seq.append(seq[-1] + current_diff)
        current_diff += d2
    answer = seq[-1] + current_diff
    return seq, answer, {"a0": a0, "d0": d0, "d2": d2}


def seq_diff_second_order(rng: random.Random) -> GeneratedQuestion:
    """Second differences are constant (d2=±1), easy to spot."""
    seq, answer, meta = _build_second_order_seq(rng, [-1, 1])
    return GeneratedQuestion(
        question_type="seq_diff_second_order",
        topic="sequences",
        effort="low",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Difference sequence.",
        grading=GradingSpec.numeric(),
        metadata=meta,
    )


def seq_diff_second_order_medium(rng: random.Random) -> GeneratedQuestion:
    """Second differences are constant (d2=±2 or ±3), harder to spot."""
    seq, answer, meta = _build_second_order_seq(rng, [-3, -2, 2, 3])
    return GeneratedQuestion(
        question_type="seq_diff_second_order_medium",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Difference sequence.",
        grading=GradingSpec.numeric(),
        metadata=meta,
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


def _gen_double_subseq(rng, length, allow_geometric):
    """Generate terms and next-term for one interleaved sub-sequence.

    Returns (terms, next_term, kind, params).
    """
    if allow_geometric and rng.random() < 0.5:
        start = rng.randint(1, 4)
        r = rng.choice([2, 3])
        terms = [start * r ** i for i in range(length)]
        return terms, start * r ** length, "geometric", {"start": start, "r": r}
    else:
        start = rng.randint(1, 15)
        d = rng.choice([x for x in range(-8, 9) if abs(x) >= 2])
        terms = [start + i * d for i in range(length)]
        return terms, start + length * d, "arithmetic", {"start": start, "d": d}


def seq_double_even_odd(rng: random.Random) -> GeneratedQuestion:
    """Two interleaved arithmetic sequences. Show 6 terms; ask for the 7th."""
    n_per = 3  # terms per sub-sequence shown
    odd_terms, odd_next, _, odd_params = _gen_double_subseq(rng, n_per, allow_geometric=False)
    even_terms, _, _, even_params = _gen_double_subseq(rng, n_per, allow_geometric=False)

    seq = [val for pair in zip(odd_terms, even_terms) for val in pair]
    return GeneratedQuestion(
        question_type="seq_double_even_odd",
        topic="sequences",
        effort="low",
        prompt=_seq_prompt(seq),
        answer=str(odd_next),
        answer_display=str(odd_next),
        hint="Double sequence.",
        grading=GradingSpec.numeric(),
        metadata={"odd": odd_params, "even": even_params},
    )


def seq_double_even_odd_medium(rng: random.Random) -> GeneratedQuestion:
    """Two interleaved sequences, at least one geometric. Show 6 terms; ask for the 7th."""
    n_per = 3
    # Generate both; force a retry until at least one is geometric
    while True:
        odd_terms, odd_next, odd_kind, odd_params = _gen_double_subseq(rng, n_per, allow_geometric=True)
        even_terms, _, even_kind, even_params = _gen_double_subseq(rng, n_per, allow_geometric=True)
        if odd_kind == "geometric" or even_kind == "geometric":
            break

    seq = [val for pair in zip(odd_terms, even_terms) for val in pair]
    return GeneratedQuestion(
        question_type="seq_double_even_odd_medium",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(odd_next),
        answer_display=str(odd_next),
        hint="Double sequence.",
        grading=GradingSpec.numeric(),
        metadata={"odd": odd_params, "even": even_params},
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

    seq_strs = [_fmt_frac_latex(num0 + i * diff_num, den0 + i * diff_den) for i in range(length)]
    n_ans = num0 + length * diff_num
    d_ans = den0 + length * diff_den
    frac = Fraction(n_ans, d_ans)
    answer = _fmt_frac_plain(frac)

    return GeneratedQuestion(
        question_type="seq_double_fractional",
        topic="sequences",
        effort="medium",
        prompt=", ".join(seq_strs) + ", ___",
        answer=answer,
        answer_display=_fmt_frac_latex(frac.numerator, frac.denominator),
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
    """Low effort: groups of 3, delta=±1 so within-group diff changes slowly.

    Shows 3 complete groups plus the first element of a 4th; asks for the 2nd.
    """
    first_start = rng.randint(5, 80)
    group_start_diff = rng.randint(-12, 12)
    while group_start_diff == 0:
        group_start_diff = rng.randint(-12, 12)
    first_within_d = rng.randint(-12, 12)
    while abs(first_within_d) < 2:
        first_within_d = rng.randint(-12, 12)
    delta = rng.choice([-1, 1])
    seq, answer = _build_grouped_seq(rng, 3, first_start, group_start_diff,
                                     first_within_d, delta)
    return GeneratedQuestion(
        question_type="seq_grouped",
        topic="sequences",
        effort="low",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Grouped sequence.",
        grading=GradingSpec.numeric(),
        metadata={"first_start": first_start, "group_start_diff": group_start_diff,
                  "first_within_d": first_within_d, "delta": delta},
    )


def seq_grouped_medium(rng: random.Random) -> GeneratedQuestion:
    """Medium effort: groups of 3–4, delta=±2..±4 so within-group diff jumps less obviously.

    Shows 3–4 complete groups plus the first element of the next; asks for the 2nd.
    """
    n_groups_complete = rng.choice([3, 4])
    first_start = rng.randint(5, 100)
    group_start_diff = rng.randint(-15, 15)
    while abs(group_start_diff) < 3:
        group_start_diff = rng.randint(-15, 15)
    first_within_d = rng.randint(-15, 15)
    while abs(first_within_d) < 3:
        first_within_d = rng.randint(-15, 15)
    delta = rng.choice([-4, -3, -2, 2, 3, 4])
    seq, answer = _build_grouped_seq(rng, n_groups_complete, first_start,
                                     group_start_diff, first_within_d, delta)
    return GeneratedQuestion(
        question_type="seq_grouped_medium",
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
    """High effort: groups of 3, 4–5 complete groups, large numbers and larger delta.

    Shows 4–5 complete groups plus the first element of the next; asks for the 2nd.
    """
    n_groups_complete = rng.choice([4, 5])
    first_start = rng.randint(20, 150)
    group_start_diff = rng.randint(-20, 20)
    while abs(group_start_diff) < 5:
        group_start_diff = rng.randint(-20, 20)
    first_within_d = rng.randint(-20, 20)
    while abs(first_within_d) < 5:
        first_within_d = rng.randint(-20, 20)
    delta = rng.choice([-5, -4, -3, 3, 4, 5])
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
    """Differences between consecutive terms are powers of a single base (2 or 3)."""
    b = rng.choice([2, 3])
    start_exp = rng.choice([0, 1])
    start_val = rng.randint(1, 20)
    n_diffs = rng.choice([4, 5])
    seq = [start_val]
    for i in range(n_diffs):
        seq.append(seq[-1] + b ** (start_exp + i))
    answer = seq[-1] + b ** (start_exp + n_diffs)
    return GeneratedQuestion(
        question_type="seq_latent_power_in_diffs",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Latent power sequence.",
        grading=GradingSpec.numeric(),
        metadata={"b": b, "start_exp": start_exp, "start_val": start_val},
    )


def seq_latent_two_powers_in_diffs(rng: random.Random) -> GeneratedQuestion:
    """Differences between consecutive terms are sums of powers of two bases (2 and 3)."""
    start_exp = rng.choice([0, 1])
    start_val = rng.randint(1, 20)
    n_diffs = rng.choice([4, 5])
    seq = [start_val]
    for i in range(n_diffs):
        seq.append(seq[-1] + 2 ** (start_exp + i) + 3 ** (start_exp + i))
    answer = seq[-1] + 2 ** (start_exp + n_diffs) + 3 ** (start_exp + n_diffs)
    return GeneratedQuestion(
        question_type="seq_latent_two_powers_in_diffs",
        topic="sequences",
        effort="high",
        prompt=_seq_prompt(seq),
        answer=str(answer),
        answer_display=str(answer),
        hint="Latent power sequence.",
        grading=GradingSpec.numeric(),
        metadata={"start_exp": start_exp, "start_val": start_val},
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
    while True:
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
        # Reject trivial sequences where every shown term is identical
        if len(set(seq)) > 1:
            break
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

    seq_strs = [_fmt_frac_latex(x.numerator, x.denominator) for x in seq]
    answer = _fmt_frac_plain(ans_frac)
    return GeneratedQuestion(
        question_type="seq_cumulative_alt_ops",
        topic="sequences",
        effort="medium",
        prompt=", ".join(seq_strs) + ", ___",
        answer=answer,
        answer_display=_fmt_frac_latex(ans_frac.numerator, ans_frac.denominator),
        hint="Cumulative product sequence.",
        grading=GradingSpec.fraction(),
        metadata={"a0": str(a0), "a1": str(a1)},
    )


def seq_cyclic_ops(rng: random.Random) -> GeneratedQuestion:
    """Cyclic 3-op pattern: +c, ×r, ÷k in a randomized order, repeating.

    start and c are multiples of k, r = k*d — this guarantees ÷k is always
    exact regardless of op order, since all operations preserve divisibility by k.
    Shows 6 terms (2 full cycles), asks for the 7th.
    """
    k = rng.choice([2, 3, 4])
    d = rng.choice([2, 3, 4])
    r = k * d
    c = k * rng.randint(1, 5)
    start = k * rng.randint(2, 20)

    ops = [("add", c), ("mul", r), ("div", k)]
    rng.shuffle(ops)

    def apply(val, op):
        name, arg = op
        if name == "add":
            return val + arg
        elif name == "mul":
            return val * arg
        else:
            return val // arg

    seq = [start]
    for i in range(6):
        seq.append(apply(seq[-1], ops[i % 3]))

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
        metadata={"c": c, "r": r, "k": k, "start": start, "op_order": [o[0] for o in ops]},
    )


def seq_cyclic_ops_fractional(rng: random.Random) -> GeneratedQuestion:
    """Cyclic 3-op: +c and ×r (in either order) then ÷k, where ÷k yields a non-integer fraction.

    Unlike seq_cyclic_ops, divisibility is not enforced — the ÷k step deliberately
    produces fractions that persist through all subsequent operations.
    The sequence opens with 2 integer terms then turns fractional.
    Shows 5 terms (one full cycle + 2); asks for the 6th.
    """
    while True:
        k = rng.choice([3, 5, 7])
        r = rng.choice([x for x in range(2, 9) if x % k != 0])
        c = rng.randint(3, 10)
        start = rng.randint(2, 15)

        # ÷k always comes last; first two ops are +c and ×r in either order
        if rng.random() < 0.5:
            ops = [("add", c), ("mul", r), ("div", k)]
        else:
            ops = [("mul", r), ("add", c), ("div", k)]

        seq = [Fraction(start)]
        for i in range(5):
            name, arg = ops[i % 3]
            if name == "add":
                seq.append(seq[-1] + arg)
            elif name == "mul":
                seq.append(seq[-1] * arg)
            else:
                seq.append(seq[-1] / arg)

        answer_frac = seq[5]

        # Must have at least one non-integer in the 5 shown terms
        if all(x.denominator == 1 for x in seq[:5]):
            continue
        # Keep numbers manageable
        if abs(answer_frac.numerator) > 5000:
            continue

        break

    def fmt(f: Fraction) -> str:
        return str(f.numerator) if f.denominator == 1 else _fmt_frac_latex(f.numerator, f.denominator)

    return GeneratedQuestion(
        question_type="seq_cyclic_ops_fractional",
        topic="sequences",
        effort="high",
        prompt=", ".join(fmt(f) for f in seq[:5]) + ", ___",
        answer=_fmt_frac_plain(answer_frac),
        answer_display=_fmt_frac_latex(answer_frac.numerator, answer_frac.denominator),
        hint="Cyclic sequence.",
        grading=GradingSpec.fraction(),
        metadata={"c": c, "r": r, "k": k, "start": start, "op_order": [o[0] for o in ops]},
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


def seq_harmonic_diff(rng: random.Random) -> GeneratedQuestion:
    """Differences between consecutive terms are ±1/((n+1)*(n+2)), telescoping unit fractions."""
    direction = rng.choice([1, -1])
    start = rng.randint(2, 15)
    length = 6
    seq = [Fraction(start)]
    for n in range(1, length):
        seq.append(seq[-1] + direction * Fraction(1, (n + 1) * (n + 2)))
    answer_frac = seq[-1] + direction * Fraction(1, (length + 1) * (length + 2))

    return GeneratedQuestion(
        question_type="seq_harmonic_diff",
        topic="sequences",
        effort="medium",
        prompt=", ".join(_fmt_frac_latex(f.numerator, f.denominator) for f in seq) + ", ___",
        answer=_fmt_frac_plain(answer_frac),
        answer_display=_fmt_frac_latex(answer_frac.numerator, answer_frac.denominator),
        hint="Harmonic difference sequence.",
        grading=GradingSpec.fraction(),
        metadata={"start": start, "direction": direction},
    )


def seq_chained_fraction(rng: random.Random) -> GeneratedQuestion:
    """Chained fraction: each term's denominator becomes the next term's numerator.

    Denominators increase by base^((i+1)//2), so the step doubles every two terms.
    Shows 6 terms; asks for the 7th.

    Fractions are displayed WITHOUT simplification so the chain structure is visible
    (e.g. 6/4, 4/5, ... not 3/2, 4/5, ...). The answer is stored fully reduced.
    """
    base = rng.choice([2, 4])
    d0 = rng.randint(2, 8)
    n0 = d0 + rng.randint(1, 8)
    length = 6

    denoms = [d0]
    for i in range(length):
        denoms.append(denoms[-1] + base ** ((i + 1) // 2))

    # numers[0] = n0 (free start); numers[i] = denoms[i-1] for i >= 1 (chained)
    numers = [n0] + denoms[:length]

    # Display raw integers (no simplification) so the denominator→numerator chain is visible
    seq_strs = [_fmt_frac_latex(numers[i], denoms[i]) for i in range(length)]

    # Answer is fully reduced (grader normalises both sides via Fraction)
    ans_frac = Fraction(numers[length], denoms[length])
    answer = _fmt_frac_plain(ans_frac)

    return GeneratedQuestion(
        question_type="seq_chained_fraction",
        topic="sequences",
        effort="medium",
        prompt=", ".join(seq_strs) + ", ___",
        answer=answer,
        answer_display=_fmt_frac_latex(ans_frac.numerator, ans_frac.denominator),
        hint="Chained fraction sequence.",
        grading=GradingSpec.fraction(),
        metadata={"base": base, "d0": d0, "n0": n0},
    )


def seq_frac_cumulative_product(rng: random.Random) -> GeneratedQuestion:
    """Each term is the product of the two preceding terms, starting from reciprocal fractional seeds."""
    pool = [2, 3, 4, 5, 7]
    p = rng.choice(pool)
    q = rng.choice([x for x in pool if x != p])
    a0 = Fraction(p, q)
    a1 = Fraction(q, p)
    length = 6
    seq = [a0, a1]
    for _ in range(length - 2):
        seq.append(seq[-2] * seq[-1])
    answer_frac = seq[-2] * seq[-1]

    return GeneratedQuestion(
        question_type="seq_frac_cumulative_product",
        topic="sequences",
        effort="medium",
        prompt=", ".join(_fmt_frac_latex(f.numerator, f.denominator) for f in seq) + ", ___",
        answer=_fmt_frac_plain(answer_frac),
        answer_display=_fmt_frac_latex(answer_frac.numerator, answer_frac.denominator),
        hint="Cumulative product sequence.",
        grading=GradingSpec.fraction(),
        metadata={"p": p, "q": q},
    )


def seq_alternating_ops(rng: random.Random) -> GeneratedQuestion:
    """Alternating 2-op pattern: add c and multiply r in strict alternation."""
    r = rng.choice([2, 3, 4, 5])
    c = rng.choice([x for x in range(-10, 11) if abs(x) >= 3])
    start = rng.randint(1, 8)
    first_op = rng.choice(["add", "mul"])
    length = 6
    seq = [start]
    for i in range(length):
        if (i % 2 == 0) == (first_op == "add"):
            seq.append(seq[-1] + c)
        else:
            seq.append(seq[-1] * r)
    answer = seq[length]
    return GeneratedQuestion(
        question_type="seq_alternating_ops",
        topic="sequences",
        effort="low",
        prompt=_seq_prompt(seq[:length]),
        answer=str(answer),
        answer_display=str(answer),
        hint="Cyclic sequence.",
        grading=GradingSpec.numeric(),
        metadata={"r": r, "c": c, "start": start, "first_op": first_op},
    )


def seq_fib_over_squares(rng: random.Random) -> GeneratedQuestion:
    """Numerators follow Fibonacci; denominators are consecutive perfect squares.

    Fractions are displayed in reduced form, hiding the square denominators.
    Shows 6 terms; asks for the 7th.
    """
    # _FIBONACCI = [1,1,2,3,5,8,13,21,34,55,89] — need 7 consecutive values
    fib_start = rng.randint(2, 4)          # indices 2-4 → values 2,3,5
    den_start = rng.randint(2, 5)          # n² starting square: 4,9,16,25
    length = 6

    raw_fibs = [_FIBONACCI[fib_start + i] for i in range(length + 1)]
    fracs = [Fraction(raw_fibs[i], (den_start + i) ** 2) for i in range(length + 1)]

    seq_strs = [_fmt_frac_latex(f.numerator, f.denominator) for f in fracs[:length]]
    ans_frac = fracs[length]
    answer = _fmt_frac_plain(ans_frac)

    return GeneratedQuestion(
        question_type="seq_fib_over_squares",
        topic="sequences",
        effort="high",
        prompt=", ".join(seq_strs) + ", ___",
        answer=answer,
        answer_display=_fmt_frac_latex(ans_frac.numerator, ans_frac.denominator),
        hint="Latent Fibonacci sequence.",
        grading=GradingSpec.fraction(),
        metadata={"fib_start": fib_start, "den_start": den_start},
    )


def seq_alternating_frac_diff(rng: random.Random) -> GeneratedQuestion:
    """Differences alternate sign and grow: diff[j] = sign * (j+1)/(j+2).

    Concretely: -1/2, +2/3, -3/4, +4/5, -5/6, +6/7, …  (or the opposite sign).
    Shows 6 terms; asks for the 7th.
    """
    direction = rng.choice([1, -1])
    # Start as a simple integer so first few terms look approachable
    start_val = rng.randint(1, 10)
    length = 6
    seq = [Fraction(start_val)]
    for j in range(length):
        d = Fraction(direction * ((-1) ** j) * (j + 1), j + 2)
        seq.append(seq[-1] + d)

    ans_frac = seq[length]
    seq_strs = [_fmt_frac_latex(f.numerator, f.denominator) for f in seq[:length]]
    answer = _fmt_frac_plain(ans_frac)

    return GeneratedQuestion(
        question_type="seq_alternating_frac_diff",
        topic="sequences",
        effort="high",
        prompt=", ".join(seq_strs) + ", ___",
        answer=answer,
        answer_display=_fmt_frac_latex(ans_frac.numerator, ans_frac.denominator),
        hint="Harmonic difference sequence.",
        grading=GradingSpec.fraction(),
        metadata={"start_val": start_val, "direction": direction},
    )


def seq_alt_recurrence_2back(rng: random.Random) -> GeneratedQuestion:
    """Alternating recurrence: even-index terms use a[n-1]+a[n-2], odd-index use a[n-1]+a[n-3].

    Shows 6 terms; asks for the 7th (even-indexed, so uses the n-1+n-2 rule).
    """
    a0 = rng.randint(-5, 5)
    a1 = rng.randint(-5, 5)
    while a0 == 0 and a1 == 0:
        a1 = rng.randint(-5, 5)
    length = 7
    seq = [a0, a1]
    for n in range(2, length):
        if n % 2 == 0:
            seq.append(seq[-1] + seq[-2])
        else:
            seq.append(seq[-1] + seq[-3])

    # Reject if all shown terms are the same or sequence is boring
    shown = seq[:6]
    if len(set(shown)) <= 2:
        # Fallback: retry with different seeds
        a0, a1 = rng.randint(-5, 5), rng.randint(-5, 5)
        seq = [a0, a1]
        for n in range(2, length):
            if n % 2 == 0:
                seq.append(seq[-1] + seq[-2])
            else:
                seq.append(seq[-1] + seq[-3])

    answer = seq[6]
    return GeneratedQuestion(
        question_type="seq_alt_recurrence_2back",
        topic="sequences",
        effort="high",
        prompt=_seq_prompt(seq[:6]),
        answer=str(answer),
        answer_display=str(answer),
        hint="Linear sequence.",
        grading=GradingSpec.numeric(),
        metadata={"a0": a0, "a1": a1},
    )


def seq_cumulative_sum_3(rng: random.Random) -> GeneratedQuestion:
    """Each term is the sum of the three preceding terms: a[n] = a[n-1] + a[n-2] + a[n-3].

    Seeds may include zero and small negatives to produce non-obvious sequences.
    Shows 6 terms; asks for the 7th.
    """
    seeds = list(range(-3, 4))   # -3..3
    while True:
        a0 = rng.choice(seeds)
        a1 = rng.choice(seeds)
        a2 = rng.choice(seeds)
        length = 7
        seq = [a0, a1, a2]
        for _ in range(length - 3):
            seq.append(seq[-1] + seq[-2] + seq[-3])
        shown = seq[:6]
        # Reject trivial all-zero or all-same sequences
        if len(set(shown)) >= 3:
            break

    answer = seq[6]
    return GeneratedQuestion(
        question_type="seq_cumulative_sum_3",
        topic="sequences",
        effort="medium",
        prompt=_seq_prompt(shown),
        answer=str(answer),
        answer_display=str(answer),
        hint="Cumulative sum sequence.",
        grading=GradingSpec.numeric(),
        metadata={"a0": a0, "a1": a1, "a2": a2},
    )


GENERATORS = [
    seq_arithmetic,
    seq_geometric,
    seq_diff_second_order,
    seq_diff_second_order_medium,
    seq_diff_geometric,
    seq_ratio_alternating,
    seq_double_even_odd,
    seq_double_even_odd_medium,
    seq_double_fractional,
    seq_triplet,
    seq_grouped,
    seq_grouped_medium,
    seq_grouped_hard,
    seq_linear_diff_prior2,
    seq_linear_mult_plus_c,
    seq_cumulative_product,
    seq_latent_fibonacci,
    seq_latent_prime_squared,
    seq_latent_power_in_diffs,
    seq_latent_two_powers_in_diffs,
    seq_latent_alphabetic,
    seq_cumulative_product_3,
    seq_diff_prime,
    seq_linear_recurrence,
    seq_latent_prime_alternating,
    seq_cumulative_alt_ops,
    seq_cyclic_ops,
    seq_cyclic_ops_fractional,
    seq_diff_fibonacci,
    seq_harmonic_diff,
    seq_chained_fraction,
    seq_frac_cumulative_product,
    seq_alternating_ops,
    seq_fib_over_squares,
    seq_alternating_frac_diff,
    seq_alt_recurrence_2back,
    seq_cumulative_sum_3,
]
