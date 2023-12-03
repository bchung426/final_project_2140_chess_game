#code for the chess pieces

class Piece():
    """
    A parent class for all the different chess pieces

    """
    black = "black"
    white = "white"
    def __init__(self,color):
        self.Color = color
        self.position = None
    
class Pawn(Piece):
    def __init__(self):
        super().__init__()
        if self.Color == self.white:
            self.direction = -1
        if self.Color == self.black:
            self.direction = 1

class Rook(Piece):
    def __init__(self):
        super().__init__()

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