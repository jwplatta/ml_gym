import math
import random
from fractions import Fraction

from source.fast_math.models import GeneratedQuestion, GradingSpec


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    limit = math.isqrt(value)
    for divisor in range(3, limit + 1, 2):
        if value % divisor == 0:
            return False
    return True


def format_fraction_as_decimal(value: Fraction) -> str:
    return f"{float(value):.4f}".rstrip("0").rstrip(".")


def choose_expectation_answer_format(value: Fraction) -> tuple[str, str, str, GradingSpec]:
    if value.denominator == 1:
        exact_value = str(value.numerator)
        return exact_value, exact_value, "Give an exact answer.", GradingSpec.numeric()

    denominator = value.denominator
    while denominator % 2 == 0:
        denominator //= 2
    while denominator % 5 == 0:
        denominator //= 5

    if denominator == 1 and value.denominator <= 100:
        decimal = format_fraction_as_decimal(value)
        return decimal, f"{decimal} (exactly {value})", "Give a decimal answer.", GradingSpec.numeric(
            tolerance=0.001
        )

    fraction = str(value)
    return fraction, fraction, "Give a simplified fraction.", GradingSpec.fraction()


def solve_linear_system(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    size = len(vector)
    augmented = [row[:] + [value] for row, value in zip(matrix, vector, strict=True)]

    for pivot_index in range(size):
        pivot_row = next(
            row_index for row_index in range(pivot_index, size) if augmented[row_index][pivot_index] != 0
        )
        augmented[pivot_index], augmented[pivot_row] = augmented[pivot_row], augmented[pivot_index]

        pivot = augmented[pivot_index][pivot_index]
        augmented[pivot_index] = [entry / pivot for entry in augmented[pivot_index]]

        for row_index in range(size):
            if row_index == pivot_index:
                continue
            factor = augmented[row_index][pivot_index]
            if factor == 0:
                continue
            augmented[row_index] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(augmented[row_index], augmented[pivot_index], strict=True)
            ]

    return [row[-1] for row in augmented]


def even_or_prime_die_roll(rng: random.Random) -> GeneratedQuestion:
    sides = rng.randrange(2, 20, 2)
    even_outcomes = [value for value in range(1, sides + 1) if value % 2 == 0]
    prime_outcomes = [value for value in range(1, sides + 1) if is_prime(value)]
    overlap_outcomes = sorted(set(even_outcomes) & set(prime_outcomes))
    favorable_outcomes = sorted(set(even_outcomes) | set(prime_outcomes))
    answer = Fraction(len(favorable_outcomes), sides)
    return GeneratedQuestion(
        question_type="even_or_prime_die_roll",
        topic="probability",
        subtopic="probability-rules",
        effort="low",
        prompt=f"What is the probability of rolling a fair {sides}-sided die and getting an even number or a prime number? Give your answer as a simplified fraction.",
        answer=str(answer),
        answer_display=str(answer),
        hint="Use the union rule: P(A or B) = P(A) + P(B) - P(A and B).",
        grading=GradingSpec.fraction(),
        metadata={
            "sample_space": sides,
            "even_outcomes": even_outcomes,
            "prime_outcomes": prime_outcomes,
            "overlap_outcomes": overlap_outcomes,
            "favorable_outcomes": favorable_outcomes,
            "fraction": str(answer),
        },
    )


def equal_heads_n_flips(rng: random.Random) -> GeneratedQuestion:
    flips = rng.randint(1, 5)
    favorable = sum(math.comb(flips, k) ** 2 for k in range(flips + 1))
    total = 2**flips * 2**flips
    result = Fraction(favorable, total)
    return GeneratedQuestion(
        question_type="equal_heads_n_flips",
        topic="probability",
        subtopic="probability-rules",
        effort="medium",
        prompt=f"You and your opponent each flip a fair coin {flips} times. What is the probability that you get the same number of heads? Give a simplified fraction.",
        answer=f"{result.numerator}/{result.denominator}",
        answer_display=f"{result.numerator}/{result.denominator}",
        hint=(
            "Break it into disjoint cases: 0 heads, 1 head, ..., n heads. "
            "For each k, multiply P(you get k heads) by P(opponent gets k heads), "
            "then add those case probabilities together."
        ),
        grading=GradingSpec.fraction(),
        metadata={"flips": flips, "favorable": favorable, "total": total, "fraction": str(result)},
    )


def all_target_children_given_at_least_one(rng: random.Random) -> GeneratedQuestion:
    children = rng.randint(2, 4)
    target_gender = rng.choice(["girl", "boy"])
    answer = Fraction(1, 2**children - 1)
    return GeneratedQuestion(
        question_type="all_target_children_given_at_least_one",
        topic="probability",
        subtopic="bayes",
        effort="medium",
        prompt=(
            f"There is a family with {children} children. Given that at least one child is a {target_gender}, "
            f"what is the probability that all {children} children are {target_gender}s? "
            "Give a simplified fraction."
        ),
        answer=str(answer),
        answer_display=str(answer),
        hint=(
            "List or count all equally likely gender outcomes. "
            f"Remove the one case with no {target_gender}s. "
            f"Among the remaining cases, only one has all {children} children as {target_gender}s."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "children": children,
            "target_gender": target_gender,
            "conditional_outcomes": 2**children - 1,
            "favorable_outcomes": 1,
            "fraction": str(answer),
        },
    )


def double_headed_coin_given_heads(rng: random.Random) -> GeneratedQuestion:
    fair_coins = rng.randint(4, 24)
    double_headed_coins = rng.randint(1, 4)
    double_tailed_coins = rng.randint(1, 4)
    favorable_head_sides = 2 * double_headed_coins
    total_head_sides = fair_coins + 2 * double_headed_coins
    answer = Fraction(favorable_head_sides, total_head_sides)
    return GeneratedQuestion(
        question_type="double_headed_coin_given_heads",
        topic="probability",
        subtopic="bayes",
        effort="medium",
        prompt=(
            f"An urn has {fair_coins} fair coins, {double_headed_coins} coins with both sides heads, "
            f"and {double_tailed_coins} coins with both sides tails. You pick a coin at random and flip it. "
            "Given that you see heads, what is the probability that you picked a coin with both sides heads? "
            "Give a simplified fraction."
        ),
        answer=str(answer),
        answer_display=str(answer),
        hint=(
            "Count head-producing sides. Each fair coin contributes 1 head side, "
            "each double-headed coin contributes 2, and double-tailed coins contribute 0. "
            "Then take the fraction coming from double-headed coins."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "fair_coins": fair_coins,
            "double_headed_coins": double_headed_coins,
            "double_tailed_coins": double_tailed_coins,
            "favorable_head_sides": favorable_head_sides,
            "total_head_sides": total_head_sides,
            "fraction": str(answer),
        },
    )


