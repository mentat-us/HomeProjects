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
            print(board[i][j], end=" | ")
        print()
        print(" ___", "___", "___")
        #print(" ___", "___", "___")    #üstteki print olmadığında bunu sola kaydırsam oluyordu.



def play_tile(board, r, c, tile):
    board[r][c] = tile


def is_tictactoe_by_row(board):
    for i in range(BOARD_SIZE):
        test = []
        test.append([])
        for j in range(BOARD_SIZE):
            test[i].append(board[i][j])   ### !!! test[j] ?
        control = 0
        for k in range(len(test) - 1):     ### aşağıdaki üçünde d ebunu aynı yaptım fonksiyona çeviriyim mi ?
            if test[k] == test[k + 1]:
                control += 1
        if control == 2:
            return True
    return False

def is_tictactoe_by_colum(board):
    for i in range(BOARD_SIZE):
        test = []
        test.append([])
        for j in range(BOARD_SIZE):
            test[j].append(board[j][i])   ### !!! test[i] ?
        control = 0
        for k in range(len(test) - 1):
            if test[k] == test[k + 1]:
                control += 1
        if control == 2:
            return True
    return False

def is_tictactoe_by_diagonal(board):
    test = []
    for i in range(BOARD_SIZE):
        test.append([])   #bir kere olucağına emin olduğum için içerde kontrol yapmadım
        for j in range(BOARD_SIZE):
            if i == j:
                test.append(board[i][j])
        control = 0
        for k in range(len(test) - 1):
            if test[k] == test[k + 1]:
                control += 1
        if control == 2:
            return True
    return False

def is_tictactoe_by_reverse_diagonal(board):
    test = []
    for i in range(BOARD_SIZE, 0, -1):
        test.append([])
        for j in range(BOARD_SIZE):
            if i == j:
                test.append(board[i][j])
        control = 0
        for k in range(len(test) - 1):
            if test[k] == test[k + 1]:
                control += 1
        if control == 2:
            return True
    return False


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




