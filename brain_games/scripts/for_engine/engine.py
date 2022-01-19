import prompt
import sys
from time import sleep
from brain_games.scripts.games import brain_calc, brain_even, brain_gcd, \
    brain_progression, brain_prime


def choise_games_func(game):

    if game == "brain_calc":
        return brain_calc.brain_calculation()

    elif game == "brain_even":
        return brain_even.brain_parity()

    elif game == "brain_gcd":
        return brain_gcd.search_gcd()

    elif game == "brain_prime":
        return brain_prime.brain_primer()

    elif game == "brain_progression":
        return brain_progression.brain_progress()


def engine_for_games(greeting, func_games):

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    sleep(0.2)
    print(greeting)
    sleep(0.1)
    for _ in range(3):
        question, corct_ans = choise_games_func(func_games)
        print("Question: {} ".format(question))
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
