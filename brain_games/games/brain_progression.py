from random import randint


CONDITIONS = 'What number is missing in the progression?'


def make_progression(start, step):
    progression = [str(start)]
    counter = 9
    while counter > 0:
        start += step
        progression.append(str(start))
        counter -= 1
    return progression


def get_game():
    start = randint(1, 10)
    step = randint(1, 30)
    progression = make_progression(start, step)
    parent_index = randint(0, 9)
    parent = '..'
    correct_answer = progression[parent_index]
    progression[parent_index] = parent
    question = ' '.join(progression)

    return [question, correct_answer]
