import numpy as np


def generate_board():
    """Creates a 3x3 board with labels A-C for columns and 1-3 for rows."""
    board = np.full((4, 4), '.')
    board[0] = [' ', 'A', 'B', 'C']
    board[1][0], board[2][0], board[3][0] = 1, 2, 3
    return board


def display_board(board):
    """Displays current state of the board to the players."""
    for row in board:
        print(row)


def select_mark():
    """Asks Player 1 to choose, whether he wants to play 'x' or 'o'. Also gives Player 2 remaining mark."""
    player_1_name = input("Please provide name for Player 1:")
    player_2_name = input("Please provide name for Player 2:")
    chosen_mark = input(f"{player_1_name} please choose a mark ('x' or 'o'):")
    if chosen_mark == 'x' or chosen_mark == 'o':
        if chosen_mark == 'x':
            player_1 = 'x'
            player_2 = 'o'
        else:
            player_1 = 'o'
            player_2 = 'x'
    else:
        print("Choose between 'x' and 'o' please.")
        select_mark()

    print(f"{player_1_name} is playing '{player_1}' and {player_2_name} is playing '{player_2}'.")
    return (player_1, player_1_name, player_2, player_2_name)


def current_player(move, player_1, player_1_name, player_2, player_2_name):
    """Determine which player is making a move."""
    if move%2 == 0:
        print(f"Current player: {player_1_name}")
        move += 1
        return player_1, player_1_name, move
    else:
        print(f"Current player: {player_2_name}")
        move += 1
        return player_2,player_2_name, move


def get_coordinates_from_player(board):
    """Ask current player for coordinates where he want to put his mark."""
    raw_input = input("Please specify coordinates for your mark (e.g. A1, C2 etc.):")
    if len(raw_input) == 2:
        if raw_input[0].upper() in ['A', 'B', 'C'] and int(raw_input[1]) in [1, 2, 3]:
            row = int(np.where(board == raw_input[1])[0])
            column = int(np.where(board == raw_input[0])[1])
        else:
            print("Something went wrong...")
            get_coordinates_from_player(board)
    else:
        print("Something went wrong...")
        get_coordinates_from_player(board)

    return (row, column)

def put_mark_on_board(board, coords, mark):
    """Puts current players mark on board. If given field is taken"""
    if board[coords] == '.':
        board[coords] = mark
        return board, True
    else:
        print("Sorry, this field is already taken. Try different coords.")
        return board, False

def check_if_game_over(board):
    """Checks if the game is finished based on current board state."""
    for row in board[1:, 1:]:
        if all(row == 'x') or all(row == 'o'):
            return True

    for row in board[1:, 1:].transpose():
        if all(row == 'x') or all(row == 'o'):
            return True

    if all(board[1:, 1:].diagonal() == 'x') or all(board[1:, 1:].diagonal() == 'o'):
        return True

    if all(np.fliplr(board[1:, 1:]).diagonal() == 'x') or all(np.fliplr(board[1:, 1:]).diagonal() == 'o'):
        return True

    return False

def play_game():
    """Starts a new game."""
    board = generate_board()
    display_board(board)
    player_1, player_1_name, player_2, player_2_name = select_mark()
    move = 0
    successful_mark = False
    is_game_over = False

    while is_game_over == False:
        display_board(board)
        player, player_name, move = current_player(move, player_1, player_1_name, player_2, player_2_name)
        while successful_mark == False:
            coords = get_coordinates_from_player(board)
            board, successful_mark = put_mark_on_board(board, coords, player)
        is_game_over, winner = check_if_game_over(board)

    winner = player_name
    return f"Game is over. {winner} won the game."