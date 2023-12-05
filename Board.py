#code for the chess board

class Board():
    """
    A representation of a Chess board
    which can be updated with legal moves
    and detect if there is currently a winner.


    """
    SIZE = 8
    def __init__(self):
        """
        initialize the chess board to represent a standard
        starting chess position with pieces on both sides
        """
        self.board = [[' ' for i in range(self.SIZE)] for j in range(self.SIZE)]
        self.start_pos()
        
    
    def start_pos(self):
        """
        places the pieces on the board in 
        the standard starting position
        """
