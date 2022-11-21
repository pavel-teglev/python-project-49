from random import randint


MAIN_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    result = True
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            result = False
    return result


def run_game():
    question = randint(1, 10000)
    correct_answer = 'no'
    if is_prime(question):
        correct_answer = 'yes'
    return [question, correct_answer]