def painted_cube_hidden_red_given_visible_white(rng: random.Random) -> GeneratedQuestion:
    side_length = rng.randint(3, 6)
    interior_cubes = (side_length - 2) ** 3
    one_red_face_cubes = 6 * (side_length - 2) ** 2
    favorable_orientations = one_red_face_cubes
    total_consistent_orientations = one_red_face_cubes + 6 * interior_cubes
    answer = Fraction(favorable_orientations, total_consistent_orientations)
    return GeneratedQuestion(
        question_type="painted_cube_hidden_red_given_visible_white",
        topic="probability",
        subtopic="bayes",
        effort="high",
        prompt=(
            f"There is a {side_length}x{side_length}x{side_length} cube whose outer surface is painted red "
            "and all inner faces are white. One of the component 1x1 cubes is selected at random and thrown on a table. "
            "Given that all visible faces are white, what is the probability that the bottom face is red? "
            "Give a simplified fraction."
        ),
        answer=str(answer),
        answer_display=str(answer),
        hint=(
            "Only two cube types can show all visible faces white: a completely interior cube, "
            "or a surface-center cube with exactly one red face placed face-down. "
            "Count the valid orientations of each type and form the conditional fraction."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "side_length": side_length,
            "interior_cubes": interior_cubes,
            "one_red_face_cubes": one_red_face_cubes,
            "favorable_orientations": favorable_orientations,
            "total_consistent_orientations": total_consistent_orientations,
            "fraction": str(answer),
        },
    )


def pocket_queens(rng: random.Random) -> GeneratedQuestion:
    rank_name = "queens"
    hand_size = rng.randint(3, 7)
    target_count = rng.randint(1, min(4, hand_size - 1))
    favorable_hands = math.comb(4, target_count) * math.comb(48, hand_size - target_count)
    total_hands = math.comb(52, hand_size)
    answer = Fraction(favorable_hands, total_hands)
    return GeneratedQuestion(
        question_type="pocket_queens",
        topic="probability",
        subtopic="combinations",
        effort="medium",
        prompt=(
            f"What is the probability of getting exactly {target_count} {rank_name} "
            f"in a {hand_size}-card hand from a standard 52-card deck? Give a simplified fraction."
        ),
        answer=str(answer),
        answer_display=str(answer),
        hint=(
            f"Use unordered hands: C(4,{target_count}) * C(48,{hand_size - target_count}) / C(52,{hand_size}). "
            f"C(4,{target_count}) chooses which {target_count} of the 4 queens appear. "
            f"C(48,{hand_size - target_count}) chooses the remaining {hand_size - target_count} non-queen cards from the 48 non-queens. "
            f"C(52,{hand_size}) is the total number of {hand_size}-card hands."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "rank_name": rank_name,
            "hand_size": hand_size,
            "target_count": target_count,
            "favorable_hands": favorable_hands,
            "total_hands": total_hands,
            "fraction": str(answer),
        },
    )


def one_of_each_rank_before_ace_of_diamonds(rng: random.Random) -> GeneratedQuestion:
    required_ranks = rng.sample(["king", "queen", "jack"], k=rng.randint(2, 3))
    relevant_non_ace_cards = 4 * len(required_ranks)
    probability = Fraction(1, 1)

    for seen_rank_count in range(len(required_ranks)):
        unseen_rank_count = len(required_ranks) - seen_rank_count
        favorable_choices = 4 * unseen_rank_count
        remaining_relevant_cards = relevant_non_ace_cards + 1 - seen_rank_count
        probability *= Fraction(favorable_choices, remaining_relevant_cards)

    probability *= Fraction(1, relevant_non_ace_cards + 1 - len(required_ranks))

    rank_labels = [f"{rank}" for rank in required_ranks]
    if len(rank_labels) == 2:
        requirement_text = " and ".join(f"one {label}" for label in rank_labels)
    else:
        requirement_text = ", ".join(f"one {label}" for label in rank_labels[:-1])
        requirement_text += f", and one {rank_labels[-1]}"

    return GeneratedQuestion(
        question_type="one_of_each_rank_before_ace_of_diamonds",
        topic="probability",
        subtopic="combinations",
        effort="high",
        prompt=(
            "Cards are dealt from a randomly shuffled 52-card deck until the ace of diamonds appears. "
            f"What is the probability that exactly {requirement_text} appear before the ace of diamonds? "
            "Give a simplified fraction."
        ),
        answer=str(probability),
        answer_display=str(probability),
        hint=(
            "Ignore all irrelevant cards. Only the relative order of the chosen ranks and the ace of diamonds matters. "
            "Work in the reduced deck, hit one unseen required rank at each step, then hit the ace next."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "required_ranks": required_ranks,
            "relevant_non_ace_cards": relevant_non_ace_cards,
            "fraction": str(probability),
        },
    )


def die_higher_wins_expected_value(rng: random.Random) -> GeneratedQuestion:
    sides = rng.randint(4, 10)
    win_amount = rng.choice([1, 2, 3, 5])
    winning_outcomes = sides * (sides - 1) // 2
    total_outcomes = sides * sides
    expectation = Fraction(win_amount * winning_outcomes, total_outcomes)
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(expectation)
    return GeneratedQuestion(
        question_type="die_higher_wins_expected_value",
        topic="probability",
        subtopic="expectation",
        effort="medium",
        prompt=(
            f"You and your opponent each roll a fair {sides}-sided die. "
            f"If you get a larger number, you win {win_amount}. Otherwise, you get 0. "
            f"What is your expected winning? {answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            "Use the law of total expectation. You only get paid when your roll is larger. "
            "Count the winning ordered pairs, divide by all ordered pairs, then multiply by the payout."
        ),
        grading=grading,
        metadata={
            "sides": sides,
            "win_amount": win_amount,
            "winning_outcomes": winning_outcomes,
            "total_outcomes": total_outcomes,
            "fraction": str(expectation),
            "answer_format": grading.kind,
        },
    )


def expected_rolls_until_target_face(rng: random.Random) -> GeneratedQuestion:
    sides = rng.randint(4, 12)
    target_face = rng.randint(1, sides)
    expectation = Fraction(sides, 1)
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(expectation)
    return GeneratedQuestion(
        question_type="expected_rolls_until_target_face",
        topic="probability",
        subtopic="expectation",
        effort="medium",
        prompt=(
            f"You roll a fair {sides}-sided die until a {target_face} comes up. "
            f"What is the expected number of rolls? {answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            "Use the recursive expectation setup: either you hit the target on the next roll, "
            "or you spend one roll and the problem resets. This gives E = 1/p for success probability p."
        ),
        grading=grading,
        metadata={
            "sides": sides,
            "target_face": target_face,
            "success_probability": f"1/{sides}",
            "fraction": str(expectation),
            "answer_format": grading.kind,
        },
    )


