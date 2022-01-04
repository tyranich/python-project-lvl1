#!/usr/bin/env python3
from brain_games.scripts.for_engine import engine
import random

greeting = "What is the result of the expression?"

def main():

    sings_collection = ("-", "+", "*")
    num = random.randint(1, 10)
    second_num = random.randint(1, 10)
    random_sing = random.choice(sings_collection)
    string_for_question = "{} {} {}".format(num, random_sing, second_num)
    correctly_answer = int(eval(string_for_question))
    return string_for_question, correctly_answer

if __name__ == "__main__":
    engine.engine_for_games(greeting, main())
