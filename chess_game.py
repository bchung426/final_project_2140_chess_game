#code for the chess pieces

class Board():
    """
    A representation of a Chess board
    which can be updated with legal moves
    and detect if there is currently a winner.


    """

    SIZE = 8
    EMPTY = ''
    files = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
    def __init__(self):
        """
        initialize the chess board to represent a standard
        starting chess position with pieces on both sides
        """
        self.board = [['' for i in range(self.SIZE)] for j in range(self.SIZE)]
        self.start_pos()
    
    def print_board(self):
        """
        prints the chess board along with the labeled rows and files

        the board is printed from a point of view of the player using
        the white pieces (white starting position will always appear at the bottom)

        used basically the same stuff from the tictactoe; added stuff in to get 
        the row/file labels as well as increased the spacing between rows b/c the spacing with
        the chess piece characters are muy interesante 
        """
        #initial line of space
        self.show = '\n'
        #♚ ♔ ♖ ♜ ♝ ♗ ♛ ♕ ♞ ♘ ♟ ♙ 
        """   put in README maybe! :
        the pieces_w used "black pieces" but since the background of vscode is black, the "white pieces"
        appear black since they are just a hollow outline of the piece, so the terminal you are using
        might make these look different   """
        self.pieces_w = {Pawn:'♟ ', Rook:'♜ ', Knight:'♞ ', Bishop:'♝ ', King:'♚ ', Queen:'♛ '}
        self.pieces_b = {Pawn:'♙ ', Rook:'♖ ', Knight:'♘ ', Bishop:'♗ ', King:'♔ ', Queen:'♕ '}
        for i in range(self.SIZE):
            #adding the row number labels for the board
            self.show += str(8-i) + " "
            for j in range(self.SIZE):
                if self.board[i][j] == self.EMPTY:
                    self.show += "[  ] " 
                    #formatting so that the empty squares will take up the same amount of space as
                    #the squares with pieces in them, so the formatting doesn't hurt ur eyes and brain
                else:
                    if self.board[i][j].Color == Piece.white:
                        self.show += "[" + self.pieces_w[type(self.board[i][j])] + "] "
                    if self.board[i][j].Color == Piece.black:
                        self.show += "[" + self.pieces_b[type(self.board[i][j])] + "] "
            if i == 7:
                self.show += "\n"
            else: 
                #using only one '\n' made the board look very clumped - a mi no me gusta
                self.show += "\n\n"
        #adding the labels for the files of the board
        for i in range(1,9):
            self.show += "   " + self.files[i] + " "
        print(self.show)

    
    def start_pos(self):
        """
        places the pieces on the board in 
        the standard starting position
        """
        spec_pieces = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        for i in range(self.SIZE):
            #pawns
            self.board[1][i] = Pawn(Pawn.black)
            self.board[6][i] = Pawn(Pawn.white)
            #other pieces
            self.board[0][i] = spec_pieces[i](Piece.black)
            self.board[7][i] = spec_pieces[i](Piece.white)
        #self.board[4][1] = Knight(Knight.white) #line i test methods for pieces with
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j] == self.EMPTY:
                    pass
                else:
                    self.board[i][j].position = (i, j)


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
    def __init__(self,color = "white"):
        self.Color = color
        self.position = None
    
    def find_moves(self, position, color, increments, board):
        """
        returns a list of moves that could be made
        given a position of a piece, the piece color,
        and the increments in which the piece moves

        increments is a list of tuples which will denote the
        different increments that a piece will be able to move in

        this function is only for pieces that can move an infinite 
        number of spaces (rook, bishop, queen)
        """
        row = position[0]
        file = position[1]
        move_list = []
        for x, y in increments:
            curr_row = row + x
            curr_file = file + y
            for i in range(7):
                if curr_row > 7 or curr_file > 7 or curr_row < 0 or curr_file < 0:
                    #any of these values would result in  an illegal move since the 
                    # piece would no longer be on the board, so shouldn't add it to 
                    # the list of moves; also the increments would continue moving in
                    # the direction to be off the board, so should also stop 
                    # the current increment values
                    break
                if board[curr_row][curr_file] == Board.EMPTY:
                    #if there is no piece in the location, should add
                    # the location to the move list
                    move_list.append((curr_row,curr_file))
                
                #if it runs into a piece of the opposite color, adds the 
                #square to the move list and goes to the next increment
                elif board[curr_row][curr_file].Color != color:
                    move_list.append((curr_row,curr_file))
                    break
                #if it runs into a piece of the same color, 
                #goes to the next increment w/o adding the move
                elif board[curr_row][curr_file].Color == color:
                    break
                #increments
                curr_row += x 
                curr_file += y
        return move_list




    
