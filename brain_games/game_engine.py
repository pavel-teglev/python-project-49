import prompt


def game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.MAIN_QUESTION)
    try_count = 3
    while try_count > 0:
        question, correct_answer = game.run_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            try_count -= 1
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}"'
                f'\nLet\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
