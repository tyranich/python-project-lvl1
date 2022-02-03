#!usr/bin/env/ python3
import random
import math


GREETING = "Find the greatest common divisor of given numbers."


def generate_round():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    string_for_question = "{} {}".format(first_num, second_num)
    correctly_answer = math.gcd(first_num, second_num)
    return string_for_question, str(correctly_answer)
