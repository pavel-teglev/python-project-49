from random import randint

main_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculation():
    conditions = randint(1, 10000)
    result = 'yes'
    for i in range(2, (conditions // 2) + 1):
        if conditions % i == 0:
            result = 'no'
    return [conditions, result]
