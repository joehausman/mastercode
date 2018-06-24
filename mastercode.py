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

# checks for guesses that are the correct color and in the correct spot
# returns
def black_check(answer, guess):
    # print('ans: ' + str(answer))
    # print('gue: ' + str(guess))
    correct = 0
    i = 0
    while i < 4:
        if answer[i] == guess[i]:
            correct += 1
            answer[i] = 'X' # placeholder
            guess[i] = 'Y'  # different placeholder
        i += 1
    return correct, answer, guess


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
    # cb = str(correct_black)
    # cw = str(correct_white)
    # gu = ''.join(guess)
    print(CT + '|  |', end = '')

def print_checks(correct_black, correct_white):
    cb = str(correct_black)
    cw = str(correct_white)
    # print('_|' + cb + cw + '|____')
    print(' |' + cb + cw + '|    ')
    print('-|--|----')

# def print_row_start():
#     print(str(CURR_TURN) + '|', end = '')
#
# def print_row_end(correct_black, correct_white):
#     cb = str(correct_black)
#     cw = str(correct_white)
#     print('|' + cb + cw)

def print_code():
    global CODE
    print('\n     ' + ''.join(CODE) + ' <-- code\n')

def win_game():
    # @TODO: print win state thingy
    print_code()
    print('Well done!')
    exit(0)

def lose_game():
    print_code()
    # @TODO: print lose state thingy
    # @TODO: print sad message
    print('Better luck next time :(')
    exit(0)
#-----------------------------------------------------------
# @TODO: max turn choice (via args)

def setup():
    global CODE
    CODE = generate_code()
    # print_code()    # DEBUGGING
    print('-|BW|----')

def run():
    global CURR_TURN
    global MAX_TURNS
    while CURR_TURN < MAX_TURNS:
        global CODE
        answer = CODE.copy()
        # print_row_start()
        print_row()
        # print_code()    # DEBUGGING
        # @TODO: get player input
        # guess = generate_code()    # DEBUGGING
        # print(''.join(guess), end = '') # DEBUGGING
        guess = list(input())
        # print('\b\b', end = '') # remove trailing newline from input
        guess_copy = guess.copy()
        correct_black, answer, guess_copy = black_check(answer, guess_copy)
        if correct_black == 4:
            win_game()

        correct_white = white_check(answer, guess_copy)
        print_checks(correct_black, correct_white)
        # print_row(correct_black, correct_white, guess)
        # print_row_end(correct_black, correct_white)

        CURR_TURN += 1

    lose_game()

setup()
run()
