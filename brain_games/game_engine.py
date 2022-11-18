import prompt
import brain_games.games.brain_calc as calc



def game_engine(game):
  print('Welcome to the Brain Games!')
  name = prompt.string('May I have your name? ')
  print(f'Hello, {name}')
  print(game.main_question)
  trys_count = 3
  while trys_count > 0:
    game_logic = game.colculation()
    question = game_logic[0]
    correct_answer = game_logic[1]
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if int(answer) == correct_answer:
      print('Correct!')
      trys_count -= 1
    elif int(answer) != correct_answer:
      print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}" \nLet\'s try again, {name}!')
  print(f'Congratulations, {name}!')

