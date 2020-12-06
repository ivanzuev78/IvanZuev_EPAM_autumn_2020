from HomeWork_7.hw3 import tic_tac_toe_checker


def test_tic_tac_toe_checker_x_wins_in_row():
    board = [["x", "x", "x"], ["o", "x", "o"], ["x", "o", "o"]]
    assert tic_tac_toe_checker(board) == "x wins!"


def test_tic_tac_toe_checker_o_wins_in_col():
    board = [["o", "x", "x"], ["o", "x", "o"], ["o", "o", "x"]]

    assert tic_tac_toe_checker(board) == "o wins!"


def test_tic_tac_toe_checker_o_wins_in_diagonal():
    board = [["o", "x", "x"], ["x", "o", "o"], ["x", "x", "o"]]

    assert tic_tac_toe_checker(board) == "o wins!"


def test_tic_tac_toe_checker_draw():
    board = [["o", "o", "x"], ["x", "x", "o"], ["o", "x", "o"]]

    assert tic_tac_toe_checker(board) == "draw!"


def test_tic_tac_toe_checker_unfinished():
    board = [["o", "o", "x"], ["x", "-", "o"], ["o", "x", "o"]]
    assert tic_tac_toe_checker(board) == "unfinished"
