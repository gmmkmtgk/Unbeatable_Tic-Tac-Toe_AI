import random

# The game board is represented as a list of lists
# with each cell being empty (' '), 'X', or 'O'.
# The positions are numbered as follows:
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9

def print_board(board):
    print("---------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("---------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("---------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("---------")

def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def check_tie(board):
    return all(cell != ' ' for cell in board)

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

def minimax(board, depth, maximizing_player):
    scores = {'X': 1, 'O': -1, 'tie': 0}

    if check_win(board, 'X'):
        return scores['X']
    if check_win(board, 'O'):
        return scores['O']
    if check_tie(board):
        return scores['tie']

    if maximizing_player:
        max_score = float('-inf')
        for move in get_empty_cells(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            max_score = max(max_score, score)
        return max_score
    else:
        min_score = float('inf')
        for move in get_empty_cells(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            min_score = min(min_score, score)
        return min_score

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_empty_cells(board):
        board[move] = 'X'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = [' '] * 9
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        player_move = int(input("Enter your move (1-9): "))
        if board[player_move - 1] != ' ':
            print("Invalid move. Please try again.")
            continue
        board[player_move - 1] = 'O'
        if check_win(board, 'O'):
            print("You win!")
            break
        if check_tie(board):
            print("It's a tie!")
            break
        ai_move = get_best_move(board)
        board[ai_move] = 'X'
        print_board(board)
        if check_win(board, 'X'):
            print("AI wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

play_game()
