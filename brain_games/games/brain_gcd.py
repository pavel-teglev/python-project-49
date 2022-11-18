from random import randint
import math

main_question = 'Find the greatest common divisor of given numbers.'

def colculation():
  first_number = randint(0, 100)
  second_number = randint(0, 100)
  condtions = f'{first_number} {second_number}'
  result = math.gcd(first_number, second_number)
  return [condtions, result]