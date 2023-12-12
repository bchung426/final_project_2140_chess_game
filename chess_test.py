import chess_game
import unittest

class chess_test(unittest.TestCase):
    def test_pos(self):
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
                
    

    """
    def test_unique_id(self):
        b1 = BankAccountTester.mkBA()
        b2 = BankAccountTester.mkBA()
        self.assertNotEqual(b1.getAccountId(), b2.getAccountId())
        """

if __name__ == '__main__':
    unittest.main()
