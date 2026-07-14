import math
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


def coin_match_game(rng: random.Random) -> GeneratedQuestion:
    n = rng.choice([2, 3, 4, 5, 6])
    face = rng.choice(["heads", "tails"])
    # pay_them > win, both positive
    win = rng.choice([1, 2, 3])
    pay_them = rng.choice([v for v in [2, 3, 4, 5, 6] if v > win])

    # P(match) = C(2n, n) / 4^n  (Vandermonde)
    p_match = Fraction(math.comb(2 * n, n), 4 ** n)
    p_no_match = 1 - p_match
    ev = p_no_match * win - p_match * pay_them

    ev_str = f"{ev.numerator}/{ev.denominator}" if ev.denominator != 1 else str(ev.numerator)
    return GeneratedQuestion(
        question_type="coin_match_game",
        topic="games",
        subtopic="expectation",
        prompt=(
            f"You and another person each flip {n} fair coins. "
            f"If you both get the same number of {face}, you pay them {pay_them}. "
            f"Otherwise, they pay you {win}. "
            "What is your expected payoff? Give a simplified fraction."
        ),
        answer=ev_str,
        answer_display=ev_str,
        hint=(
            f"P(both get same number of {face}) = C(2·{n}, {n}) / 4^{n}. "
            f"EV = P(no match) · {win} - P(match) · {pay_them}."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "n": n,
            "face": face,
            "win": win,
            "pay_them": pay_them,
            "p_match": str(p_match),
            "ev": str(ev),
        },
    )


def random_ttt_game(rng: random.Random) -> GeneratedQuestion:
    n = rng.choice([3, 4, 5, 6])
    cells = n * n
    # winning lines: n rows + n cols + 2 diagonals
    winning_lines = 2 * n + 2
    total_ways = math.comb(cells, n)
    variant = rng.choice(["same", "xo"])

    if variant == "same":
        # All pieces identical: P(ttt) = winning_lines / C(n², n)
        p_win = Fraction(winning_lines, total_ways)
        setup = f"If I toss {n} identical pieces onto a {n}x{n} tic-tac-toe board at random"
        win_condition = "the pieces form a tic-tac-toe (all in one row, column, or diagonal)"
        hint_prob = f"P(tic-tac-toe) = {winning_lines} / C({cells},{n})."
    else:
        # Each of n placed pieces is independently X or O with equal probability.
        # P(ttt) = P(winning line) × P(all same symbol) = [winning_lines/C(n²,n)] × [2/2^n]
        p_win = Fraction(winning_lines * 2, total_ways * (2 ** n))
        setup = f"If I toss {n} pieces onto a {n}x{n} tic-tac-toe board at random, where each piece is independently and randomly assigned to be an X or an O"
        win_condition = "the pieces form a tic-tac-toe (all the same symbol in one row, column, or diagonal)"
        hint_prob = (
            f"P(ttt) = P(winning line) * P(all same symbol) = "
            f"[{winning_lines}/C({cells},{n})] * [2/2^{n}]."
        )

    p_lose = 1 - p_win

    # you_win > they_win so EV favors the other player
    they_win = rng.choice([1, 2, 3])
    you_win = rng.choice([v for v in range(they_win + 1, they_win + 6)])

    ev = p_win * they_win - p_lose * you_win
    ev_str = f"{ev.numerator}/{ev.denominator}" if ev.denominator != 1 else str(ev.numerator)

    return GeneratedQuestion(
        question_type="random_ttt_game",
        topic="games",
        subtopic="expectation",
        prompt=(
            f"{setup}, and I pay you {you_win} if {win_condition}, "
            f"and you pay me {they_win} if they don't, "
            "what is the expected value of the game for me? Give a simplified fraction."
        ),
        answer=ev_str,
        answer_display=ev_str,
        hint=(
            f"There are {cells} cells and {winning_lines} winning lines ({n} rows + {n} cols + 2 diagonals). "
            f"{hint_prob} "
            f"EV = P(win) * {they_win} - P(lose) * {you_win}."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "n": n,
            "cells": cells,
            "winning_lines": winning_lines,
            "total_ways": total_ways,
            "p_win": str(p_win),
            "you_win": you_win,
            "they_win": they_win,
            "variant": variant,
            "ev": str(ev),
        },
    )


def _die_bust_ev(n: int, bust_faces: set[int], safe_faces: list[int], threshold: Fraction) -> Fraction:
    memo: dict[Fraction, Fraction] = {}

    def v(x: Fraction) -> Fraction:
        if x in memo:
            return memo[x]
        if x >= threshold:
            return x
        val = sum(Fraction(1, n) * v(x + f) for f in safe_faces)
        memo[x] = val
        return val

    return v(Fraction(0, 1))


