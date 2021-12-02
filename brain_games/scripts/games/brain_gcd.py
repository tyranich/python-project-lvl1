#!/usr/bin/env/ python3

from brain_games.scripts.for_engine import engine
import random


def binary_search(list, number):

    first_index = 0
    last_index = len(list) - 1
    return_val = -1
    while first_index <= last_index and return_val == -1:
        mid = (first_index + last_index) // 2
        if list[mid] == number:
            return_val = 1
        else:
            if number < list[mid]:
                last_index = mid - 1
            else:
                first_index = mid + 1
    return return_val


def finding_divisor(first, second):
    interim_list = []
    a = len(first)
    b = len(second)
    if a > b:
        for _ in second:
            if binary_search(first, _) == 1:
                interim_list.append(_)
    else:
        for _ in first:
            if binary_search(second, _) == 1:
                interim_list.append(_)
    return max(interim_list)


def search_modul_num(num_first, num_second):
    if num_first > num_second:
        modul_num = num_second
    else:
        modul_num = num_second
    return modul_num


def chek_even(num_first, num_second, modul):
    first_list = []
    second_list = []
    for _ in range(modul + 1):
        if _ != 0:
            a = num_first % _
            b = num_second % _
            if a == 0:
                first_list.append(_)
            if b == 0:
                second_list.append(_)
    return first_list, second_list


def main():
    name = engine.welcome_user()
    print("Find the greatest common divisor of given numbers.")
    i = 0
    while True:
        first_num = random.randint(1, 100)
        second_num = random.randint(1, 100)
        string_for_question = "{} {}".format(first_num, second_num)
        answer = engine.question_for_user(string_for_question)
        num_modul = search_modul_num(first_num, second_num)
        first_list, second_list = chek_even(first_num, second_num, num_modul)
        correctly_answer = finding_divisor(first_list, second_list)
        engine.cheking_answer(answer, str(correctly_answer), name)
        i += 1
        if i == 3:
            engine.farewell(name)
            break


if __name__ == "__main__":

    main()
