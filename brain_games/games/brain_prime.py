from random import randint


main_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def colculation():
  condtions = randint(1, 10000)
  for i in range(2, (condtions//2)+1):
        if condtions % i == 0:
          result = 'no'
        else:
          result = 'yes'
  return [condtions, result]
