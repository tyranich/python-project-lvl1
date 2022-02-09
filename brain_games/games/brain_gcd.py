import random


GREETING = "Find the greatest common divisor of given numbers."


def gcd(num_1, num_2):
    if num_1 == 0:
        return num_2
    return gcd(num_2 % num_1, num_1)


def generate_round():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    string_for_question = "{} {}".format(first_num, second_num)
    correctly_answer = gcd(first_num, second_num)
    return string_for_question, str(correctly_answer)
