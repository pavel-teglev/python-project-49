from random import randint


main_question = 'What number is missing in the progression?'


def calculation():
    start = randint(1, 10)
    step = randint(1, 30)
    index = randint(0, 9)
    progression = [str(start)]
    parent = '..'
    counter = 9
    while counter > 0:
        start += step
        progression.append(str(start))
        counter -= 1
    result = progression[index]
    progression[index] = parent
    conditions = ' '.join(progression)
    return [conditions, result]
