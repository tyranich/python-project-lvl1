import prompt
import sys
from brain_games.scripts.games import brain_calc, brain_even, brain_gcd,\
    brain_progression, brain_prime


def engine_for_games(greeting, func_games):

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print(greeting)

    for _ in range(3):
        question, corct_ans = eval(func_games)
        print("Question: {}".format(question))
        ans = prompt.string("Your answer: ")

        if ans == corct_ans:
            print("Correct!")
        elif ans != corct_ans:
            txt = "'{}' is wrong answer ;(."
            txt2 = " Correct answer was '{}'"
            print(txt.format(ans) + txt2.format(corct_ans))
            print("Let's try again, {}!".format(name))
            sys.exit(0)

    print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    None
