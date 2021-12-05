#!/usr/bin/env python3
import random
from brain_games.scripts.for_engine import engine


def main():
    name = engine.welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    i = 0
    correctly_answer = ''
    while True:
        num = random.randint(1, 100)
        answer = engine.question_for_user(str(num))
        if num % 2 == 0:
            correctly_answer = "yes"
        else:
            correctly_answer = "no"

        engine.cheking_answer(answer.lower(), correctly_answer, name)

        i += 1
        if i == 3:
            engine.farewell(name)
            break


if __name__ == '__main__':
    main()
