#!/usr/bin/env python3
import random
import sys


GREETING = "What is the result of the expression?"


def calc(num1, num2, operation):

    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    else:
        print("unknown operation {}".format(operation))
        sys.exit()


def generate_round():

    sings_collection = ("-", "+", "*")
    num = random.randint(1, 10)
    second_num = random.randint(1, 10)
    random_sing = random.choice(sings_collection)
    string_for_question = "{} {} {}".format(num, random_sing, second_num)
    correctly_answer = calc(num, second_num, random_sing)
    return string_for_question, str(correctly_answer)
