import chess_game
import unittest
"""
I do not know how many unit tests you would like but also I can't really add unit tests
for my Game class since basically all the Game methods require some user input
"""

class Board_test(unittest.TestCase):
    def test_positions(self):
        a = chess_game.Board()
        for i in range(8):
            for j in range(8):
                if a.board[i][j] == chess_game.Board.EMPTY:
                    self.assertEqual(a.board[i][j], chess_game.Board.EMPTY)
                else:
                    self.assertEqual(a.board[i][j].position, (i, j))
    def test_starting_pawns(self):
        a = chess_game.Board()
        for i in range(8):
            for j in range(8):
                if type(a.board[i][j]) == chess_game.Pawn:
                    if a.board[i][j].Color == chess_game.Pawn.white:
                        self.assertIn((i-2,j),a.board[i][j].available_moves(a.board))
                    elif a.board[i][j].Color == chess_game.Pawn.black:
                        self.assertIn((i+2,j), a.board[i][j].available_moves(a.board))
                    else:
                        pass
                else:
                    pass
class Piece_test(unittest.TestCase):
    def test_promotion(self):
        #checking the pawn promotion
        a = chess_game.Board()
        a.board[1][1] = chess_game.Pawn('white')
        a.update_pos()
        a.place_move((1, 1), (0, 0))
        self.assertEqual(type(a.board[0][0]), chess_game.Queen)
    def test_rook_start_protecting(self):
        a = chess_game.Board()
        self.assertEqual(set(a.board[7][0].protecting(a.board)), {(7, 1), (6, 0)})
    def test_start_cant_move(self):
        a = chess_game.Board()
        for i in a.board:
            for j in i:
                if j == a.EMPTY:
                    pass
                elif type(j) != chess_game.Pawn and type(j) != chess_game.Knight:
                    self.assertFalse(j.available_moves(a.board))
    
if __name__ == '__main__':
    unittest.main()
