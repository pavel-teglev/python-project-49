from random import randint, choice

MAIN_QUESTION = 'What is the result of the expression?'


def make_calculation(first_operand, operator, second_operand):
    result = ''
    if operator == '*':
        result = first_operand * second_operand
    elif operator == '-':
        result = first_operand - second_operand
    elif operator == '+':
        result = first_operand + second_operand
    result = str(result)
    return [result]


def run_game():
    first_operand = randint(0, 100)
    second_operand = randint(0, 100)
    operator = choice(['*', '-', '+'])
    question = f'{first_operand} {operator} {second_operand}'
    correct_answer = make_calculation(first_operand, operator, second_operand)
    return [question, correct_answer]
