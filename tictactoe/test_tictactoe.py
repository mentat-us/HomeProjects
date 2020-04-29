import unittest
import tictactoe as ttt

class TicTacToeTestCase(unittest.TestCase):
    def test_tictactoe_by_colum_1(self):
        m = [[ttt.TILE_O, ttt.TILE_EMPTY, ttt.TILE_EMPTY],
             [ttt.TILE_O, ttt.TILE_EMPTY, ttt.TILE_EMPTY],
             [ttt.TILE_O, ttt.TILE_EMPTY, ttt.TILE_X]]
        self.assertEqual(True, ttt.is_tictactoe_by_colum(m))

    def test_tictactoe_by_colum_2(self):
        m = [[ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY]]
        self.assertEqual(False, ttt.is_tictactoe_by_colum(m))

    def test_tictactoe_by_row_1(self):
        m = [[ttt.TILE_O, ttt.TILE_O, ttt.TILE_O],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY]]
        self.assertEqual(True, ttt.is_tictactoe_by_row(m))

    def test_tictactoe_by_row_2(self):
        m = [[ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY]]
        self.assertEqual(False, ttt.is_tictactoe_by_row(m))

    def test_tictactoe_by_row_3(self):
        m = [[ttt.TILE_EMPTY, ttt.TILE_X, ttt.TILE_X],
             [ttt.TILE_O, ttt.TILE_O, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY]]
        self.assertEqual(False, ttt.is_tictactoe_by_row(m))

    def test_tictactoe_by_diagonal_1(self):
        m = [[ttt.TILE_O, ttt.TILE_X, ttt.TILE_X],
             [ttt.TILE_O, ttt.TILE_O, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_O]]
        self.assertEqual(True, ttt.is_tictactoe_by_diagonal(m))

    def test_tictactoe_by_diagonal_2(self):
        m = [[ttt.TILE_EMPTY, ttt.TILE_X, ttt.TILE_X],
             [ttt.TILE_O, ttt.TILE_O, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY]]
        self.assertEqual(False, ttt.is_tictactoe_by_diagonal(m))

    def test_tictactoe_by_reverse_diagonal_1(self):
        m = [[ttt.TILE_EMPTY, ttt.TILE_X, ttt.TILE_X],
             [ttt.TILE_O, ttt.TILE_X, ttt.TILE_EMPTY],
             [ttt.TILE_X, ttt.TILE_EMPTY, ttt.TILE_EMPTY]]
        self.assertEqual(True,ttt.is_tictactoe_by_reverse_diagonal(m))

    def test_tictactoe_by_reverse_diagonal_2(self):
        m = [[ttt.TILE_EMPTY, ttt.TILE_X, ttt.TILE_X],
             [ttt.TILE_O, ttt.TILE_O, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY]]
        self.assertEqual(False, ttt.is_tictactoe_by_reverse_diagonal(m))


    def test_tictactoe_1(self):
        m = [[ttt.TILE_EMPTY, ttt.TILE_X, ttt.TILE_X],
             [ttt.TILE_O, ttt.TILE_O, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY]]
        self.assertEqual(False, ttt.is_tictactoe(m))


    def test_tictactoe_2(self):
        m = [[ttt.TILE_EMPTY, ttt.TILE_X, ttt.TILE_X],
             [ttt.TILE_O, ttt.TILE_O, ttt.TILE_O],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_EMPTY]]
        self.assertEqual(True, ttt.is_tictactoe(m))

    def test_tictactoe_3(self):
        m = [[ttt.TILE_O, ttt.TILE_X, ttt.TILE_X],
             [ttt.TILE_EMPTY, ttt.TILE_O, ttt.TILE_EMPTY],
             [ttt.TILE_EMPTY, ttt.TILE_EMPTY, ttt.TILE_X]]
        self.assertEqual(False, ttt.is_tictactoe(m))

if __name__ == '__main__':
    unittest.main()
