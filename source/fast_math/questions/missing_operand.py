import random

from source.fast_math.models import GeneratedQuestion, GradingSpec


# ── Helpers ───────────────────────────────────────────────────────────────────

# Denominators whose decimal expansions terminate (no repeating digits).
# Thirds, sixths, sevenths etc. are excluded - those need fraction answers.
_SCALES = [2, 4, 5, 8, 10, 100]
_SCALE_DP = {2: 1, 4: 2, 5: 1, 8: 3, 10: 1, 100: 2}


def _fmt(value) -> str:
    """Format a number, stripping trailing zeros after the decimal point."""
    if isinstance(value, int):
        return str(value)
    s = f"{value:.4f}".rstrip("0").rstrip(".")
    return s


def _digit_count(n) -> int:
    """Count total digit characters (0-9) in the formatted number."""
    return sum(1 for c in _fmt(n) if c.isdigit())


def _ok(n) -> bool:
    """True if n > 0 and has at most 4 digit characters."""
    return n > 0 and _digit_count(n) <= 4


def _int_distractors(rng: random.Random, correct: int, n: int = 3) -> list:
    """Generate n unique positive integer distractors near correct."""
    pool = [2, 3, 4, 5, 7, 8, 10, 12, 15, -2, -3, -4, -5, -7, -8, -10, -12, -15]
    rng.shuffle(pool)
    result = []
    for offset in pool:
        candidate = correct + offset
        if candidate > 0 and candidate != correct and candidate not in result:
            result.append(candidate)
        if len(result) == n:
            break
    i = 1
    while len(result) < n:
        for sign in (1, -1):
            c = correct + sign * i
            if c > 0 and c != correct and c not in result:
                result.append(c)
            if len(result) == n:
                break
        i += 1
    return result


def _scaled_distractors(rng: random.Random, answer_raw: int, scale: int, dp: int, n: int = 3) -> list:
    """Generate distractors by offsetting answer_raw in integer space, then scaling down."""
    raw = _int_distractors(rng, answer_raw, n)
    result = []
    for d in raw:
        val = round(d / scale, dp)
        if val > 0 and val not in result:
            result.append(val)
    i = 1
    while len(result) < n:
        for sign in (1, -1):
            val = round((answer_raw + sign * i) / scale, dp)
            if val > 0 and val not in result and abs(val - answer_raw / scale) > 1e-9:
                result.append(val)
            if len(result) == n:
                break
        i += 1
    return result[:n]


def _choices(rng: random.Random, correct, distractors: list) -> list:
    """Return a shuffled list of formatted strings: correct answer + distractors."""
    opts = [_fmt(correct)] + [_fmt(d) for d in distractors]
    rng.shuffle(opts)
    return opts


# ── Addition ──────────────────────────────────────────────────────────────────

def missing_operand_add_int(rng: random.Random) -> GeneratedQuestion:
    """A + ? = B; all integers, answer = B - A."""
    a, answer, b = 10, 10, 20
    for _ in range(200):
        a = rng.randint(10, 999)
        answer = rng.randint(10, 999)
        b = a + answer
        if _ok(a) and _ok(answer) and _ok(b):
            break
    distractors = _int_distractors(rng, answer)
    return GeneratedQuestion(
        question_type="missing_operand_add_int",
        topic="missing-operand",
        subtopic="addition",
        effort="low",
        prompt=f"{a} + ? = {b}",
        answer=str(answer),
        answer_display=str(answer),
        hint=f"Subtract {a} from {b}.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "answer": answer, "b": b, "choices": _choices(rng, answer, distractors)},
    )