def die_bust_optimal_stop(rng: random.Random) -> GeneratedQuestion:
    n = rng.choice([6, 8, 10, 12])
    faces = list(range(1, n + 1))

    # Pick bust faces: always include 1 and n (extremes), optionally add one more pair
    core_bust = {1, n}
    extra_candidates = [(2, n - 1), (3, n - 2)]
    if rng.random() < 0.4 and n >= 8:
        extra = rng.choice(extra_candidates)
        bust_faces = core_bust | set(extra)
    else:
        bust_faces = core_bust

    safe_faces = [f for f in faces if f not in bust_faces]
    p_bust = Fraction(len(bust_faces), n)
    p_safe = Fraction(len(safe_faces), n)
    e_safe = Fraction(sum(safe_faces), len(safe_faces))
    # Keep rolling while p_safe * E_safe > p_bust * x, i.e. x < threshold
    threshold = p_safe * e_safe / p_bust

    ev = _die_bust_ev(n, bust_faces, safe_faces, threshold)
    ev_decimal = f"{float(ev):.4f}".rstrip("0").rstrip(".")
    threshold_str = str(threshold) if threshold.denominator != 1 else str(threshold.numerator)

    bust_str = ", ".join(str(f) for f in sorted(bust_faces))
    safe_str = ", ".join(str(f) for f in safe_faces)

    return GeneratedQuestion(
        question_type="die_bust_optimal_stop",
        topic="games",
        subtopic="expectation",
        prompt=(
            f"You are playing a game with a fair {n}-sided die. "
            f"If you roll {safe_str}, you add that amount in dollars to your balance. "
            f"If you roll {bust_str}, your balance goes to zero and the game ends. "
            "After each roll you may cash out your balance or keep rolling. "
            "What is your optimal cash-out threshold and expected payout? "
            "Enter as: threshold, EV  (threshold as a fraction, EV as a decimal)."
        ),
        answer=f"{threshold_str},{ev_decimal}",
        answer_display=f"Cash out at {threshold_str}, EV = {ev_decimal}",
        hint=(
            f"Keep rolling while expected gain > expected loss: "
            f"p_safe * E[safe] > p_bust * x, i.e. ({p_safe}) * {e_safe} > ({p_bust}) * x. "
            f"Solve for x: cash out when x >= {threshold_str}."
        ),
        grading=GradingSpec.compound_fraction_numeric(tolerance=0.01),
        metadata={
            "n": n,
            "bust_faces": sorted(bust_faces),
            "safe_faces": safe_faces,
            "p_bust": str(p_bust),
            "p_safe": str(p_safe),
            "e_safe": str(e_safe),
            "threshold": threshold_str,
            "ev": ev_decimal,
        },
    )


def two_urn_bayes_draw(rng: random.Random) -> GeneratedQuestion:
    # Urn A is the "rich" urn (more high-value chips), urn B is the "poor" urn.
    # Vary chip counts and values.
    v_lo = rng.choice([1, 2, 5])
    v_hi = rng.choice([c for c in [10, 20, 50, 100] if c > v_lo])

    # Urn A: more hi chips. Urn B: fewer hi chips.
    total_a = rng.choice([8, 10, 12])
    hi_a = rng.randint(2, total_a - 2)           # at least 2 hi, leave room for lo
    lo_a = total_a - hi_a

    total_b = rng.choice([8, 10, 12])
    # hi_b must be < hi_a (so urns differ) and >= 1
    hi_b = rng.randint(1, max(1, hi_a - 1))
    lo_b = total_b - hi_b

    # P(urn A | drew hi) via Bayes (equal prior)
    p_hi_a = Fraction(hi_a, total_a)
    p_hi_b = Fraction(hi_b, total_b)
    post_a = p_hi_a / (p_hi_a + p_hi_b)
    post_b = 1 - post_a

    # E[draw from same urn] — one hi chip already removed
    e_same_a = Fraction(hi_a - 1, total_a - 1) * v_hi + Fraction(lo_a, total_a - 1) * v_lo
    e_same_b = Fraction(hi_b - 1, total_b - 1) * v_hi + Fraction(lo_b, total_b - 1) * v_lo
    e_same = post_a * e_same_a + post_b * e_same_b

    # E[draw from opposite urn] — urn untouched
    e_full_a = Fraction(hi_a, total_a) * v_hi + Fraction(lo_a, total_a) * v_lo
    e_full_b = Fraction(hi_b, total_b) * v_hi + Fraction(lo_b, total_b) * v_lo
    e_switch = post_a * e_full_b + post_b * e_full_a

    better = "same" if e_same > e_switch else "opposite"
    e_same_str = f"{e_same.numerator}/{e_same.denominator}" if e_same.denominator != 1 else str(e_same.numerator)
    e_switch_str = f"{e_switch.numerator}/{e_switch.denominator}" if e_switch.denominator != 1 else str(e_switch.numerator)
    answer = f"{better},{e_same_str},{e_switch_str}"

    return GeneratedQuestion(
        question_type="two_urn_bayes_draw",
        topic="games",
        subtopic="bayes",
        prompt=(
            f"Two identical-looking urns: urn A has {lo_a} chips worth {v_lo} and {hi_a} chips worth {v_hi}; "
            f"urn B has {lo_b} chips worth {v_lo} and {hi_b} chips worth {v_hi}. "
            f"You randomly pick an urn and draw a chip — it's worth {v_hi}. "
            f"Without replacing it, you may draw a second chip from either urn. "
            f"Should you draw from the same urn or the opposite urn? "
            f"Give the expected value of each choice as a simplified fraction (same urn first, then opposite urn)."
        ),
        answer=answer,
        answer_display=f"Draw from {better} urn. E[same]={e_same_str}, E[opposite]={e_switch_str}",
        hint=(
            f"Use Bayes to find P(urn A | drew {v_hi}): "
            f"P(A|hi) = ({hi_a}/{total_a}) / ({hi_a}/{total_a} + {hi_b}/{total_b}) = {post_a}. "
            f"Then compute E[same] and E[switch] weighting by posterior."
        ),
        grading=GradingSpec.text(),
        metadata={
            "v_lo": v_lo, "v_hi": v_hi,
            "lo_a": lo_a, "hi_a": hi_a, "total_a": total_a,
            "lo_b": lo_b, "hi_b": hi_b, "total_b": total_b,
            "post_a": str(post_a), "post_b": str(post_b),
            "e_same": e_same_str, "e_switch": e_switch_str,
            "better": better,
        },
    )


GENERATORS = [
    proportional_allocation_game,
    coin_match_game,
    random_ttt_game,
    die_bust_optimal_stop,
    two_urn_bayes_draw,
]
