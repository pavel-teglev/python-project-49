from random import randint


main_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def colculation():
  condtions = randint(0, 100)
  if condtions % 2 == 0:
    result = 'yes'
  else:
    result = 'no'
  return [condtions, result]