def missing_operand_add_dec(rng: random.Random) -> GeneratedQuestion:
    """A + ? = B; decimals built by scaling an integer equation."""
    scale, dp = 10, 1
    a, answer, b = 4.6, 1.9, 6.5
    answer_raw = 19
    for _ in range(200):
        scale = rng.choice(_SCALES)
        dp = _SCALE_DP[scale]
        a_raw = rng.randint(1, 9999)
        answer_raw = rng.randint(1, 9999)
        if answer_raw % scale == 0:
            continue
        b_raw = a_raw + answer_raw
        a = round(a_raw / scale, dp)
        answer = round(answer_raw / scale, dp)
        b = round(b_raw / scale, dp)
        if _ok(a) and _ok(answer) and _ok(b):
            break
    distractors = _scaled_distractors(rng, answer_raw, scale, dp)
    return GeneratedQuestion(
        question_type="missing_operand_add_dec",
        topic="missing-operand",
        subtopic="addition",
        effort="low",
        prompt=f"{_fmt(a)} + ? = {_fmt(b)}",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint=f"Subtract {_fmt(a)} from {_fmt(b)}.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "answer": answer, "b": b, "scale": scale,
                  "choices": _choices(rng, answer, distractors)},
    )


# ── Subtraction ───────────────────────────────────────────────────────────────

def missing_operand_sub_int(rng: random.Random) -> GeneratedQuestion:
    """A - ? = B; all integers, answer = A - B."""
    a, answer, b = 20, 10, 10
    for _ in range(200):
        a = rng.randint(20, 999)
        answer = rng.randint(10, a - 1)
        b = a - answer
        if _ok(a) and _ok(answer) and _ok(b):
            break
    distractors = _int_distractors(rng, answer)
    return GeneratedQuestion(
        question_type="missing_operand_sub_int",
        topic="missing-operand",
        subtopic="subtraction",
        effort="low",
        prompt=f"{a} - ? = {b}",
        answer=str(answer),
        answer_display=str(answer),
        hint=f"Subtract {b} from {a}.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "answer": answer, "b": b, "choices": _choices(rng, answer, distractors)},
    )


def missing_operand_sub_dec(rng: random.Random) -> GeneratedQuestion:
    """A - ? = B; decimals built by scaling an integer equation."""
    scale, dp = 10, 1
    a, answer, b = 8.2, 1.9, 6.3
    answer_raw = 19
    for _ in range(200):
        scale = rng.choice(_SCALES)
        dp = _SCALE_DP[scale]
        a_raw = rng.randint(2, 9999)
        answer_raw = rng.randint(1, a_raw - 1)
        if answer_raw % scale == 0:
            continue
        b_raw = a_raw - answer_raw
        if b_raw <= 0:
            continue
        a = round(a_raw / scale, dp)
        answer = round(answer_raw / scale, dp)
        b = round(b_raw / scale, dp)
        if _ok(a) and _ok(answer) and _ok(b):
            break
    distractors = _scaled_distractors(rng, answer_raw, scale, dp)
    return GeneratedQuestion(
        question_type="missing_operand_sub_dec",
        topic="missing-operand",
        subtopic="subtraction",
        effort="low",
        prompt=f"{_fmt(a)} - ? = {_fmt(b)}",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint=f"Subtract {_fmt(b)} from {_fmt(a)}.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "answer": answer, "b": b, "scale": scale,
                  "choices": _choices(rng, answer, distractors)},
    )


# ── Multiplication ────────────────────────────────────────────────────────────

def missing_operand_mul_int(rng: random.Random) -> GeneratedQuestion:
    """A x ? = B; all integers, answer = B / A."""
    a, answer, b = 12, 46, 552
    for _ in range(200):
        a = rng.randint(2, 99)
        answer = rng.randint(2, 99)
        b = a * answer
        if _ok(a) and _ok(answer) and _ok(b):
            break
    distractors = _int_distractors(rng, answer)
    return GeneratedQuestion(
        question_type="missing_operand_mul_int",
        topic="missing-operand",
        subtopic="multiplication",
        effort="low",
        prompt=f"{a} x ? = {b}",
        answer=str(answer),
        answer_display=str(answer),
        hint=f"Divide {b} by {a}.",
        grading=GradingSpec.numeric(),
        metadata={"a": a, "answer": answer, "b": b, "choices": _choices(rng, answer, distractors)},
    )


