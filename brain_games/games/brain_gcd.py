#!usr/bin/env/ python3
import random

GREETING = "Find the greatest common divisor of given numbers."


def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def generate_round():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    string_for_question = "{} {}".format(first_num, second_num)
    correctly_answer = gcd(first_num, second_num)
    return string_for_question, str(correctly_answer)
