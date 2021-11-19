# TIC TAC TOE GAME

game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# game_board = [['1', '1', '3'], ['4', '5', '6'], ['7', '7', '7']]
marker = [[' ', 'v', ' '], [' ', '<', ' ']]
victory = 0
current_player = 'X'


def display(game_board):
    """Reprints the game board using the game_board and marker lists"""
    display_board = '\n'
    for h in marker[0]:
        display_board += h
        display_board += ' '
    display_board += '\n'
    for ridx, r in enumerate(game_board):
        for cidx, c in enumerate(r):
            display_board += c
            if cidx != 2:
                display_board += '|'
        display_board += marker[1][ridx]
        if ridx != 2:
            display_board += '\n-----\n'
    display_board += '\n'
    print(display_board)


def move(user_input):
    global current_player
    """Cycles the marker in the marker list based on user-input"""
    if user_input == 'a':
        marker[0].append(marker[0].pop(0))
    elif user_input == 'w':
        marker[1].append(marker[1].pop(0))
    elif user_input == 'd':
        marker[0].insert(0, marker[0].pop(2))
    elif user_input == 'x':
        marker[1].insert(0, marker[1].pop(2))
    elif user_input == 's':
        r = marker[1].index('<')
        c = marker[0].index('v')
        if game_board[r][c] == ' ':
            game_board[r][c] = current_player
            check_victory(game_board)
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print('That space is taken already!')


def check_victory(game_board):
    """Check for victory conditions"""
    global victory
    tie = True
    for ridx, r in enumerate(game_board):
        if len(set(r)) == 1 and ' ' not in set(r):
            victory = 1
            break
        column = []
        for cidx, c in enumerate(r):
            column.append(game_board[cidx][ridx])
            if game_board[ridx][cidx] == ' ':
                tie = False
        if len(set(column)) == 1 and ' ' not in set(column):
            victory = 1
            break
    if not victory:
        diag1 = []
        diag2 = []
        for n in range(3):
            diag1.append(game_board[n][n])
            diag2.append(game_board[n][2-n])
        if len(set(diag1)) == 1 and ' ' not in set(diag1):
            victory = 1
        if len(set(diag2)) == 1 and ' ' not in set(diag2):
            victory = 1
    if victory == 1:
        print(f'Winner is the {current_player} player!')
    elif tie:
        print('There is a tie!')


def user_choice():
    """Asks for user input"""
    choice = ''
    while choice not in ['a', 'w', 'd', 'x', 's']:
        choice = input('W, A, D, X to move marker. S to place piece.\n').lower()
        if choice not in ['a', 'w', 'd', 'x', 's']:
            print('That is not an accepted button!')
    return choice


while victory == 0:
    display(game_board)
    move(user_choice())

