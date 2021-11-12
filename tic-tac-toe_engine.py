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
    chosen_mark = input("Choose mark for first player ('x' or 'o'):")
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

    print(f"Player 1 is playing '{player_1}' and Player 2 is playing '{player_2}'.")
    return player_1, player_2



def get_coordinates_from_player():
    """Ask current player for coordinates where he want to put his mark."""
    while True:
        input_text = f"{'Krzyżyk' if mark in ['x', 'X'] else 'Kółko'}: podaj współrzędne w formacie (y,x): "
        raw_input = input(input_text)

        if raw_input[0].isnumeric() and raw_input[-1].isnumeric():
            if int(raw_input[0]) >= 0 and int(raw_input[0]) <= 2 and int(raw_input[-1]) >= 0 and int(
                    raw_input[-1]) <= 2:
                break

    return (int(raw_input[0]), int(raw_input[-1]))


def put_item_on_board(board, coords: tuple, mark: str):
    if mark != 'o' and mark != 'x':
        return board, False

    if board[coords] != '.':
        return board, False

    board[coords] = mark

    return board, True


def check_if_game_over(board):
    for r in board:
        if all(r == 'x') or all(r == 'o'):
            return True

    for c in range(board.shape[1]):
        if all(board[:, c] == 'x') or all(board[:, c] == 'o'):
            return True

    if all(board.diagonal() == 'x') or all(board.diagonal() == 'o'):
        return True

    if all(np.fliplr(board).diagonal() == 'x') or all(np.fliplr(board).diagonal() == 'o'):
        return True

    return False


def start_tic_tac_toe():
    is_game_over = False
    is_success = False
    board = generate_board()
    turn = 0

    while is_game_over == False:
        coords = get_coordinates_from_player()
        put_item_on_board(board, coords, mark)
        check_if_game_over(board)
