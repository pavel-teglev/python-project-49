from random import randint


main_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculation():
    conditions = randint(0, 100)
    if conditions % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return [conditions, result]
