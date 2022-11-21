from random import randint

main_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def colculation():
    condtions = randint(1, 10000)
    result = 'yes'
    for i in range(2, (condtions // 2) + 1):
        if condtions % i == 0:
            result = 'no'
    return [condtions, result]
