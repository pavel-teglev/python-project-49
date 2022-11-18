from random import randint
import prompt


def brain_even():
  print('Welcome to the Brain Games!')
  name = prompt.string('May I have your name? ')
  print(f'Hello, {name}')
  print('Answer "yes" if the number is even, otherwise answer "no".')
  trys_count = 3
  while trys_count > 0:
    question = randint(0, 100)
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if (question % 2 == 0 and answer == 'yes') or (question % 2 != 0 and answer == 'no'):
      print('Correct!')
      trys_count -= 1
    elif question % 2 == 0 and answer != 'yes':
      print(f'"{answer}" is wrong answer ;(. Correct answer was "yes" \nLet\'s try again, {name}!')
    elif question % 2 != 0 and answer != 'no':
      print(f'"{answer}" is wrong answer ;(. Correct answer was "no" \nLet\'s try again, {name}!')
  print(f'Congratulations, {name}!')

brain_even()