def expected_rolls_to_see_all_faces(rng: random.Random) -> GeneratedQuestion:
    sides = rng.randint(3, 6)
    expectation = sum(Fraction(sides, unseen) for unseen in range(sides, 0, -1))
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(expectation)
    return GeneratedQuestion(
        question_type="expected_rolls_to_see_all_faces",
        topic="probability",
        subtopic="expectation",
        effort="high",
        prompt=(
            f"What is the expected number of rolls of a fair {sides}-sided die until you have seen every face at least once? "
            f"{answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            "Break the process into stages: waiting for the 1st new face, 2nd new face, ..., last new face. "
            "At each stage, the waiting time is 1 divided by the probability of rolling a new face."
        ),
        grading=grading,
        metadata={
            "sides": sides,
            "incremental_expectations": [str(Fraction(sides, unseen)) for unseen in range(sides, 0, -1)],
            "fraction": str(expectation),
            "answer_format": grading.kind,
        },
    )


def expected_days_until_bad_returns(rng: random.Random) -> GeneratedQuestion:
    p_good_to_good = rng.choice([Fraction(1, 5), Fraction(2, 5), Fraction(1, 2), Fraction(3, 5)])
    p_bad_to_good = rng.choice([Fraction(1, 5), Fraction(1, 4), Fraction(1, 3), Fraction(2, 5)])
    p_good_to_bad = 1 - p_good_to_good
    p_bad_to_bad = 1 - p_bad_to_good

    expectation_from_good = Fraction(1, p_good_to_bad)
    expectation_from_bad = 1 + p_bad_to_good * expectation_from_good
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(
        expectation_from_bad
    )
    return GeneratedQuestion(
        question_type="expected_days_until_bad_returns",
        topic="probability",
        subtopic="expectation",
        effort="high",
        prompt=(
            f"If it is a good day (G), there is a {p_good_to_good} chance tomorrow is G and a {p_good_to_bad} chance tomorrow is bad (B). "
            f"If it is a bad day (B), there is a {p_bad_to_good} chance tomorrow is G and a {p_bad_to_bad} chance tomorrow is B. "
            f"If today is B, what is the expected number of days before seeing another B? {answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            "Write two recursive expectations: one starting from B and one from G. "
            "From G, either B arrives tomorrow or you spend one day and stay in the G-state recursion. "
            "Then plug the G result into the B equation."
        ),
        grading=grading,
        metadata={
            "p_good_to_good": str(p_good_to_good),
            "p_good_to_bad": str(p_good_to_bad),
            "p_bad_to_good": str(p_bad_to_good),
            "p_bad_to_bad": str(p_bad_to_bad),
            "expectation_from_good": str(expectation_from_good),
            "fraction": str(expectation_from_bad),
            "answer_format": grading.kind,
        },
    )


def expected_flips_for_consecutive_heads(rng: random.Random) -> GeneratedQuestion:
    streak = rng.randint(2, 4)
    size = streak
    matrix: list[list[Fraction]] = []
    vector: list[Fraction] = []
    for state in range(size):
        row = [Fraction(0) for _ in range(size)]
        row[state] = Fraction(1)
        row[0] -= Fraction(1, 2)
        if state + 1 < streak:
            row[state + 1] -= Fraction(1, 2)
        vector.append(Fraction(1))
        matrix.append(row)

    expectations = solve_linear_system(matrix, vector)
    expectation = expectations[0]
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(expectation)
    return GeneratedQuestion(
        question_type="expected_flips_for_consecutive_heads",
        topic="probability",
        subtopic="expectation",
        effort="high",
        prompt=(
            f"You flip a fair coin until you get {streak} consecutive heads. "
            f"What is the expected number of flips? {answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            "Define states by your current run of consecutive heads: 0, 1, ..., n-1. "
            "Write a recursion for each state. A head moves you forward one state, and a tail resets you to 0."
        ),
        grading=grading,
        metadata={
            "streak": streak,
            "state_expectations": [str(value) for value in expectations],
            "fraction": str(expectation),
            "answer_format": grading.kind,
        },
    )


def expected_draws_until_all_balls_same_color(rng: random.Random) -> GeneratedQuestion:
    balls_per_color = rng.randint(2, 4)
    total_balls = 2 * balls_per_color
    transient_states = list(range(1, total_balls))
    state_to_index = {state: index for index, state in enumerate(transient_states)}
    matrix: list[list[Fraction]] = []
    vector: list[Fraction] = []

    for red_count in transient_states:
        black_count = total_balls - red_count
        p_shift = Fraction(red_count * black_count, total_balls * (total_balls - 1))
        p_same = Fraction(
            red_count * (red_count - 1) + black_count * (black_count - 1),
            total_balls * (total_balls - 1),
        )

        row = [Fraction(0) for _ in transient_states]
        row[state_to_index[red_count]] = 1 - p_same
        if red_count + 1 < total_balls:
            row[state_to_index[red_count + 1]] -= p_shift
        if red_count - 1 > 0:
            row[state_to_index[red_count - 1]] -= p_shift
        matrix.append(row)
        vector.append(Fraction(1))

    expectations = solve_linear_system(matrix, vector)
    expectation = expectations[state_to_index[balls_per_color]]
    answer = format_fraction_as_decimal(expectation)
    return GeneratedQuestion(
        question_type="expected_draws_until_all_balls_same_color",
        topic="probability",
        subtopic="expectation",
        effort="high",
        prompt=(
            f"There are {balls_per_color} red balls and {balls_per_color} black balls in a bag. "
            "Randomly pick 2 balls without replacement, then repaint the second ball to the color of the first. "
            "What is the expected number of draws until all balls have the same color? Give a decimal answer."
        ),
        answer=answer,
        answer_display=f"{answer} (exactly {expectation})",
        hint=(
            "Track the state by how many red balls are in the bag. "
            "A mixed-color draw changes the red count by 1, while a same-color draw leaves the state unchanged. "
            "Write the recursion for the balanced state and its neighbors."
        ),
        grading=GradingSpec.numeric(tolerance=0.001),
        metadata={
            "balls_per_color": balls_per_color,
            "total_balls": total_balls,
            "state_expectations": {
                str(state): str(expectations[state_to_index[state]]) for state in transient_states
            },
            "fraction": str(expectation),
            "answer_format": "numeric",
        },
    )


def fair_die_variance(rng: random.Random) -> GeneratedQuestion:
    sides = rng.randint(4, 12)
    mean = Fraction(sides + 1, 2)
    second_moment = Fraction(sum(face * face for face in range(1, sides + 1)), sides)
    variance = second_moment - mean * mean
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(variance)
    return GeneratedQuestion(
        question_type="fair_die_variance",
        topic="probability",
        subtopic="variance",
        effort="medium",
        prompt=f"What is the variance of a fair {sides}-sided die roll? {answer_instruction}",
        answer=answer,
        answer_display=answer_display,
        hint=(
            "Use Var(X) = E(X^2) - E(X)^2. "
            "Compute the average of the face values and the average of the squared face values."
        ),
        grading=grading,
        metadata={
            "sides": sides,
            "mean": str(mean),
            "second_moment": str(second_moment),
            "fraction": str(variance),
            "answer_format": grading.kind,
        },
    )


