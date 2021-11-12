import numpy as np
from IPython.display import clear_output


def generate_board():
    board = np.full((3, 3), '.')
    return board


def get_coordinates_from_player(mark):
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