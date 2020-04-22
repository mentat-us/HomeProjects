import tictactoe as ttt

import math
import time

def _check_bounds(r, c):
    if r < 0 or r >= ttt.BOARD_SIZE or c < 0 or c >= ttt.BOARD_SIZE:
        return False
    return True

def game_loop():
    board = ttt.get_board()
    player_counter = 0
    while True:
        player = player_counter % 2 + 1

        if ttt.is_board_full(board):
            ttt.print_board(board)
            print("Tie")
            break

        ttt.print_board(board)
        try:
            r, c = input("Player" + str(player) + "-> r, c").split()
            r, c = int(r) - 1, int(c) - 1
        except ValueError:
            print("Player", str(player), "Invalid Row Column Format \nExample input for row 1 and column 2 is: 1 2")
            continue
        if not _check_bounds(r, c):
            print("Player", str(player),  "Invalid Position")
            continue
        if not ttt.is_playable(board, r, c):
            print("Player", str(player), "Position already filled")
            continue

        ttt.play_tile(board, r, c, ttt.TILE_X if player == 1 else ttt.TILE_O)

        if ttt.is_tictactoe(board):
            ttt.print_board(board)
            print("Player",  player,  "wins")
            break

        player_counter += 1

    ttt.clear_board(board)

    return player


def _convert_min_sec(_time):
    _time = math.floor(_time)
    min = _time // 60
    sec = _time % 60
    return min, sec

def display_statistics(round_count, p1, start_time, end_time):
    min_sec = _convert_min_sec(end_time - start_time)
    print("{} round played, Player 1 wins {} times, Player 2 wins {} times, Game duration {:02d} min : {:02d} sec "
          .format(round_count, p1, round_count - p1, min_sec[0], min_sec[1]))



def main():
    p1 = 0
    round_count = 0
    start_time = time.time()
    while True:
        round_count += 1
        winner = game_loop()
        if winner == 1:
            p1 += 1

        str = input("Do you wat to play one more round [yes or no]").strip().lower()
        if not str == "yes":
            break
    end_time = time.time()

    display_statistics(round_count, p1, start_time, end_time)



if __name__ == "__main__":
    main()