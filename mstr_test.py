import mastercode
black_check = mastercode.black_check
white_check = mastercode.white_check

answer = ['A','B','C','D']
guess = ['A','D','C','A']

def bc_test(answer, guess):
    print('\nblack_check test--------')
    correct, answer, guess = black_check(answer, guess)
    print('cor: ' + str(correct))
    print('ans: ' + str(answer))
    print('gus: ' + str(guess))
    return answer, guess

def wc_test(answer, guess):
    # print('\nans: ' + str(answer))
    # print('gus: ' + str(guess))
    print('\nwhite_check test--------')
    correct = white_check(answer, guess)
    print('cor: ' + str(correct))

answer, guess = bc_test(answer, guess)
wc_test(answer, guess)
