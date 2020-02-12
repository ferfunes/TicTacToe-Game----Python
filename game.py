
# ---------------------------Board----------------------------------
# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad,
# so you get a 3 by 3 board representation.

the_board = [''] * 10


def board():
    print(the_board[7] + '|' + the_board[8] + '|' + the_board[9])
    print(the_board[4] + '|' + the_board[5] + '|' + the_board[6])
    print(the_board[1] + '|' + the_board[2] + '|' + the_board[3])


# ---------------------------players----------------------------------
# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.


def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O \n')

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print('player 1 is ' + player1 + ',' + ' player 2 is ' + player2)


player_input()
board()
