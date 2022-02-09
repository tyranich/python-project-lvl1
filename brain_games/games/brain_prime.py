import random

GREETING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):

    for _ in range(2, num // 2 + 1):
        if (num % _ == 0):
            return False
    return True


def generate_round():

    num = random.randint(1, 100)
    if is_prime(num):
        correctly_answer = "yes"
    else:
        correctly_answer = "no"

    return str(num), correctly_answer
