#!/usr/bin/env python3
import random

GREETING = 'Answer "yes" if the number is even, otherwise answer "no".'


def parity_chek(num):
    if num % 2 == 0:
        return True
    else:
        return False


def generate_round():
    correctly_answer = ''
    num = random.randint(1, 100)
    if parity_chek(num):
        correctly_answer = "yes"
    else:
        correctly_answer = "no"

    return str(num), correctly_answer

