#!usr/bin/env/ python3
from brain_games.scripts.for_engine import engine
import random

greeting = "Find the greatest common divisor of given numbers."


def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def search_gcd():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    string_for_question = "{} {}".format(first_num, second_num)
    correctly_answer = gcd_rem_division(first_num, second_num)
    return string_for_question, str(correctly_answer)


def main():
    engine.engine_for_games(greeting, "brain_gcd.search_gcd()")


if __name__ == "__main__":
    main()
