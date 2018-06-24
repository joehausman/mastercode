import random

MAX_TURNS = 10
CODECHARS = 'ABCDEF'

CODE = ''

def generate_code():
    return random.choice(CODECHARS)

# checks for guesses that are the correct color and in the correct spot
# returns
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


def white_check(answer, guess):
    correct = 0
    i = 0
    # count = 0   # DEBUGGING
    # outercount = 0  # DEBUGGING
    while i < 4:
        j = 0
        # outercount += 1 # DEBUGGING
        while j < 4:
            # print('a[i]: ' + answer[i] + ' g[j]: ' + guess[j]) # DEBUGGING
            # count += 1  # DEBUGGING
            if answer[i] == guess[j]:
                correct += 1
                answer[i] = 'X' # placeholder
                guess[j] = 'Y'  # different placeholder
            j += 1
        i += 1
    # print(count)    # DEBUGGING
    # print(outercount)   # DEBUGGING
    return correct

#-----------------------------------------------------------
# @TODO: max turn choice (via args)

# CODE = generate_code()
#
#
#
# correct_black, answer, guess = black_check(answer, guess)
# if correct_black == 4:
#     win_game()
#
# correct_white = white_check(answer, guess)
