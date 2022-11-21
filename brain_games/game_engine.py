import prompt


def game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.main_question)
    try_count = 3
    while try_count > 0:
        game_logic = game.colculation()
        question = game_logic[0]
        correct_answer = game_logic[1]
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            try_count -= 1
        elif answer != correct_answer:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}" '
                  f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
