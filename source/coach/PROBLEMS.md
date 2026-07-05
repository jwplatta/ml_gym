## params

- one function per question type
- show hint / technique to use
- question types
- keep a log of questions answered
  - correct
  - incorrect
  - passed
- compute stats

## consecutive summation

- What is the sum of all odd numbers up to sixty?
- What is the sum of all integers from 23 to 91?

## probability

- 1,000 fair coins are thrown, what's the possibility of getting an even number of heads?
  - binomial theorem
- We take turn flipping a coin, the first one that get a tail wins the game. Is it an even game? If not what is the probability of the first player winning.
  - recursive expectation
- If I flip 3 coins and tell you at least 1 is heads, what's the probability all 3 are heads?
  - bayesian - ratio of marginal random var to the conditioning random var
- Three biased coins all have different chances of landing heads. The most biased coin lands on heads with probability 7/8, the least biased coin lands on heads with probability 13/24, and the remaining coin lands on heads with probability 2/3. I picked a coin at random to flip and it landed on tails. What is the probability that I picked the most biased coin?
  - bayesian long form - need to use the law of total probability
- permutations
- combinations
- What's the probability of rolling a 6-sided die and getting an even number or a prime number?
- You have two dice, each of which has two sides painted red, two painted black, one painted yellow and the last painted white. When you roll both dice, what is the probability that both land with the same color face up?
- You and I toss a fair coin 3 times each. What is the probability that we will have an equal number of heads?
- There is a family with two children. What are the chances that if one of the children is a girl, that both children are girls?
  - Bayes ratio
- An urn has 98 fair coins. 1 coin with both sides heads, and 1 coin with both sides tails. You pick a coin at random and flip it. Given that you see a heads, what is the probability that it was a coin with both sides heads?
  - topic: Bayes
  - use bayes full formula
- There is a 3x3 cube whose outer surface is painted red. All inner faces are painted white. One of the component cubes (1x1) is taken from the 3x3 cube at random and thrown on a table. What is the conditional probability of the bottom face of this cube being red given that the rest are white?
- A boat fires torpedoes at another boat. The probability that the torpedo hits is 1/3. If the torpedo hits the boat, the boat is destroyed. Two torpedoes are fired. What is the probability of the ship being destroyed?
  - topic: probability rules
- You and your opponent each roll a six-sided die. If you get a larger number, you get $1. Otherwise, you get nothing. What is your expected winning?
  - topic: expectation
- You have a deck of cards, but assume for the face cards that A=1, J=11, Q=12, K=13. For hearts, all the values are doubled. What is the expected value of drawing a card?
  - topic: expectation
- You roll a die until a 6 comes up. What is the expected number of rolls E(x)?
  - If you get a 6 on the first roll, the game ends in 1 roll.
  - If you don't, the problem resets. Your total expected number of flips to get 6 is no E(x)
  - topic: recursive expectation
- What is the expected number of times you must roll a 6 sided die until you see every number at least once?
  - topic: recursive expectation
- If it is a good day (G) there is a 60% chance tomorrow will be G and a 40% chance tomorrow will be bad (B). If it is a B day, there's a 30% chance tomorrow will be G and a 70% chance tomorrow will be B. If today is B, what is the expected number of days before seeing another B?
  - topic: recursive expectation
- You flip a fair coin until you get 3 consecutive heads. What is the expected number of flips?
  - topic: recursive expectation
- What is the variance of a six sided die roll?
  - topic: variance

## stats

## squaring

- nearest tens
- two digit 5s
- Nearest fives
- Power of 2
- Fast 2-Digits

## multiplication

- multiply by 5
- multiply by 25
- multiply by 50
- multiply by 125
- multiply by $10^n$
- multiply by 9
- Fast multiply by 11
- Fast multiply by 12
- Flip a percent x% of y = y% of x
- Reverse FOIL technique for multiplying 2 digit
- Difference in squares method
- Common grounds
  - For example, e.g. $38 \cdot 79 = (40-2)(40 \cdot 2 - 1) = 3200 - 200 +2  = 3002$
  - Multiply `43 x 38` = (40 + 3)(40 - 2)
    - 1600 - 80 + 120 - 6
    - 1634

## constant product
- Smallest number with digits multiplying to x
  - What is the smallest integer whose digits multiply together to equal 108?
  - What is the smallest integer whose digits multiply together to equal 216?
- Largest number with digits multiplying to x
  - What is the largest integer whose digits multiply together to equal 120 (the integer can't contain 1)?


## addition

## subtraction

## division