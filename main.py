import random

# Constants for the players
HUMAN = -1
AI = 1

# Function to print the game board
def print_board(board):
    for row in board:
        print("|".join(str(cell) for cell in row))
        print("-----")

# Function to check if a player has won
def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for a tie
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        return "tie"

    # No winner
    return None

# Function to evaluate the score of the board
def evaluate(board):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    else:
        return 0

# Minimax function
def minimax(board, depth, is_maximizing):
    if check_winner(board) is not None:
        return evaluate(board)

    if is_maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = HUMAN
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Function to make the AI's move
def make_move(board):
    best_score = float("-inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = AI

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while check_winner(board) is None:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = HUMAN
        if check_winner(board) is not None:
            break
        make_move(board)
        print_board(board)
    winner = check_winner(board)
    if winner == "tie":
        print("It's a tie!")
    elif winner == HUMAN:
        print("You win!")
    elif winner == AI:
        print("You lose!")

# Start the game
play_game()
