import random
board = [" " for _ in range(9)]
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def check_draw(board):
    return " " not in board
def minimax(board, player):
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]

    # Check for terminal states (win, lose, draw)
    if check_win(board, "O"):
        return {"score": 1}
    elif check_win(board, "X"):
        return {"score": -1}
    elif len(empty_cells) == 0:
        return {"score": 0}
    moves = []
    for cell in empty_cells:
        move = {}
        move["index"] = cell
        board[cell] = player

        if player == "O":
            result = minimax(board, "X")
            move["score"] = result["score"]
        else:
            result = minimax(board, "O")
            move["score"] = result["score"]

        board[cell] = " "
        moves.append(move)
    if player == "O":
        best_move = max(moves, key=lambda x: x["score"])
    else:
        best_move = min(moves, key=lambda x: x["score"])

    return best_move

current_player = "X"
game_over = False

while not game_over:
    display_board(board)

    if current_player == "X":
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move < 9 and board[move] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")
        board[move] = "X"
    else:
        # AI's turn
        print("AI's turn (O)")
        best_move = minimax(board, "O")
        board[best_move["index"]] = "O"

    if check_win(board, current_player):
        display_board(board)
        print(f"Player {current_player} wins!")
        game_over = True
    elif check_draw(board):
        display_board(board)
        print("It's a draw!")
        game_over = True
    else:
        current_player = "O" if current_player == "X" else "X"
