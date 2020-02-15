
# ---------------------------Board----------------------------------
# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad,
# so you get a 3 by 3 board representation.


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

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O \n').upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print('player 1 is ' + player1 + ',' + ' player 2 is ' + player2)


player_input()


# ---------------------------Board Positions----------------------------------
# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.


def place_marker(board, marker, position):
    board[position] = marker


place_marker(test_board, 'X', 8)
display_board(test_board)

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
        print("True")
    else:
        print("False")


win_check(test_board, 'O')
