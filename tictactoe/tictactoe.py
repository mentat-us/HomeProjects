TILE_EMPTY = 0
TILE_X = 1
TILE_O = 2

BOARD_SIZE = 5

board = None

def get_board():
    """
    list of list
    creates a board and returns
    :return: 3x3 matrix
    """
    global board
    if board is not None:
        return board

    board = []
    for i in range(BOARD_SIZE):
        row = []
        for j in range(BOARD_SIZE):
            row.append(TILE_EMPTY)
        board.append(row)

    return board


def clear_board(board):
    """
    sets the elemnet TILE_EMPTY
    :param m: (list of list) board
    :return: None
    """
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            board[i][j] = TILE_EMPTY

def _disp_und_scr_line():
    print("  ", 12 * "_", sep="")


def print_board(board):
    """
    display board
     __ __ __
    |__|__|__|
     __ __ __
    |__|__|__|
     __ __ __
    |__|__|__|

    :param m:
    :return:
    """
    print(4 * " ", 1, 2 * " ", 2, 3 * " ", 3, sep="")
    _disp_und_scr_line()
    for i in range(BOARD_SIZE):
        print(i + 1, sep="", end="")
        for j in range(BOARD_SIZE):
            if board[i][j] == TILE_X:
                dis_ch = "X"
            elif board[i][j] == TILE_O:
                dis_ch = "O"
            else:
                dis_ch = " "
            print(format("|", "1s"), " ", dis_ch, " ", sep="", end="")

        print(format("|", "2s"), sep="")
        _disp_und_scr_line()




def play_tile(board, r, c, tile):
    board[r][c] = tile




def _check_cols(board):
    for row in range(BOARD_SIZE):
        x_counter = 0
        o_counter = 0
        for col in range(BOARD_SIZE):
            if board[row][col] == TILE_X:
                x_counter += 1
            if board[row][col] == TILE_O:
                o_counter += 1

        if x_counter == BOARD_SIZE or o_counter == BOARD_SIZE:
            return True

    return False


def _check_rows(board):

    for col in range(BOARD_SIZE):
        x_counter = 0
        o_counter = 0
        for row in range(BOARD_SIZE):
            if board[row][col] == TILE_X:
                x_counter += 1
            if board[row][col] == TILE_O:
                o_counter += 1

        if x_counter == BOARD_SIZE or o_counter == BOARD_SIZE:
            return True

    return False


def _check_diagonal(board):
    x_counter = 0
    o_counter = 0
    for i in range(BOARD_SIZE):
        if board[i][i] == TILE_X:
            x_counter += 1
        if board[i][i] == TILE_O:
            o_counter += 1

    return x_counter == BOARD_SIZE or o_counter == BOARD_SIZE

def _check_anti_diagonal(board):
    x_counter = 0
    o_counter = 0
    for i in range(BOARD_SIZE):
        if board[i][BOARD_SIZE - i - 1] == TILE_X:
            x_counter += 1
        if board[i][BOARD_SIZE - i - 1] == TILE_O:
            o_counter += 1

    return x_counter == BOARD_SIZE or o_counter == BOARD_SIZE


def is_tictactoe(board):
    """

    :param board:
    :return: bool
    """
    return _check_cols(board) or \
           _check_rows(board) or \
           _check_diagonal(board) or \
           _check_anti_diagonal(board)


def is_playable(board, r, c):
    """

    :param board:
    :return: bool
    """
    return board[r][c] is TILE_EMPTY

def is_board_full(board):
    for rows in board:
        if rows.count(TILE_EMPTY) > 0:
            return False

    return True