class Pawn(Piece):
    """
    Pawns can only move in one direction, which is based
    on what color they are.

    Pawns can only capture diagonally

    The first move for pawns can be either one or two
    squares forward.
    """
    def __init__(self, color = "white", moves = 0):
        super().__init__(color)
        self.moves = moves
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
    
    def available_moves(self, position, board):
        """
        returns a list of legal squares where the pawn can move

        if it is the pawn's first move, will be able to move 2 squares
        in the direction

        will not be able to en passant (unless i have extra time but i cba)
        !! seems to work, as well with the capture moves
        """
        move_list = []
        pos = position
        if self.Color == self.white:
            if self.is_first_move():
                #if its the pawns first move, can move two squares
                for i in range(1,3):
                    if board[pos[0] - i][pos[1]] == Board.EMPTY:
                        #only add the move if the pawn isn't blocked
                        move_list.append((pos[0] - i, pos[1]))
                    else:
                        #if the pawn is being blocked, breaks the loop
                        break
            else:
                if board[pos[0] - 1][pos[1]] == Board.EMPTY:
                    move_list.append((pos[0] - 1, pos[1]))
            #adding moves for the pawn to capture other pieces
            if board[pos[0] - 1][pos[1] - 1]:
                if board[pos[0] - 1][pos[1] - 1].Color == self.black:
                    move_list.append((pos[0] - 1, pos[1] - 1))
            if board[pos[0] - 1][pos[1] + 1]:
                if board[pos[0] - 1][pos[1] + 1].Color == self.black:
                    move_list.append((pos[0] - 1, pos[1] + 1))

        if self.Color == self.black:
            if self.is_first_move():
                #if its the pawns first move, can move two squares
                for i in range(pos[0] + 1, pos[0] + 3):
                    #checks if the squares are empty
                    if board[pos[i]][pos[1]] == Board.EMPTY:
                        move_list.append((i, pos[1]))
                    else:
                        break
            else: #if it isn't first move, will only move one square
                if board[pos[0] + 1][pos[1]] == Board.EMPTY:
                    move_list.append((pos[0] + 1, pos[1]))
            #adding moves for the pawn to capture other pieces
            if board[pos[0] + 1][pos[1] + 1].Color == self.white:
                move_list.append((pos[0] + 1, pos[1] + 1))
            if board[pos[0] + 1][pos[1] - 1].Color == self.white:
                move_list.append((pos[0] + 1, pos[1] - 1))
        return move_list

class Knight(Piece):
    #a list for the tuples for the knight moves (knight displacement)
    knight_disp = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    def __init__(self,color):
        super().__init__(color)
    def available_moves(self, position, board):
        """
        returns a list containing tuples of available moves for a knight.
        takes in parameters for the position and the board
        !!seems to work
        """
        move_list = []
        pos = position
        for x, y in self.knight_disp:
            if pos[0] + x > 7 or pos[1] + y > 7 or pos[0] + x < 0 or pos[1] + y < 0:
                continue
            if board[pos[0] + x][pos[1] + y] == Board.EMPTY:
                move_list.append((pos[0] + x, pos[1] + y))
            elif board[pos[0] + x][pos[1] + y].Color == self.Color:
                continue
            elif board[pos[0] + x][pos[1] + y].Color != self.Color:
                move_list.append((pos[0] + x, pos[1] + y))
        return move_list
                


class Rook(Piece):
    #can only move horizontally/vertically
    r_increments = [(1,0), (-1,0), (0,1), (0,-1)]
    def __init__(self,color):
        super().__init__(color)

    def available_moves(self, position, board):
        """
        returns a list containing tuples of available moves for a rook.
        takes in parameters for the position and the board
        !! seems to work!
        """
        return self.find_moves(position, self.Color, self.r_increments, board)

class Bishop(Piece):
    #can only move diagonally
    b_increments = [(1,1), (1,-1), (-1,1), (-1,-1)]
    def __init__(self,color):
        super().__init__(color)

    def available_moves(self, position, board):
        """
        returns a list containing tuples of available moves for a bishop.
        takes in parameters for the position and the board
        !! seems to work!
        """
        return self.find_moves(position, self.Color, self.b_increments, board)
class King(Piece):
    """
    need to add methods for check, as well as methods for if other color pieces
    will be able to see the king if it moves to a certain square in the Board class!!!
    """
    #same directions as the queen, but can only move 1 square
    king_disp = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    def __init__(self,color):
        super().__init__(color)
    def available_moves(self, position, board):
        """
        returns a list containing tuples of available moves for a king.
        takes in parameters for the position and the baod
        """

class Queen(Piece):
    #can move either horizontally/vertically or diagonally
    q_increments = [(1,1), (1,-1), (-1,1), (-1,-1), (1,0), (-1,0), (0,1), (0,-1)]
    def __init__(self,color):
        super().__init__(color)

    def available_moves(self, position, board):
        """
        returns a list containing tuples of available moves for a queen.
        takes in parameters for the position and the board
        !! seems to work!
        """
        return self.find_moves(position, self.Color, self.q_increments, board)

class Game():
    """
    Class to control the state of the Chess game. 
    """
    white_pieces = "white"
    black_pieces = "black"
    def __init__(self):
        self.board = Board()
        self.turn = Game.white_pieces
    def play_turn(self):
        """
        This method executes a single turn by:
         - prompting the user for a legal move
         - modifying the board state
         - ending the current player's turn
        """
    
    def get_move(self):
        """
        gets the move from the player whose turn it is
        """
    def in_check(self):
        """
        checks if either king piece is in check. if it detects a 
        king in check, it will thendetermine if there is checkmate,
        if there isn't checkmate, will tell the player whose King
        is in check that they are in check
        """

a = Board()
a.print_board()
print(a.board[4][1].position)
print(a.board[4][1].Color)
print(type(a.board[4][1]))

print(a.board[4][1].available_moves(a.board[4][1].position, a.board))
#print(a.board)
#print(a.board[0][0].Color)