#!/usr/bin/env python3
import random
from brain_games.scripts.for_engine import engine


def chek_on_prime(num):
    i = 0
    for _ in range(2, num // 2 + 1):
        if (num % _ == 0):
            i += 1
    if (i <= 0):
        return True
    else:
        return False


GREETING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def brain_primer():

    num = random.randint(1, 100)
    if chek_on_prime(num):
        correctly_answer = "yes"
    else:
        correctly_answer = "no"

    return num, correctly_answer


def main():

    engine.engine_for_games(GREETING, "brain_prime")


if __name__ == "__main__":
    main()
