#!/usr/bin/env python3
from brain_games.scripts.for_engine import engine
import random


def main():

    name = engine.welcome_user()
    print("What is the result of the expression?")
    sings_collection = ("-", "+", "*")
    i = 0
    while True:
        num = random.randint(1, 10)
        second_num = random.randint(1, 10)
        random_sing = random.choice(sings_collection)
        string_for_question = "{} {} {}".format(num, random_sing, second_num)
        correctly_answer = int(eval(string_for_question))
        answer = engine.question_for_user(string_for_question)
        engine.cheking_answer(answer, str(correctly_answer), name)
        i += 1
        if i == 3:
            engine.farewell(name)
            break


if __name__ == "__main__":

    main()
