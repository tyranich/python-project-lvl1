#!/usr/bin/env python3
import random
from brain_games.scripts.for_engine import engine

GREETING = 'Answer "yes" if the number is even, otherwise answer "no".'


def parity_chek(num):
    if num % 2 == 0:
        return True
    else:
        return False


def brain_parity():
    correctly_answer = ''
    num = random.randint(1, 100)
    if parity_chek(num):
        correctly_answer = "yes"
    else:
        correctly_answer = "no"

    return num, correctly_answer


def main():
    engine.engine_for_games(GREETING, "brain_even")


if __name__ == '__main__':
    main()
