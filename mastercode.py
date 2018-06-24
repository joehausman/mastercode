import random

MAX_TURNS = 10
CURR_TURN = 0
CODECHARS = 'ABCDEF'

CODE = []

def generate_code():
    rand = []
    i = 0
    while i < 4:
        rand.append(random.choice(CODECHARS))
        i += 1
    return rand


# checks for guesses that are the correct color and position
# returns number of correct guesses
# inserts placeholders to prevent future matches in white_check()
def black_check(answer, guess):
    correct = 0
    i = 0
    while i < 4:
        if answer[i] == guess[i]:
            correct += 1
            answer[i] = 'X' # placeholder
            guess[i] = 'Y'  # different placeholder
        i += 1
    return correct, answer, guess

# checks for guesses that are correct in color only
# assumes anything found by black_check() was replaced by placeholders
def white_check(answer, guess):
    correct = 0
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            if answer[i] == guess[j]:
                correct += 1
                answer[i] = 'X' # placeholder
                guess[j] = 'Y'  # different placeholder
            j += 1
        i += 1
    return correct


def print_row():
    CT = str(CURR_TURN)
    print(CT + '|  |', end = '')

def print_checks(correct_black, correct_white):
    cb = str(correct_black)
    cw = str(correct_white)
    print(' |' + cb + cw + '|    ')
    print('-|--|----')

def print_code():
    global CODE
    print('\n     ' + ''.join(CODE) + ' <-- code\n')

def win_game():
    print_code()
    print('Well done!')
    exit(0)

def lose_game():
    print_code()
    print('Better luck next time :(')
    exit(0)


def setup():
    # @TODO: max turn choice (via args)
    # @TODO: instructions / help
    global CODE
    CODE = generate_code()
    print('-|BW|----')

def run():
    global CURR_TURN
    global MAX_TURNS
    while CURR_TURN < MAX_TURNS:
        global CODE
        answer = CODE.copy()
        print_row()
        guess = list(input())
        guess_copy = guess.copy()
        correct_black, answer, guess_copy = black_check(answer, guess_copy)
        if correct_black == 4:
            win_game()

        correct_white = white_check(answer, guess_copy)
        print_checks(correct_black, correct_white)
        CURR_TURN += 1

    lose_game()

setup()
run()
