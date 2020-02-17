
# ---------------------------Board----------------------------------
# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad,
# so you get a 3 by 3 board representation.


import random


def greeting():
    print('Welcome to TIC TAC TOE')


def display_board(board):
    print('\n' * 3)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


# ---------------------------players----------------------------------
# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.


def player_input():

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O \n').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# ---------------------------Board Positions----------------------------------
# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board, "X", 8)
# display_board(test_board)

# ---------------------------Checking----------------------------------
# Step 4: Write a function that takes in a board and checks to see if someone has won.


def win_check(board, marker):

    # check all ROWS, and check if they share the same markers

    if((board[7] == marker and board[8] == marker and board[9] == marker) or
        (board[4] == marker and board[5] == marker and board[6] == marker) or
        (board[1] == marker and board[2] == marker and board[3] == marker) or
        # check all COLUMNS, and check if they share the same markers
        (board[3] == marker and board[6] == marker and board[9] == marker) or
        (board[2] == marker and board[5] == marker and board[8] == marker) or
        (board[1] == marker and board[4] == marker and board[7] == marker) or
        # check DIAGONALS, and check if they share the same markers
        (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[7] == marker and board[5] == marker and board[3] == marker)):
        return True
    else:
        return False


# win_check(test_board, "O")


# ---------------------------Selecting player Randomly----------------------------------
# Step 5: Write a function that uses the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'player 1'
    else:
        return'player 2'


# choose_first()

# ---------------------------Checking for free spaces on board----------------------------------
# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.


def space_check(board, position):
    if board[position] == ' ':
        return True

# ---------------------------Checking if Board is full----------------------------------
# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# ---------------------------Asking for next position----------------------------------
# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position.
# If it is, then return the position for later use.

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position

# ---------------------------PLay again?----------------------------------
# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.


def replay():
    choice = input('Would you like to play again?\n Enter yes or no\n')
    return choice == 'yes'


# ---------------------------Building the logic tu run the game----------------------------------

greeting()

# 1- While loop to keep runing the game
while True:

    # PLay the game

    # Sey everything up (Board, whos first, choose markers (X, O))
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? \n')

    if play_game[0] == 'y':
        game_on = True
    else:
        game_on = False

    # Game play
    while game_on:

        # PLayer one turn
        if turn == 'player 1':
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)

            # PLace the marker on the position
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!!')
                game_on = False

            # Or check if theres is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('THERE IS A TIE')
                    game_on = False
                else:
                    turn = 'player 2'

        # PLayer two turn
        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)

            # PLace the marker on the position
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!!!')
                game_on = False

            # Or check if theres is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('THERE IS A TIE')
                    game_on = False
                else:
                    turn = 'player 1'
            # Break out of the while loop on replay()

    if not replay():
        break
