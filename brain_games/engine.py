import prompt
NUM_ITER = 3


def start_game(game):

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print(game.GREETING)
    for _ in range(NUM_ITER):
        question, corct_ans = game.generate_round()
        print("Question: {}".format(question))
        ans = prompt.string("Your answer: ")

        if ans == corct_ans:
            print("Correct!")
        elif ans != corct_ans:
            txt = "'{}' is wrong answer ;(. Correct answer was '{}'"
            print(txt.format(ans, corct_ans))
            print("Let's try again, {}!".format(name))
            return

    print("Congratulations, {}!".format(name))
