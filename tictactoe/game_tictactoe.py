import tictactoe as ttt

def game_loop():
    board = ttt.init_board()

    counter = 0
    while True:
        if ttt.is_board_full(board) == True:
            print("Tie")
            break
        player = counter % 2
        ttt.print_board(board)
        try:
            player_row, player_colum = eval(input("Player " + str(player + 1) + " enter row and colum:"))
        except TypeError:
            continue
        player_row -= 1
        player_colum -= 1
        if ttt.is_playable(board, player_row, player_colum) == True:
            if player == 0:
                tile = ttt.TILE_X
            else:
                tile = ttt.TILE_O
            ttt.play_tile(board, player_row, player_colum, tile)
            counter += 1
        else:
            continue
        if ttt.is_tictactoe(board) == True:
            ttt.print_board(board)
            print("Player", str(player + 1), "win")
            break


def main():
    '''
    #tekrar oynamak isternisiniz
   start = time.time()
   '''
    game_loop()
    '''
    end = time.time()
    import  time
    time.time()
    "Player n bu karad kazandı , 2 kazan bu kada r beraberlik, süre gösterlim."
    "Ortalam oyun süresi, en uzun süren oyun, standart sapması nedir"
    '''


if __name__ == "__main__":
    main()