from random import randint, choice

MAIN_QUESTION = 'What is the result of the expression?'


def make_calculation(first_operand, operator, second_operand):
    question = f'{first_operand} {operator} {second_operand}'
    if operator == '*':
        correct_answer = first_operand * second_operand
    elif operator == '-':
        correct_answer = first_operand - second_operand
    elif operator == '+':
        correct_answer = first_operand + second_operand
    correct_answer = str(correct_answer)
    return [question, correct_answer]


def run_game():
    first_operand = randint(0, 100)
    second_operand = randint(0, 100)
    operator = choice(['*', '-', '+'])
    return make_calculation(first_operand, operator, second_operand)
