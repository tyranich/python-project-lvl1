#!/ust/bin/env python
import random
from brain_games.scripts.for_engine import engine


def create_ret_str(str_prog, cut_str):

    return_string = ""

    for _ in range(len(str_prog)):
        if _ == cut_str + 2 and str_prog[cut_str + 2] != ' ':
            return_string = return_string + "."
        elif _ != cut_str and _ != cut_str + 1:
            return_string = return_string + str_prog[_]
        else:
            return_string = return_string + "."

    return return_string


greeting = "What number is missing in the progression?"


def brain_progress():

    num_start_progressive = random.randint(1, 50)
    magnifer = random.randint(1, 10)
    len_progressie = random.randint(5, 10)
    string_progres = ""
    list_progres = []

    for _ in range(len_progressie):
        num_start_progressive = num_start_progressive + magnifer
        list_progres.append(num_start_progressive)
        string_progres = string_progres + str(num_start_progressive) + " "

    cut_element = random.choice(list_progres)
    cut_string = string_progres.find(str(cut_element))

    correctly_answer = cut_element
    return_str = create_ret_str(string_progres, cut_string)
    return return_str, str(correctly_answer)


def main():
    engine.engine_for_games(greeting, "brain_progression")


if __name__ == "__main__":
    main()
