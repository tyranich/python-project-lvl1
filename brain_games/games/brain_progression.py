#!/ust/bin/env python
import random


GREETING = "What number is missing in the progression?"


def create_ret_str(first, diff, length):

    str_list = []
    for _ in range(length):
        str_list.append(str(first))
        first += diff
    return str_list


def generate_round():

    first_num = random.randint(1, 50)
    diff_num = random.randint(1, 10)
    len_progressie = random.randint(5, 10)
    ind_cut_elmt = random.randint(0, len_progressie - 1)
    list_str = create_ret_str(first_num, diff_num, len_progressie)
    correctly_answer = list_str[ind_cut_elmt]
    if int(list_str[ind_cut_elmt]) / 10 >= 10:
        list_str[ind_cut_elmt] = "..."
    else:
        list_str[ind_cut_elmt] = ".."

    return_str = " ".join(list_str)
    return return_str, str(correctly_answer)
