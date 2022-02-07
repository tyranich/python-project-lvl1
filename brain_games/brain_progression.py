import random


GREETING = "What number is missing in the progression?"


def create_elmts(first, diff, length):

    elmt_list = []
    for _ in range(length):
        elmt_list.append(first)
        first += diff
    return elmt_list


def generate_round():

    first_num = random.randint(1, 50)
    diff_num = random.randint(1, 10)
    len_progressie = random.randint(5, 10)
    ind_cut_elmt = random.randint(0, len_progressie - 1)
    list_str = create_elmts(first_num, diff_num, len_progressie)
    list_str = [str(i) for i in list_str]
    correctly_answer = list_str[ind_cut_elmt]
    list_str[ind_cut_elmt] = ".."
    return_str = " ".join(list_str)
    return return_str, str(correctly_answer)
