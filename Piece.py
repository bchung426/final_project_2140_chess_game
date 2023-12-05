#code for the chess pieces

class Piece():
    """
    A parent class for all the different chess pieces

    All pieces have a color; either white or black

    Pieces have a position, which will be represented
    by a tuple of size 2, with both elements being the
    indices of the piece in an 8x8 matrix

    ex: the position for the starting white rook in the 'a' file will be
    represented by a tuple (7, 0) (row 7, column 0). When represented on the board, this
    will appear to be the column of index 0 (1) and the row of index 7 (1)

    """
    black = "black"
    white = "white"
    def __init__(self,color):
        self.Color = color
        self.position = None
    
    def find_moves(self, position, color, increments):
        """
        returns a list of moves that could be made
        given a position of a piece, the piece color,
        and the increments in which the piece moves

        increments is a list of tuples which will denote the
        different increments that a piece will be able to move in

        this function is only for pieces that can move an infinite 
        number of spaces (rook, bishop, queen) and will be redefined 
        for pieces like the king, knight, and pawn
        """
        row = position[0]
        file = position[1]
        for x, y in increments:
            for i in range(7):
                return 0




    
class Pawn(Piece):
    """
    Pawns can only move in one direction, which is based
    on what color they are.

    Pawns can only capture diagonally

    The first move for pawns can be either one or two
    squares forward.
    """
    def __init__(self,color):
        super().__init__()
        self.moves = 0
        """
        if self.Color == self.white:
            self.direction = -1
        if self.Color == self.black:
            self.direction = 1
        """

    def is_first_move(self):
        """
        returns either True or False depending on if the
        pawn has made a move yet
        """
        if self.moves < 1:
            return True
        else:
            return False
    
    def legal_move(self):
        """
        returns a list of legal squares where the pawn can move


        """
        move_list = []
        if self.Color == self.white:
            if self.is_first_move():
                for i in range(self.position[1] + 1, self.position[1] + 3):
                    move_list.append((self.position[0], i))
            else:
                move_list.append(self.position[0],self.position[1] + 1)
        if self.is_first_move():

            move_list.add()


class Rook(Piece):
    def __init__(self):
        super().__init__()
    def legal_move(self):
        move_list = []
        

class Knight(Piece):
    def __init__(self):
        super().__init__()

class Bishop(Piece):
    def __init__(self):
        super().__init__()

class King(Piece):
    def __init__(self):
        super().__init__()

class Queen(Piece):
    def __init__(self):
        super().__init__()