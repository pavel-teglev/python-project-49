from random import randint


main_question = 'Find the greatest common divisor of given numbers.'


def colculation():
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
    condtions = ' '.join(progression)
    return [condtions, result]
