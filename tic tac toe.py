# tic tac toe
# display greeting
import random
print("Welcome to Tic Tac Toe!")
# pick random X or O and assign to player
player = random.choice(["X", "O"])
turn = "O"
# assign the computer the other symbol
if player == "X":
    computer = "O"
else:
    computer = "X"

print("You are " + player)

# create a board with numbers 1-9
board = [" "] * 10

# display the board


def display_board(board):
    print("\n")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("----------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("----------")
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("\n")

# region Check Board
# region Check Win


def win(board, player):
    # check rows
    row_winner = check_rows(board, player)
    # check columns
    column_winner = check_columns(board, player)
    # check diagonals
    diagonal_winner = check_diagonals(board, player)
    if row_winner:
        return True
    elif column_winner:
        return True
    elif diagonal_winner:
        return True
    else:
        return False


def check_rows(board, player):
    # check if any of the rows have all the same value
    if board[1] == board[2] == board[3] == player:
        return True
    elif board[4] == board[5] == board[6] == player:
        return True
    elif board[7] == board[8] == board[9] == player:
        return True
    else:
        return False


def check_columns(board, player):
    # check if any of the columns have all the same value
    if board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[3] == board[6] == board[9] == player:
        return True
    else:
        return False


def check_diagonals(board, player):
    # check if any of the diagonals have all the same value
    if board[1] == board[5] == board[9] == player:
        return True
    elif board[3] == board[5] == board[7] == player:
        return True
    else:
        return False
# endregion
# region Check Fill


def full(board):
    # check if the board is full
    if " " in board:
        return False
    else:
        return True
# endregion
# endregion


display_board(board)
while True:

    # display the board
    display_board(board)

    # check if the player has won
    if win(board, player):
        print("Congratulations! You have won!")
        break
    # check if the board is full
    if full(board):
        print("The game is a tie!")
        break
    if turn == player:
        # ask the user where they want to place 1-9 starting top-left
        #if the space is empty, place the player's symbol
        #if the space is not empty, ask the user to choose another space
        position = int(input("Choose a position 1-9: "))
        if board[position] == " ":
            board[position] = player
        else:
            print("That space is taken. Please choose another.")
            continue
        # assign the position to the board
        board[position] = player
        # switch turns
        turn = computer
    else:
        # assign the computer to a random position
        # if the position is already taken, assign the computer to a random position
        position = random.randint(1, 9)
        while board[position] != " ":
            position = random.randint(1, 9)
        board[position] = computer
        # switch turns
        turn = player