def scaled_die_variance(rng: random.Random) -> GeneratedQuestion:
    sides = rng.randint(4, 10)
    scale = rng.choice([2, 3, 4, 5])
    base_variance = Fraction(sides * sides - 1, 12)
    variance = scale * scale * base_variance
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(variance)
    return GeneratedQuestion(
        question_type="scaled_die_variance",
        topic="probability",
        subtopic="variance",
        effort="medium",
        prompt=(
            f"Let X be the result of a fair {sides}-sided die roll. "
            f"What is Var({scale}X)? {answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            "First find Var(X) for the fair die, then use the scaling rule Var(cX) = c^2 Var(X)."
        ),
        grading=grading,
        metadata={
            "sides": sides,
            "scale": scale,
            "base_variance": str(base_variance),
            "fraction": str(variance),
            "answer_format": grading.kind,
        },
    )


def sample_variance_from_dataset(rng: random.Random) -> GeneratedQuestion:
    center = rng.randint(5, 20)
    offset_a = rng.randint(1, 4)
    offset_b = rng.randint(offset_a, 5)
    values = [center - offset_b, center - offset_a, center + offset_a, center + offset_b]
    mean = Fraction(sum(values), len(values))
    sum_squared_deviations = sum((Fraction(value) - mean) ** 2 for value in values)
    sample_variance = sum_squared_deviations / (len(values) - 1)
    values_text = ", ".join(str(value) for value in values)
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(
        sample_variance
    )
    return GeneratedQuestion(
        question_type="sample_variance_from_dataset",
        topic="probability",
        subtopic="variance",
        effort="medium",
        prompt=(
            f"What is the sample variance of the data set {values_text}? "
            f"{answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            "Use s^2 = (1/(n-1)) * sum((x_i - x_bar)^2). "
            "First compute the sample mean. Then find each squared deviation from the mean, "
            "add them up, and divide by n - 1."
        ),
        grading=grading,
        metadata={
            "values": values,
            "mean": str(mean),
            "sum_squared_deviations": str(sum_squared_deviations),
            "fraction": str(sample_variance),
            "answer_format": grading.kind,
        },
    )


def doubled_suit_card_expected_value(rng: random.Random) -> GeneratedQuestion:
    suit = rng.choice(["hearts", "spades", "clubs", "diamonds"])
    multiplier = rng.choice([2, 3, 4])
    base_average = Fraction(1 + 13, 2)
    expectation = base_average * Fraction(3 + multiplier, 4)
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(expectation)
    return GeneratedQuestion(
        question_type="doubled_suit_card_expected_value",
        topic="probability",
        subtopic="expectation",
        effort="medium",
        prompt=(
            f"You draw one card from a standard deck, with A=1, J=11, Q=12, K=13. "
            f"For {suit}, all card values are multiplied by {multiplier}. "
            f"What is the expected value of the card? {answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            "Condition on whether the card is in the special suit. "
            "The average card value in any suit is the same, so multiply that average for the special suit, "
            "then take the weighted average with probability 1/4 versus 3/4."
        ),
        grading=grading,
        metadata={
            "suit": suit,
            "multiplier": multiplier,
            "base_average": str(base_average),
            "fraction": str(expectation),
            "answer_format": grading.kind,
        },
    )


def three_dice_match_expected_value(rng: random.Random) -> GeneratedQuestion:
    sides = rng.randint(4, 8)
    triple_payout = rng.choice([8, 10, 12])
    pair_payout = rng.choice([3, 4, 5])
    all_different_loss = rng.choice([1, 2])

    triple_outcomes = sides
    pair_outcomes = 3 * sides * (sides - 1)
    all_different_outcomes = sides * (sides - 1) * (sides - 2)
    total_outcomes = sides**3
    expectation = Fraction(
        triple_outcomes * triple_payout
        + pair_outcomes * pair_payout
        - all_different_outcomes * all_different_loss,
        total_outcomes,
    )
    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(expectation)
    return GeneratedQuestion(
        question_type="three_dice_match_expected_value",
        topic="probability",
        subtopic="expectation",
        effort="high",
        prompt=(
            f"You roll 3 fair {sides}-sided dice. If all three match, you win {triple_payout}. "
            f"If exactly two match, you win {pair_payout}. If all three are different, you lose {all_different_loss}. "
            f"What is your expected winning? {answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            "Split into three disjoint cases: all three same, exactly two same, and all different. "
            "Count each case, multiply by its payout, then divide by the total number of ordered outcomes."
        ),
        grading=grading,
        metadata={
            "sides": sides,
            "triple_payout": triple_payout,
            "pair_payout": pair_payout,
            "all_different_loss": all_different_loss,
            "triple_outcomes": triple_outcomes,
            "pair_outcomes": pair_outcomes,
            "all_different_outcomes": all_different_outcomes,
            "total_outcomes": total_outcomes,
            "fraction": str(expectation),
            "answer_format": grading.kind,
        },
    )


def torpedoes_destroy_ship(rng: random.Random) -> GeneratedQuestion:
    hit_probability = rng.choice(
        [
            Fraction(1, 5),
            Fraction(1, 4),
            Fraction(1, 3),
            Fraction(2, 5),
            Fraction(1, 2),
            Fraction(3, 5),
        ]
    )
    torpedoes = rng.randint(2, 5)
    destroyed = 1 - (1 - hit_probability) ** torpedoes
    answer = f"{destroyed.numerator}/{destroyed.denominator}"

    return GeneratedQuestion(
        question_type="torpedoes_destroy_ship",
        topic="probability",
        subtopic="probability-rules",
        effort="low",
        prompt=(
            f"A torpedo hits with probability {hit_probability} and destroys the ship if it hits. "
            f"{torpedoes} torpedoes are fired independently. What is the probability the ship is destroyed? "
            "Give a simplified fraction."
        ),
        answer=answer,
        answer_display=answer,
        hint=(
            "Use the complement. First find the probability one torpedo misses, "
            "raise that to the number of torpedoes to get the probability all miss, "
            "then subtract from 1."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "hit_probability": str(hit_probability),
            "miss_probability": str(1 - hit_probability),
            "torpedoes": torpedoes,
            "fraction": answer,
        },
    )


def shared_birthday_period(rng: random.Random) -> GeneratedQuestion:
    period, label, unit = rng.choice([
        (7, "day of the week", "days in a week"),
        (365, "day of the year", "days in a year"),
        (12, "month of the year", "months in a year"),
    ])
    people = rng.randint(2, 5)
    answer = Fraction(1, period ** (people - 1))
    people_str = {2: "two", 3: "three", 4: "four", 5: "five"}[people]
    return GeneratedQuestion(
        question_type="shared_birthday_period",
        topic="probability",
        subtopic="probability-rules",
        effort="low",
        prompt=(
            f"What is the probability that {people_str} people are all born on the same {label}? "
            "Give a simplified fraction."
        ),
        answer=str(answer),
        answer_display=str(answer),
        hint=(
            f"Two equivalent approaches. "
            f"(1) Sum over all {period} {unit}: probability all share a specific {label} is (1/{period})^{people}, "
            f"and there are {period} mutually exclusive choices, so {period} * (1/{period})^{people} = 1/{period}^{people - 1}. "
            f"(2) Fix the first person's {label} — it can be anything. "
            f"Each of the remaining {people - 1} people must independently match it, "
            f"each with probability 1/{period}. Multiply: (1/{period})^{people - 1}."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "period": period,
            "label": label,
            "people": people,
            "fraction": str(answer),
        },
    )


