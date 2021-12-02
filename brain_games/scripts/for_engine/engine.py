import prompt
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name


def question_for_user(string_for_question):
    print("Question! {}".format(string_for_question))
    answer = prompt.string("Your answer: ")
    return answer


def cheking_answer(answer, correct_val, name):
    string_wrong_ans = "'{}' is wrong answer ;(. Correct answer was '{}'"
    if answer == correct_val:
        print("Correct!")
    elif answer != correct_val:
        print(string_wrong_ans.format(answer, correct_val))
        print("Let's try again, {}!".format(name))
        sys.exit(0)


def farewell(name):
    print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    None
