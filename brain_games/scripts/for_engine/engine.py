import prompt
import sys


def engine_for_games(greeting, create_question):

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name)) 
    print(greeting)
    
    while i < 3:
        question, correct_ans = create_question()
        print("Question: {}".format(question))
        answer = prompt.string("Your answer: ")
        if answer == correct_ans:
            i += 1
            print("Correct!")
        elif answer != correct_ans:
            string_wrong_ans = "'{}' is wrong answer ;(. Correct answer was '{}'".format(answer, correct_ans)
            print("Let's try again, {}!".format(name))
            sys.exit(0)

        #elif answer != correct_val:
         #   print(string_wrong_ans.format(answer, correct_val))
        


    print("Congratulations, {}!".format(name))


if __name__ == "__main__":
    None