def missing_operand_mul_dec(rng: random.Random) -> GeneratedQuestion:
    """A x ? = B; A is an integer, ? is a decimal built by scaling.

    Both ? and B have visible decimal parts so the question clearly involves decimals.
    """
    scale, dp = 10, 1
    a, answer_raw = 83, 16
    answer, b = 1.6, 132.8
    for _ in range(200):
        scale = rng.choice(_SCALES)
        dp = _SCALE_DP[scale]
        a = rng.randint(2, 99)
        answer_raw = rng.randint(1, 999)
        if answer_raw % scale == 0:
            continue
        b_raw = a * answer_raw
        if b_raw % scale == 0:
            continue
        answer = round(answer_raw / scale, dp)
        b = round(b_raw / scale, dp)
        if _ok(a) and _ok(answer) and _ok(b):
            break
    distractors = _scaled_distractors(rng, answer_raw, scale, dp)
    return GeneratedQuestion(
        question_type="missing_operand_mul_dec",
        topic="missing-operand",
        subtopic="multiplication",
        effort="medium",
        prompt=f"{a} x ? = {_fmt(b)}",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint=f"Divide {_fmt(b)} by {a}.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"a": a, "answer": answer, "b": b, "scale": scale,
                  "choices": _choices(rng, answer, distractors)},
    )


# ── Division ──────────────────────────────────────────────────────────────────

def missing_operand_div_int(rng: random.Random) -> GeneratedQuestion:
    """A / ? = B; all integers, ? is the missing divisor."""
    answer, result, dividend = 6, 12, 72
    for _ in range(200):
        answer = rng.randint(2, 99)
        result = rng.randint(2, 99)
        dividend = answer * result
        if _ok(dividend) and _ok(answer) and _ok(result):
            break
    distractors = _int_distractors(rng, answer)
    return GeneratedQuestion(
        question_type="missing_operand_div_int",
        topic="missing-operand",
        subtopic="division",
        effort="low",
        prompt=f"{dividend} / ? = {result}",
        answer=str(answer),
        answer_display=str(answer),
        hint=f"Divide {dividend} by {result}.",
        grading=GradingSpec.numeric(),
        metadata={"dividend": dividend, "answer": answer, "result": result,
                  "choices": _choices(rng, answer, distractors)},
    )


def missing_operand_div_dec(rng: random.Random) -> GeneratedQuestion:
    """A / ? = B; ? is a decimal divisor built by scaling.

    Both ? and A have visible decimal parts so the question clearly involves decimals.
    """
    scale, dp = 10, 1
    answer_raw, result = 18, 67
    answer, dividend = 1.8, 120.6
    for _ in range(200):
        scale = rng.choice(_SCALES)
        dp = _SCALE_DP[scale]
        answer_raw = rng.randint(1, 999)
        if answer_raw % scale == 0:
            continue
        result = rng.randint(2, 99)
        dividend_raw = answer_raw * result
        if dividend_raw % scale == 0:
            continue
        answer = round(answer_raw / scale, dp)
        dividend = round(dividend_raw / scale, dp)
        if _ok(dividend) and _ok(answer) and _ok(result):
            break
    distractors = _scaled_distractors(rng, answer_raw, scale, dp)
    return GeneratedQuestion(
        question_type="missing_operand_div_dec",
        topic="missing-operand",
        subtopic="division",
        effort="medium",
        prompt=f"{_fmt(dividend)} / ? = {result}",
        answer=_fmt(answer),
        answer_display=_fmt(answer),
        hint=f"Divide {_fmt(dividend)} by {result}.",
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={"dividend": dividend, "answer": answer, "result": result, "scale": scale,
                  "choices": _choices(rng, answer, distractors)},
    )


GENERATORS = [
    missing_operand_add_int,
    missing_operand_add_dec,
    missing_operand_sub_int,
    missing_operand_sub_dec,
    missing_operand_mul_int,
    missing_operand_mul_dec,
    missing_operand_div_int,
    missing_operand_div_dec,
]
