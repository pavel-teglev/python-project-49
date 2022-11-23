from random import randint
import math


CONDITIONS = 'Find the greatest common divisor of given numbers.'


def get_game():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    question = f'{first_number} {second_number}'
    correct_answer = math.gcd(first_number, second_number)
    correct_answer = str(correct_answer)
    return [question, correct_answer]
