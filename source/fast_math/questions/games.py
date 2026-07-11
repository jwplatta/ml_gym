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
            f"If you both get the same number of {face}, you pay them ${pay_them}. "
            f"Otherwise, they pay you ${win}. "
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
            f"{setup}, and I pay you ${you_win} if {win_condition}, "
            f"and you pay me ${they_win} if they don't, "
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
            "Give the threshold as a fraction and the EV as a decimal."
        ),
        answer=f"{threshold_str},{ev_decimal}",
        answer_display=f"Cash out at {threshold_str}, EV = {ev_decimal}",
        hint=(
            f"Keep rolling while expected gain > expected loss: "
            f"p_safe * E[safe] > p_bust * x, i.e. ({p_safe}) * {e_safe} > ({p_bust}) * x. "
            f"Solve for x: cash out when x >= {threshold_str}."
        ),
        grading=GradingSpec.numeric(tolerance=0.01),
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


GENERATORS = [
    proportional_allocation_game,
    coin_match_game,
    random_ttt_game,
    die_bust_optimal_stop,
]
