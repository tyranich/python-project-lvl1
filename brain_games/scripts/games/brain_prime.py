#!/usr/bin/env python3
import random
from brain_games.scripts.for_engine import engine


def chek_on_prime(num):
    i = 0
    for _ in range(2, num // 2 + 1):
        if (num % _ == 0):
            i += 1
    if (i <= 0):
        return "yes"
    else:
        return "no"


def main():
    name = engine.welcome_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    i = 0
    while True:
        num = random.randint(1, 100)
        string_for_question = str(num)
        answer = engine.question_for_user(string_for_question)
        correctly_answer = chek_on_prime(num)
        engine.cheking_answer(answer, correctly_answer, name)
        i += 1
        if i == 3:
            engine.farewell(name)
            break


if __name__ == "__main__":
    main()
