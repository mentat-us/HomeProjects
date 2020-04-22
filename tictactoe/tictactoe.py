TILE_EMPTY = 0
TILE_X = 1
TILE_O = 2

BOARD_SIZE = 3

board = None


def init_board():
    """
    list of list
    creates a board and returns
    :return: 3x3 matrix
    """
    global board
    if board: #none değilse
        return board
    board = []
    for i in range(BOARD_SIZE):
        board.append([])
        for j in range(BOARD_SIZE):
            board[i].append(TILE_EMPTY)
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
    print(board)



def play_tile(board, r, c, tile):
    board[r][c] = tile


def is_tictactoe(board):
    """

    :param board:
    :return: bool
    """
    pass

def is_playable(board, r, c):
    """

    :param board:
    :return:
    """
    if board[r][c] == TILE_EMPTY:
        return True
    else:
        return False
    #return board[r][c] == TILE_EMPTY

def is_board_full(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == TILE_EMPTY:
                return False
    return True




