from random import randint


MAIN_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def run_game():
    question = randint(0, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [question, correct_answer]
