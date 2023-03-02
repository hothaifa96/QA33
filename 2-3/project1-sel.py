import random

board = [['always', 'be ', 'yourself'],
         ['keep', 'it', 'cool'],
         ['man', 'it', 'cool'],
         ['keep', 'eliran', 'cool'],
         ['keep', 'it', 'cool'],
         ['maksom', 'it', 'noy'],
         ['keep', 'it', 'cool'],
         ['keep', 'nir', 'cool'],
         ['use', 'it', 'tachanka'],
         ['aaaaa', 'it', 'fort']]

rnd = random.randint(0, 9)

# generating the guess board
origin = board[rnd]
guesses = []
for word in origin:
    w = ''
    for letter in word:
        w += '_'
    guesses.append(w)

flag = True

while flag:
    user_input = input('please enter your guess')
    for word in range(len(origin)):
        for letter in origin[word]:
            origin[word] = origin[word].replace(user_input, '_')

    for i in range(len(origin)):
        w=guesses[i]
        for j in range(len(origin[i])):
            if guesses[i][j] == '_' and origin[i][j] == '_':
                print('yeah')
                w = w[:j]+user_input+w[j+1:]
        guesses[i] = w
    print(guesses)

    flag = [x for x in guesses if '_'  in x ]

print('nice')
