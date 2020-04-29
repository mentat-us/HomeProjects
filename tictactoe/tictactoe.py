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
    print(" ___", "___", "___")
    for i in range(BOARD_SIZE):
        print("| ", end="")
        for j in range(BOARD_SIZE):
            if board[i][j] == TILE_EMPTY:
                print(" ", end=" | ")
            elif board[i][j] == TILE_X:
                print("X", end=" | ")
            else:
                print("O", end=" | ")

        print()
        print(" ___", "___", "___")
        #print(" ___", "___", "___")    #üstteki print olmadığında bunu sola kaydırsam oluyordu.



def play_tile(board, r, c, tile):
    board[r][c] = tile

def __is_empty(test):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if test[i][j] != TILE_EMPTY:
                return False
    return True

def control(test):
    for i in range(len(test)):
        o_counter = 0
        x_counter = 0
        for j in range(len(test[i])):
            if test[i][j] == TILE_O:
                o_counter += 1
            elif test[i][j] == TILE_X:
                x_counter += 1

        if o_counter == BOARD_SIZE or x_counter == BOARD_SIZE:
            return True

    return False

def is_tictactoe_by_row(board):
    test = []
    for i in range(BOARD_SIZE):
        test.append([])

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            test[i].append(board[i][j])   ### !!! test[j] ?
    return control(test)

def is_tictactoe_by_colum(board):
    test = []
    for k in range(BOARD_SIZE):
        test.append([])

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            test[i].append(board[j][i])   ### !!! test[i] ?


    return control(test)

def is_tictactoe_by_diagonal(board):
    test_r = []

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if i == j:
                test_r.append(board[i][j])

    test = []
    test.append(test_r)
    for k in range(1, BOARD_SIZE):
       test.append([])
    return control(test)

def is_tictactoe_by_reverse_diagonal(board):
    test_r = []
    for i in range(BOARD_SIZE):
       test_r.append(board[i][BOARD_SIZE - i - 1])

    test = []
    test.append(test_r)
    for k in range(1, BOARD_SIZE):
        test.append([])
    return control(test)

def is_tictactoe(board):
    """

    :param board:
    :return: bool
    """
    t_1 = is_tictactoe_by_row(board)
    t_2 = is_tictactoe_by_colum(board)
    t_3 = is_tictactoe_by_diagonal(board)
    t_4 = is_tictactoe_by_reverse_diagonal(board)
    if t_1 == True or t_2 == True or t_3 == True or t_4 == True:
        return True
    else:
        return False


def is_playable(board, r, c):
    """

    :param board:
    :return:
    """
    if (r < 0 or r > BOARD_SIZE - 1 or c < 0 or c > BOARD_SIZE - 1):
        return False
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