def circular_age_order(rng: random.Random) -> GeneratedQuestion:
    n = rng.randint(3, 10)
    total = math.factorial(n - 1)
    answer = Fraction(2, total)
    return GeneratedQuestion(
        question_type="circular_age_order",
        topic="probability",
        subtopic="combinations",
        effort="medium",
        prompt=(
            f"{n} people with distinct ages sit randomly at a round table. "
            "What is the probability they are seated in either ascending or descending order of age "
            "(clockwise)? Give a simplified fraction."
        ),
        answer=str(answer),
        answer_display=str(answer),
        hint=(
            f"Round table arrangements: fix one person's seat to remove rotational duplicates, "
            f"giving (N-1)! = {total} equally likely orderings. "
            "Only 2 of these are fully sorted by age: one clockwise ascending, one clockwise descending. "
            f"P = 2 / (N-1)! = 2/{total}."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "n": n,
            "total_arrangements": total,
            "fraction": str(answer),
        },
    )


def tournament_top_two_meet_in_round(rng: random.Random) -> GeneratedQuestion:
    exponent = rng.randint(3, 7)  # 8 to 128 players
    n = 2 ** exponent
    round_number = rng.randint(1, exponent)
    group_size = 2 ** round_number
    answer = Fraction(group_size // 2, n - 1)
    round_names = {1: "the first round", exponent: "the final"}
    round_label = round_names.get(round_number, f"round {round_number}")
    return GeneratedQuestion(
        question_type="tournament_top_two_meet_in_round",
        topic="probability",
        subtopic="combinations",
        effort="high",
        prompt=(
            f"A single-elimination tennis tournament has {n} players. "
            "Each player has a unique rating and the higher-rated player always wins. "
            f"What is the probability that the two highest-rated players meet in {round_label}? "
            "Give a simplified fraction."
        ),
        answer=str(answer),
        answer_display=str(answer),
        hint=(
            "For two players to meet in exactly round r, they must be placed in the same group of size 2^r "
            "but in different halves of that group (each of size 2^(r-1)). "
            "Fix player 1's position. Player 2 must land in one of the 2^(r-1) slots in the other half of that group, "
            "out of n-1 remaining slots total. P = 2^(r-1) / (n-1)."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "n": n,
            "round_number": round_number,
            "group_size": group_size,
            "fraction": str(answer),
        },
    )


def tournament_one_and_three_meet_in_final(rng: random.Random) -> GeneratedQuestion:
    exponent = rng.randint(3, 7)  # 8 to 128 players
    n = 2 ** exponent
    half = n // 2
    p2_same = Fraction(half - 1, n - 1)
    p3_other = Fraction(half, n - 2)
    answer = p2_same * p3_other
    return GeneratedQuestion(
        question_type="tournament_one_and_three_meet_in_final",
        topic="probability",
        subtopic="combinations",
        effort="high",
        prompt=(
            f"A single-elimination tennis tournament has {n} players. "
            "Each player has a unique rating and the higher-rated player always wins. "
            "What is the probability that the highest-rated and third-highest-rated players meet in the final? "
            "Give a simplified fraction."
        ),
        answer=str(answer),
        answer_display=str(answer),
        hint=(
            "For players 1 and 3 to meet in the final they must be in opposite halves of the bracket, "
            "and player 2 must be in the same half as player 1 (otherwise player 3 gets eliminated by player 2). "
            "Multiply: P(player 2 in player 1's half) * P(player 3 in the other half | that)."
        ),
        grading=GradingSpec.fraction(),
        metadata={
            "n": n,
            "half": half,
            "p2_same_bracket": str(p2_same),
            "p3_other_bracket": str(p3_other),
            "fraction": str(answer),
        },
    )


def two_die_optimal_stop(rng: random.Random) -> GeneratedQuestion:
    # Roll die 1 (n sides), then optionally roll die 2 (m sides).
    # Keep die 1's value v iff v > E[die2]; otherwise take die 2.
    # E[die2] = (m+1)/2. Threshold: keep iff v >= floor((m+1)/2) + 1.
    die_pairs = [(n, m) for n in range(4, 13) for m in range(4, 13) if n != m]
    n, m = rng.choice(die_pairs)

    e_die2 = Fraction(m + 1, 2)
    # Keep v if v > e_die2, i.e. v >= floor(e_die2) + 1
    threshold = int(e_die2) + 1  # works for both integer and half-integer e_die2

    keep_values = [v for v in range(1, n + 1) if v >= threshold]
    reroll_count = n - len(keep_values)

    ev = (Fraction(reroll_count, n) * e_die2 +
          Fraction(sum(keep_values), n))

    answer, answer_display, answer_instruction, grading = choose_expectation_answer_format(ev)
    return GeneratedQuestion(
        question_type="two_die_optimal_stop",
        topic="probability",
        subtopic="expectation",
        effort="high",
        prompt=(
            f"You roll a fair {n}-sided die and see the result. You can keep it and get paid that amount, "
            f"or instead roll a fair {m}-sided die and get paid that amount. "
            f"If you play optimally, what is the expected value of the game? {answer_instruction}"
        ),
        answer=answer,
        answer_display=answer_display,
        hint=(
            f"Find the expected value of the {m}-sided die: (1+{m})/2. "
            f"Keep your first roll only if it exceeds that value. "
            "Then compute the weighted average over all first-roll outcomes."
        ),
        grading=grading,
        metadata={
            "n": n,
            "m": m,
            "threshold": threshold,
            "keep_values": keep_values,
            "reroll_count": reroll_count,
            "ev_fraction": str(ev),
        },
    )


_CITY_NAME_POOLS = [
    ["Aldara", "Brenholm", "Corvex", "Duskfen", "Eldris"],
    ["Falmoor", "Grenth", "Havris", "Iravel", "Jorwick"],
    ["Kish", "Kesh", "Kuara", "Lund", "Merath"],
    ["Navik", "Orveth", "Paldur", "Quell", "Rethis"],
    ["Solfen", "Tarmis", "Ulvra", "Vendis", "Wyreth"],
]

_EYE_COLORS = ["blue", "green", "hazel", "amber", "grey"]


def total_probability_eye_color(rng: random.Random) -> GeneratedQuestion:
    n_cities = rng.randint(2, 5)
    city_pool = rng.choice(_CITY_NAME_POOLS)
    cities = rng.sample(city_pool, k=n_cities)
    eye_color = rng.choice(_EYE_COLORS)

    # Populations: multiples of 500 between 500 and 5000
    populations = [rng.randrange(500, 5001, 500) for _ in range(n_cities)]
    total_pop = sum(populations)

    # Eye color percentages: multiples of 1% between 1% and 40%
    pct_ints = [rng.randint(1, 40) for _ in range(n_cities)]

    # Exact computation via fractions
    blue_eyed_people = sum(
        Fraction(pop * pct, 100)
        for pop, pct in zip(populations, pct_ints)
    )
    p_blue = blue_eyed_people / total_pop

    # Format as a percentage value (e.g. 14.5 meaning 14.5%) rounded to 2 decimal places
    p_blue_float = float(p_blue)
    pct_value = round(p_blue_float * 100, 2)
    answer = f"{pct_value:.2f}".rstrip("0").rstrip(".")

    # Build prompt
    city_lines = "; ".join(
        f"{city} (pop {pop:,}, {pct}% {eye_color} eyes)"
        for city, pop, pct in zip(cities, populations, pct_ints)
    )
    prompt = (
        f"There are {n_cities} cities: {city_lines}. "
        f"A person is chosen at random from the combined population. "
        f"What is the probability they have {eye_color} eyes? "
        f"Use the law of total probability and give your answer as a percentage (e.g. enter 14.5 for 14.5%), rounded to 2 decimal places."
    )

    # Build hint showing the weighted sum
    weight_terms = " + ".join(
        f"({pop:,}/{total_pop:,}) × {pct}%"
        for pop, pct in zip(populations, pct_ints)
    )
    hint = (
        f"P({eye_color}) = Σ P(city_i) × P({eye_color} | city_i). "
        f"= {weight_terms}."
    )

    return GeneratedQuestion(
        question_type="total_probability_eye_color",
        topic="probability",
        subtopic="total-probability",
        effort="medium",
        prompt=prompt,
        answer=answer,
        answer_display=f"{answer}%",
        hint=hint,
        grading=GradingSpec.numeric(tolerance=0.01),
        metadata={
            "cities": cities,
            "populations": populations,
            "pct_ints": pct_ints,
            "eye_color": eye_color,
            "total_pop": total_pop,
            "fraction": str(p_blue),
        },
    )


_CHAIN_RULE_SCENARIOS = [
    {
        "group": "people",
        "trait": "been to Boston in the fall",
        "setting": "at our party",
        "pick_verb": "pick",
    },
    {
        "group": "students",
        "trait": "failed the midterm",
        "setting": "in the class",
        "pick_verb": "select",
    },
    {
        "group": "employees",
        "trait": "worked overtime last week",
        "setting": "at the company",
        "pick_verb": "choose",
    },
    {
        "group": "cards",
        "trait": "hearts",
        "setting": "in the deck",
        "pick_verb": "draw",
    },
    {
        "group": "balls",
        "trait": "red",
        "setting": "in the urn",
        "pick_verb": "draw",
    },
    {
        "group": "patients",
        "trait": "allergic to penicillin",
        "setting": "in the ward",
        "pick_verb": "select",
    },
]


def chain_rule_none_have_trait(rng: random.Random) -> GeneratedQuestion:
    scenario = rng.choice(_CHAIN_RULE_SCENARIOS)
    group = scenario["group"]
    trait = scenario["trait"]
    setting = scenario["setting"]
    pick_verb = scenario["pick_verb"]

    # Total population: 20–80, pick_count: 2–5, trait_count: small fraction
    total = rng.choice([20, 24, 30, 36, 40, 48, 50, 60])
    pick_count = rng.randint(2, 5)
    # trait_count: between 2 and ~15% of total, but leave enough non-trait items
    max_trait = max(2, total // 8)
    trait_count = rng.randint(2, max_trait)
    non_trait = total - trait_count

    # P(none have trait) via chain rule (sampling without replacement)
    # = (non_trait / total) * ((non_trait-1) / (total-1)) * ...
    answer = Fraction(1)
    for k in range(pick_count):
        answer *= Fraction(non_trait - k, total - k)

    answer_str = str(answer)

    # Build chain rule expansion for hint
    chain_terms = " × ".join(
        f"({non_trait - k}/{total - k})" for k in range(pick_count)
    )

    prompt = (
        f"There are {total} {group} {setting}, of which {trait_count} have {trait}. "
        f"We {pick_verb} {pick_count} {group} at random without replacement. "
        f"What is the probability that none of them have {trait}? Give a simplified fraction."
    )
    hint = (
        f"Use the chain rule (sampling without replacement). "
        f"There are {non_trait} {group} without the trait out of {total} total. "
        f"P(none) = {chain_terms} = {answer_str}."
    )

    return GeneratedQuestion(
        question_type="chain_rule_none_have_trait",
        topic="probability",
        subtopic="conditional-probability",
        effort="low",
        prompt=prompt,
        answer=answer_str,
        answer_display=answer_str,
        hint=hint,
        grading=GradingSpec.fraction(),
        metadata={
            "scenario": scenario["group"],
            "total": total,
            "trait_count": trait_count,
            "non_trait": non_trait,
            "pick_count": pick_count,
            "fraction": answer_str,
        },
    )


_COIN_BIASES = [
    Fraction(1, 2),
    Fraction(1, 3),
    Fraction(2, 3),
    Fraction(1, 4),
    Fraction(3, 4),
    Fraction(1, 5),
    Fraction(2, 5),
    Fraction(3, 5),
    Fraction(4, 5),
]


def exactly_k_heads_in_n_flips(rng: random.Random) -> GeneratedQuestion:
    # n > k to avoid the trivial k=n case; n in 4..10, k in 1..n-2
    n = rng.randint(4, 10)
    k = rng.randint(1, n - 2)
    p = rng.choice(_COIN_BIASES)
    q = 1 - p
    ways = math.comb(n, k)
    answer = Fraction(ways) * p**k * q**(n - k)
    answer_str = str(answer)

    if p == Fraction(1, 2):
        coin_desc = "a fair coin"
        p_display = "1/2"
        effort = "low"
    else:
        coin_desc = f"a biased coin (heads probability {p})"
        p_display = str(p)
        effort = "medium"

    return GeneratedQuestion(
        question_type="exactly_k_heads_in_n_flips",
        topic="probability",
        subtopic="probability-rules",
        effort=effort,
        prompt=(
            f"You flip {coin_desc} {n} times. "
            f"What is the probability of getting exactly {k} heads? "
            f"Give a simplified fraction."
        ),
        answer=answer_str,
        answer_display=answer_str,
        hint=(
            f"Use the binomial formula: C({n},{k}) × ({p_display})^{k} × ({q})^{n-k}. "
            f"C({n},{k}) = {ways}, so the answer is {ways} × {p**k} × {q**(n-k)} = {answer_str}."
        ),
        grading=GradingSpec.fraction(),
        metadata={"n": n, "k": k, "p": str(p), "ways": ways, "fraction": answer_str},
    )


def at_most_k_heads(rng: random.Random) -> GeneratedQuestion:
    n = rng.randint(3, 8)
    k = rng.randint(0, n - 1)
    favorable = sum(math.comb(n, i) for i in range(k + 1))
    total = 2 ** n
    result = Fraction(favorable, total)
    return GeneratedQuestion(
        question_type="at_most_k_heads",
        topic="probability",
        subtopic="probability-rules",
        effort="low",
        prompt=f"What is the probability of getting at most {k} heads in {n} fair coin flips? Give a simplified fraction.",
        answer=f"{result.numerator}/{result.denominator}",
        answer_display=f"{result.numerator}/{result.denominator}",
        hint=f"Sum the binomial probabilities for 0, 1, ..., {k} heads. P(X=i) = C({n},i) / 2^{n}.",
        grading=GradingSpec.fraction(),
        metadata={"n": n, "k": k, "favorable": favorable, "total": total},
    )


_CT3_SCENARIOS = [
    {
        "name": "Titanic passengers",
        "outcome_labels": ["Survived", "Died"],
        "sex_labels": ["Male", "Female"],
        "cabin_name": "cabin class",
        "cabin_labels": ["Cabin 1", "Cabin 2", "Cabin 3"],
    },
    {
        "name": "hospital patients",
        "outcome_labels": ["Recovered", "Died"],
        "sex_labels": ["Male", "Female"],
        "cabin_name": "ward",
        "cabin_labels": ["Ward A", "Ward B", "Ward C"],
    },
    {
        "name": "clinical trial participants",
        "outcome_labels": ["Improved", "Not Improved"],
        "sex_labels": ["Male", "Female"],
        "cabin_name": "treatment group",
        "cabin_labels": ["Placebo", "Drug A", "Drug B"],
    },
    {
        "name": "flight passengers",
        "outcome_labels": ["On Time", "Delayed"],
        "sex_labels": ["Male", "Female"],
        "cabin_name": "seating class",
        "cabin_labels": ["Economy", "Business", "First Class"],
    },
]


def _ct3_random_counts(rng: random.Random, n_cells: int, total: int) -> list[int]:
    """Stars-and-bars: n_cells positive integers summing to total."""
    cuts = sorted(rng.sample(range(1, total), k=n_cells - 1))
    counts = [cuts[0]] + [cuts[i] - cuts[i - 1] for i in range(1, n_cells - 1)] + [total - cuts[-1]]
    return counts


def _ct3_build_table_md(
    scenario: dict,
    table: list[list[list[Fraction]]],
) -> str:
    """Build a markdown pipe table for a 3D contingency table (outcome x sex x cabin)."""
    outcome_labels = scenario["outcome_labels"]
    sex_labels = scenario["sex_labels"]
    cabin_labels = scenario["cabin_labels"]
    cabin_name = scenario["cabin_name"]
    n_cabins = len(cabin_labels)

    header = "| | | " + " | ".join(cabin_labels) + " | Total |"
    sep = "|---|---|" + "---|" * (n_cabins + 1)

    rows = []
    for o, outcome in enumerate(outcome_labels):
        for s, sex in enumerate(sex_labels):
            cells = " | ".join(str(table[o][s][c]) for c in range(n_cabins))
            row_total = sum(table[o][s][c] for c in range(n_cabins))
            prefix = f"| **{outcome}** | {sex} |" if s == 0 else f"| | {sex} |"
            rows.append(f"{prefix} {cells} | {row_total} |")
        # Outcome subtotal row: P(outcome) across all sexes and cabins
        outcome_cabin_totals = [
            sum(table[o][s][c] for s in range(2)) for c in range(n_cabins)
        ]
        outcome_total = sum(outcome_cabin_totals)
        subtotal_cells = " | ".join(str(t) for t in outcome_cabin_totals)
        rows.append(f"| ***{outcome} total*** | | {subtotal_cells} | **{outcome_total}** |")

    # Column totals (marginal over outcome and sex, by cabin)
    cabin_totals = [
        sum(table[o][s][c] for o in range(2) for s in range(2))
        for c in range(n_cabins)
    ]
    total_row = "| **Total** | | " + " | ".join(str(t) for t in cabin_totals) + " | 1 |"

    caption = f"*Joint probability table — {scenario['name']} by sex and {cabin_name}*"
    return "\n".join([caption, "", header, sep] + rows + [total_row])


def contingency_table_3d(rng: random.Random) -> GeneratedQuestion:
    scenario = rng.choice(_CT3_SCENARIOS)
    outcome_labels = scenario["outcome_labels"]
    sex_labels = scenario["sex_labels"]
    cabin_labels = scenario["cabin_labels"]
    cabin_name = scenario["cabin_name"]
    n_cabins = len(cabin_labels)
    n_cells = 2 * 2 * n_cabins  # outcomes × sexes × cabins

    total = rng.choice([24, 30, 36, 40, 48, 60])
    counts = _ct3_random_counts(rng, n_cells, total)

    # table[o][s][c] = Fraction joint probability
    table: list[list[list[Fraction]]] = [
        [
            [Fraction(counts[o * 2 * n_cabins + s * n_cabins + c], total) for c in range(n_cabins)]
            for s in range(2)
        ]
        for o in range(2)
    ]

    # Precompute all marginals
    def p_osc(o: int, s: int, c: int) -> Fraction:
        return table[o][s][c]

    def p_os(o: int, s: int) -> Fraction:
        return sum(table[o][s][c] for c in range(n_cabins))

    def p_oc(o: int, c: int) -> Fraction:
        return sum(table[o][s][c] for s in range(2))

    def p_sc(s: int, c: int) -> Fraction:
        return sum(table[o][s][c] for o in range(2))

    def p_o(o: int) -> Fraction:
        return sum(table[o][s][c] for s in range(2) for c in range(n_cabins))

    def p_s(s: int) -> Fraction:
        return sum(table[o][s][c] for o in range(2) for c in range(n_cabins))

    def p_c(c: int) -> Fraction:
        return sum(table[o][s][c] for o in range(2) for s in range(2))

    table_md = _ct3_build_table_md(scenario, table)

    # Pick random indices
    o = rng.randrange(2)
    s = rng.randrange(2)
    c = rng.randrange(n_cabins)

    OL = outcome_labels
    SL = sex_labels
    CL = cabin_labels

    question_subtype = rng.choices(
        [
            "joint_3way",
            "joint_os",
            "joint_oc",
            "joint_sc",
            "marginal_o",
            "marginal_s",
            "marginal_c",
            "cond_o_given_s",
            "cond_o_given_c",
            "cond_o_given_sc",
            "cond_s_given_o",
            "cond_c_given_o",
            "cond_os_given_c",
        ],
        weights=[8, 6, 6, 6, 5, 5, 5, 10, 10, 12, 10, 10, 7],
        k=1,
    )[0]

    if question_subtype == "joint_3way":
        answer = p_osc(o, s, c)
        q = f"What is the probability that a randomly selected person is **{SL[s]}**, **{OL[o]}**, and in **{CL[c]}**?"
        hint = f"P({OL[o]}, {SL[s]}, {CL[c]}) is read directly from the table: {answer}."

    elif question_subtype == "joint_os":
        answer = p_os(o, s)
        terms = " + ".join(str(table[o][s][c2]) for c2 in range(n_cabins))
        q = f"What is the probability that a randomly selected person is **{SL[s]}** and **{OL[o]}**?"
        hint = f"P({OL[o]}, {SL[s]}) = sum over all {cabin_name}s: {terms} = {answer}."

    elif question_subtype == "joint_oc":
        answer = p_oc(o, c)
        terms = " + ".join(str(table[o][s2][c]) for s2 in range(2))
        q = f"What is the probability that a randomly selected person is **{OL[o]}** and in **{CL[c]}**?"
        hint = f"P({OL[o]}, {CL[c]}) = sum over both sexes: {terms} = {answer}."

    elif question_subtype == "joint_sc":
        answer = p_sc(s, c)
        terms = " + ".join(str(table[o2][s][c]) for o2 in range(2))
        q = f"What is the probability that a randomly selected person is **{SL[s]}** and in **{CL[c]}**?"
        hint = f"P({SL[s]}, {CL[c]}) = sum over both outcomes: {terms} = {answer}."

    elif question_subtype == "marginal_o":
        answer = p_o(o)
        terms = " + ".join(str(table[o][s2][c2]) for s2 in range(2) for c2 in range(n_cabins))
        q = f"What is the probability that a randomly selected person is **{OL[o]}**?"
        hint = f"P({OL[o]}) = sum all cells in the '{OL[o]}' rows: {terms} = {answer}."

    elif question_subtype == "marginal_s":
        answer = p_s(s)
        terms = " + ".join(str(table[o2][s][c2]) for o2 in range(2) for c2 in range(n_cabins))
        q = f"What is the probability that a randomly selected person is **{SL[s]}**?"
        hint = f"P({SL[s]}) = sum all cells in the '{SL[s]}' rows: {terms} = {answer}."

    elif question_subtype == "marginal_c":
        answer = p_c(c)
        terms = " + ".join(str(table[o2][s2][c]) for o2 in range(2) for s2 in range(2))
        q = f"What is the probability that a randomly selected person is in **{CL[c]}**?"
        hint = f"P({CL[c]}) = sum all cells in the '{CL[c]}' column: {terms} = {answer}."

    elif question_subtype == "cond_o_given_s":
        denom = p_s(s)
        answer = p_os(o, s) / denom
        q = f"Given that a person is **{SL[s]}**, what is the probability they are **{OL[o]}**?"
        hint = (
            f"P({OL[o]} | {SL[s]}) = P({OL[o]}, {SL[s]}) / P({SL[s]}) "
            f"= {p_os(o, s)} / {denom} = {answer}."
        )

    elif question_subtype == "cond_o_given_c":
        denom = p_c(c)
        answer = p_oc(o, c) / denom
        q = f"Given that a person is in **{CL[c]}**, what is the probability they are **{OL[o]}**?"
        hint = (
            f"P({OL[o]} | {CL[c]}) = P({OL[o]}, {CL[c]}) / P({CL[c]}) "
            f"= {p_oc(o, c)} / {denom} = {answer}."
        )

    elif question_subtype == "cond_o_given_sc":
        denom = p_sc(s, c)
        answer = p_osc(o, s, c) / denom
        q = (
            f"Given that a person is **{SL[s]}** and in **{CL[c]}**, "
            f"what is the probability they are **{OL[o]}**?"
        )
        hint = (
            f"P({OL[o]} | {SL[s]}, {CL[c]}) = P({OL[o]}, {SL[s]}, {CL[c]}) / P({SL[s]}, {CL[c]}) "
            f"= {p_osc(o, s, c)} / {denom} = {answer}."
        )

    elif question_subtype == "cond_s_given_o":
        denom = p_o(o)
        answer = p_os(o, s) / denom
        q = f"Given that a person is **{OL[o]}**, what is the probability they are **{SL[s]}**?"
        hint = (
            f"P({SL[s]} | {OL[o]}) = P({OL[o]}, {SL[s]}) / P({OL[o]}) "
            f"= {p_os(o, s)} / {denom} = {answer}."
        )

    elif question_subtype == "cond_c_given_o":
        denom = p_o(o)
        answer = p_oc(o, c) / denom
        q = f"Given that a person is **{OL[o]}**, what is the probability they are in **{CL[c]}**?"
        hint = (
            f"P({CL[c]} | {OL[o]}) = P({OL[o]}, {CL[c]}) / P({OL[o]}) "
            f"= {p_oc(o, c)} / {denom} = {answer}."
        )

    else:  # cond_os_given_c
        denom = p_c(c)
        answer = p_osc(o, s, c) / denom
        q = (
            f"Given that a person is in **{CL[c]}**, "
            f"what is the probability they are **{SL[s]}** and **{OL[o]}**?"
        )
        hint = (
            f"P({SL[s]}, {OL[o]} | {CL[c]}) = P({OL[o]}, {SL[s]}, {CL[c]}) / P({CL[c]}) "
            f"= {p_osc(o, s, c)} / {denom} = {answer}."
        )

    answer_str = str(answer)
    prompt = (
        f"The table shows joint probabilities for **{scenario['name']}**.\n\n"
        f"{table_md}\n\n"
        f"{q} Give a simplified fraction."
    )

    return GeneratedQuestion(
        question_type="contingency_table_3d",
        topic="probability",
        subtopic="conditional-probability",
        effort="medium",
        prompt=prompt,
        answer=answer_str,
        answer_display=answer_str,
        hint=hint,
        grading=GradingSpec.fraction(),
        metadata={
            "scenario": scenario["name"],
            "outcome_labels": outcome_labels,
            "sex_labels": sex_labels,
            "cabin_labels": cabin_labels,
            "cabin_name": cabin_name,
            "total": total,
            "counts": counts,
            "question_subtype": question_subtype,
            "o": o,
            "s": s,
            "c": c,
            "fraction": answer_str,
        },
    )


GENERATORS = [
    even_or_prime_die_roll,
    equal_heads_n_flips,
    all_target_children_given_at_least_one,
    double_headed_coin_given_heads,
    painted_cube_hidden_red_given_visible_white,
    pocket_queens,
    one_of_each_rank_before_ace_of_diamonds,
    die_higher_wins_expected_value,
    expected_rolls_until_target_face,
    expected_rolls_to_see_all_faces,
    expected_days_until_bad_returns,
    expected_flips_for_consecutive_heads,
    expected_draws_until_all_balls_same_color,
    fair_die_variance,
    scaled_die_variance,
    sample_variance_from_dataset,
    doubled_suit_card_expected_value,
    three_dice_match_expected_value,
    torpedoes_destroy_ship,
    shared_birthday_period,
    circular_age_order,
    tournament_top_two_meet_in_round,
    tournament_one_and_three_meet_in_final,
    at_most_k_heads,
    two_die_optimal_stop,
    total_probability_eye_color,
    contingency_table_3d,
    chain_rule_none_have_trait,
    exactly_k_heads_in_n_flips,
]
