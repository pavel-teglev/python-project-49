from random import randint, choice

main_question = 'What is the result of the expression?'

def colculation():
  first_operand = randint(0, 100)
  second_operand = randint(0, 100)
  operator = choice(['*', '-', '+'])
  condtions = f'{first_operand} {operator} {second_operand}'
  if operator == '*':
    result = first_operand * second_operand
  elif operator == '-':
    result = first_operand - second_operand
  elif operator == '+':
    result = first_operand + second_operand
  return [condtions, result]

