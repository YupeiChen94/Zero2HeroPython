from random import shuffle

myList = [' ', 'O', ' ']


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in map(str, list(range(3))):
        guess = input("Pick a number: 0, 1, or 2\n")
    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(mylist)


# SHUFFLE LIST
mixedup_list = shuffle_list(myList)
# PROMPT FOR USER GUESS
guess = player_guess()
# CHECK USER GUESS
check_guess(mixedup_list, guess)
