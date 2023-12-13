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
    
    def place_move(self, pos, move):
        """
        Updates the board given the position of the piece being moved
        and the move. Only places the move if the move is legal.
        Updates the previous spot on the board to become empty

        Returns: True if a move was succesfully made; False if a move
        was invalid and/or reverted. 

        pos - a tuple representing the position of the piece being moved
        move - a tuple representing the position the piece is moving to
        """
        #only plays the move if it is a legal move for that piece
        if pos[0] > 7 or pos[1] > 7 or pos[0] < 0 or pos[1] < 0 or move[0] > 7 or move[1] > 7 or move[0] < 0 or move[1] < 0:
            return False
        if self.in_check():
            #setting a variable to hold the color of the king thats in check
            a = self.board[self.in_check()[0]][self.in_check()[1]].Color
            #if a king is in check:
            if move in self.board[pos[0]][pos[1]].available_moves(self.board):
                if self.board[move[0]][move[1]] == self.EMPTY:
                    temp_hold = self.EMPTY
                else:
                    temp_hold = type(self.board[move[0]][move[1]])(self.board[move[0]][move[1]].Color) #MEMORY PROBLEM
                self.board[move[0]][move[1]] = self.board[pos[0]][pos[1]]
                self.board[pos[0]][pos[1]] = self.EMPTY
                self.update_pos()
                #after updating the board with the move, if a king is still in check:
                if self.in_check():
                    #will check if the king in check is the same color as it was before
                    if a == self.board[self.in_check()[0]][self.in_check()[1]].Color:
                        #reverts the move
                        self.board[pos[0]][pos[1]] = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = temp_hold
                        self.update_pos()
                        return False
                    #if the king in check now isn't the same color king as it was originally:
                    else:
                        if type(self.board[move[0]][move[1]]) == Pawn:
                            self.board[move[0]][move[1]].moves += 1
                        return True
                else:
                    if type(self.board[move[0]][move[1]]) == Pawn:
                        self.board[move[0]][move[1]].moves += 1
                    return True
        #when moving from check to out of check, the indices of what pos was
        #will become empty, making the elif after this cause error; this prevents this
        elif self.board[pos[0]][pos[1]] == self.EMPTY:
            return True
        elif move in self.board[pos[0]][pos[1]].available_moves(self.board):
            #holds the color of the piece being moved
            color_check = self.board[pos[0]][pos[1]].Color
            if self.board[move[0]][move[1]] == self.EMPTY:
                temp_hold = self.EMPTY
            else:
                temp_hold = type(self.board[move[0]][move[1]])(self.board[move[0]][move[1]].Color) #MEMORY PROBLEM
            self.board[move[0]][move[1]] = self.board[pos[0]][pos[1]]
            self.board[pos[0]][pos[1]] = self.EMPTY
            self.update_pos()
            if self.in_check():
                #if the king in check after the move is the same color as the piece that was
                #just moved, should revert the move
                if self.board[self.in_check()[0]][self.in_check()[1]].Color == color_check:
                    #reverts the move
                    self.board[pos[0]][pos[1]] = self.board[move[0]][move[1]]
                    self.board[move[0]][move[1]] = temp_hold
                    self.update_pos()
                    return False
                else:
                    if type(self.board[move[0]][move[1]]) == Pawn:
                        self.board[move[0]][move[1]].moves += 1
                    return True
            else:
                if type(self.board[move[0]][move[1]]) == Pawn:
                    self.board[move[0]][move[1]].moves += 1
                return True
        else:
            return False
        if type(self.board[move[0]][move[1]]) == Pawn:
            self.board[move[0]][move[1]].moves += 1
        return True
    
    def in_check(self):
        """
        Returns either the position of a king in check, or False
        checks if either king piece is in check. if it detects a 
        king in check, returns the position of the king
        """
        for j in self.board:
            for p in j:
                if p == self.EMPTY:
                    pass
                else:
                    for i in p.available_moves(self.board):
                        if self.board[i[0]][i[1]] == self.EMPTY:
                            continue
                        if type(self.board[i[0]][i[1]]) == King:
                            return (i[0], i[1])
                        """
                            if self.board[i[0]][i[1]].Color == King.white:
                                return King.white
                            if self.board[i[0]][i[1]].Color == King.black:
                                return King.black 
                        """
        return False
    
    def checkmate(self):
        """
        Returns the winner of the game (either Piece.white or Piece.black) 
        if there is checkmate. Otherwise returns None.

        checks if a king is in check, and then checks if the king has any avai
        TODO:
        if a move would put the king out of 

        Will check if the there is check first.
        """
        if self.in_check():
            king_pos = self.in_check()
            if not self.board[king_pos[0]][king_pos[1]].available_moves(self.board):
                if self.board[king_pos[0]][king_pos[1]].Color == Piece.white:
                    return Piece.black
                else:
                    return Piece.white
        else:
            return None
        
    def update_pos(self):
        """
        updates the position of every piece in the board
        """
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j] == self.EMPTY:
                    pass
                else:
                    self.board[i][j].position = (i, j)
    
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
        #self.board[3][0] = King(King.white) #line i test methods for pieces with
        self.update_pos()

    def is_occupied(self, pos):
        """
        Returns True if there is a piece at a certain position, and 
        False if the index is not on the board or if position is empty
        """
        row = pos[0]
        file = pos[1]
        if row > 7 or file > 7 or row < 0 or file < 0:
            return False
        if self.board[row][file] == self.EMPTY:
            return False
        else:
            return True
    def get_color(self, pos):
        """
        Returns the color of a piece at a certain position
        """
        if pos[0] > 7 or pos[1] > 7 or pos[0] < 0 or pos[1] < 0:
            return False
        if self.board[pos[0]][pos[1]] == self.EMPTY:
            return False
        return self.board[pos[0]][pos[1]].Color


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
    def protected(self, color, increments, board):
        """
        returns a list of moves that the piece would be "protecting"
        given the color, the increment, and the board

        nearly identical to the find_moves method above, only difference is 
        it adds a move if the piece in the square is the same color before
        going on to the next increment instead of just not adding the move

        this function is only for pieces that can move an infinite 
        number of spaces (rook, bishop, queen)
        """
        pos = self.position
        row = pos[0]
        file = pos[1]
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
                #adds the move and then goes to the next increment "protected"
                elif board[curr_row][curr_file].Color == color:
                    move_list.append((curr_row, curr_file))
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
    
    def available_moves(self, board):
        """
        returns a list of legal squares where the pawn can move

        if it is the pawn's first move, will be able to move 2 squares
        in the direction

        will not be able to en passant (unless i have extra time but i cba)
        !! seems to work, as well with the capture moves
        """
        move_list = []
        pos = self.position
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
                if pos[0] > 0:
                    if board[pos[0] - 1][pos[1]] == Board.EMPTY:
                        move_list.append((pos[0] - 1, pos[1]))
            #adding moves for the pawn to capture other pieces
            #if the index of the row is 0, shouldn't go out of bounds
            if pos[0] > 0:
                #if the index of the column is 0, shouldn't go out of bounds
                if pos[1] > 0: 
                    if board[pos[0] - 1][pos[1] - 1]:
                        if board[pos[0] - 1][pos[1] - 1].Color == self.black:
                            move_list.append((pos[0] - 1, pos[1] - 1))
                #if the index of the column is 7, shouldn't go out of bounds
                if pos[1] < 7:
                    if board[pos[0] - 1][pos[1] + 1]:
                        if board[pos[0] - 1][pos[1] + 1].Color == self.black:
                            move_list.append((pos[0] - 1, pos[1] + 1))

        if self.Color == self.black:
            if self.is_first_move():
                #if its the pawns first move, can move two squares
                for i in range(1, 3):
                    #checks if the squares are empty
                    if board[pos[0] + i][pos[1]] == Board.EMPTY:
                        move_list.append((pos[0] + i, pos[1]))
                    else:
                        break
            else: #if it isn't first move, will only move one square
                if pos[0] < 7:
                    if board[pos[0] + 1][pos[1]] == Board.EMPTY:
                        move_list.append((pos[0] + 1, pos[1]))
            #adding moves for the pawn to capture other pieces
            if pos[0] < 7:
                if pos[1] < 7:
                    if board[pos[0] + 1][pos[1] + 1]:
                        if board[pos[0] + 1][pos[1] + 1].Color == self.white:
                            move_list.append((pos[0] + 1, pos[1] + 1))
                if pos[1] > 0:
                    if board[pos[0] + 1][pos[1] - 1]:
                        if board[pos[0] + 1][pos[1] - 1].Color == self.white:
                            move_list.append((pos[0] + 1, pos[1] - 1))
        return move_list
    
    def protecting(self, board):
        """
        returns the legal squares where a pawn would be able to take
        a piece if a piece were in the squares
        to be used for the line_of_sight method in the King class
        adds the move even if a piece of the same color is in it "protecting"
          like a knight outpost
        """
        move_list = []
        pos = self.position
        if self.Color == self.white:
            if pos[0] > 0:
                #if the index of the column is 0, shouldn't go out of bounds
                if pos[1] > 0:
                    move_list.append((pos[0] - 1, pos[1] - 1))
                #if the index of the column is 7, shouldn't go out of bounds
                if pos[1] < 7:
                    move_list.append((pos[0] - 1, pos[1] + 1))
        if self.Color == self.black:
            if pos[0] < 7:
                #if the index of the column is 0, shouldn't go out of bounds
                if pos[1] > 0:
                    move_list.append((pos[0] + 1, pos[1] - 1))
                #if the index of the column is 7, shouldn't go out of bounds
                if pos[1] < 7:
                    move_list.append((pos[0] + 1, pos[1] + 1))
        return move_list

class Knight(Piece):
    #a list for the tuples for the knight moves (knight displacement)
    knight_disp = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    def __init__(self,color):
        super().__init__(color)
    def available_moves(self, board):
        """
        returns a list containing tuples of available moves for a knight.
        takes in parameters for the position and the board
        !!seems to work
        """
        move_list = []
        pos = self.position
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
    def protecting(self, board):
        """
        returns the list of tuples containing squares "protected" by the
        knight
        """
        move_list = []
        pos = self.position
        for x, y in self.knight_disp:
            if pos[0] + x > 7 or pos[1] + y > 7 or pos[0] + x < 0 or pos[1] + y < 0:
                continue
            else:
                move_list.append((pos[0] + x, pos[1] + y))
        return move_list

class Rook(Piece):
    #can only move horizontally/vertically
    r_increments = [(1,0), (-1,0), (0,1), (0,-1)]
    def __init__(self,color):
        super().__init__(color)

    def available_moves(self, board):
        """
        returns a list containing tuples of available moves for a rook.
        takes in parameters for the position and the board
        !! seems to work!
        """
        return self.find_moves(self.position, self.Color, self.r_increments, board)
    
    def protecting(self, board):
        """
        returns the list of tuples containing squares "protected" by the
        rook
        """
        return self.protected(self.Color, self.r_increments, board)
    
class Bishop(Piece):
    #can only move diagonally
    b_increments = [(1,1), (1,-1), (-1,1), (-1,-1)]
    def __init__(self,color):
        super().__init__(color)

    def available_moves(self, board):
        """
        returns a list containing tuples of available moves for a bishop.
        takes in parameters for the position and the board
        !! seems to work!
        """
        return self.find_moves(self.position, self.Color, self.b_increments, board)
    
    def protecting(self, board):
        """
        returns the list of tuples containing squares "protected" by the
        bishop
        """
        return self.protected(self.Color, self.b_increments, board)
    
class King(Piece):
    """
    need to add methods for check, as well as methods for if other color pieces
    will be able to see the king if it moves to a certain square in the Board class!!!
    """
    #same directions as the queen, but can only move 1 square
    king_disp = [(1,1), (1,-1), (-1,1), (-1,-1), (1,0), (-1,0), (0,1), (0,-1)]
    def __init__(self,color):
        super().__init__(color)
    def available_moves(self, board):
        """
        returns a list containing tuples of available moves for a king.
        takes in parameters for the position and the baod
        TODO: check for check, and if a move would put the king in line 
        of sight of a piece of the opposite color
        """
        move_list = []
        pos = self.position
        for x, y in self.king_disp:
            #keeping the moves in bounds
            if pos[0] + x > 7 or pos[1] + y > 7 or pos[0] + x < 0 or pos[1] + y < 0:
                continue
            if board[pos[0] + x][pos[1] + y] == Board.EMPTY: #and the method for line of sight
                move_list.append((pos[0] + x, pos[1] + y))
            elif board[pos[0] + x][pos[1] + y].Color == self.Color:
                continue
            elif board[pos[0] + x][pos[1] + y].Color != self.Color:
                move_list.append((pos[0] + x, pos[1] + y))
        move_list = self.line_of_sight(move_list, self.Color, board)
        return move_list
    
    def line_of_sight(self, moves, color, board):
        """
        takes in a list of moves as a parameter (a list of tuples)
        and checks all the pieces on the board to see if any pieces of
        the opposite color would have line of sight of any of the squares

        also takes in the color as a parameter so it can check
        for the opposite color

        the method is for the king, and is meant to return a new list of moves
        with these squares that would be in line of sight and squares that have pieces
        that are protected to be removed.
        """
        bad_moves = set()
        for m in moves:
            for l in board:
                for p in l:
                    if p == Board.EMPTY:
                        pass
                    else:
                        if p.Color == color:
                            pass
                        else:
                            if m in p.protecting(board):
                                bad_moves.add(m)
        if len(bad_moves) == 0:
            return moves
        else:
            for i in bad_moves:
                moves.remove(i)
        return moves
    
    def protecting(self, board):
        """
        the same exact function as the King.available_moves, except
        it will not remove moves from the list of moves given line
        of sight. 
        Used in the line_of_sight method to potentially remove moves
        due to the other king
        will also have the moves even if a piece of the same color is in
        that square, since the king would protect it from the other king
        """
        move_list = []
        pos = self.position
        for x, y in self.king_disp:
            #keeping the moves in bounds
            if pos[0] + x > 7 or pos[1] + y > 7 or pos[0] + x < 0 or pos[1] + y < 0:
                continue
            move_list.append((pos[0] + x, pos[1] + y))
        return move_list

class Queen(Piece):
    #can move either horizontally/vertically or diagonally
    q_increments = [(1,1), (1,-1), (-1,1), (-1,-1), (1,0), (-1,0), (0,1), (0,-1)]
    def __init__(self,color):
        super().__init__(color)

    def available_moves(self, board):
        """
        returns a list containing tuples of available moves for a queen
        takes in parameters for the position and the board
        !! seems to work!
        """
        return self.find_moves(self.position, self.Color, self.q_increments, board)
    
    def protecting(self, board):
        """
        returns the list of tuples containing squares "protected" by the
        queen
        """
        return self.protected(self.Color, self.q_increments, board)

class Game():
    """
    Class to control the state of the Chess game. 
    """
    white_pieces = "white"
    black_pieces = "black"
    #dictionaries to convert the player's input into the position
    # of the piece in the board: file a is column of index 0 etc.
    file_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    row_dict = {'1':7, '2':6, '3':5, '4':4, '5':3, '6':2, '7':1, '8':0}
    def __init__(self):
        self.Board = Board()
        self.turn = Game.white_pieces
    def play_turn(self):
        """
        This method executes a single turn by:
         - prompting the user for the position of the piece to move
         - prompting the user for a legal move
         - modifying the board
         - ending the current player's turn
        """
        #initializing these as values that are not valid and would 
        # cause the while loops to run
        move = (8, 8) 
        piece = (8, 8)
        
        self.Board.print_board()
        #MAKE USER GET OUT OF CHEKC IF THEY IN CHECK
        if self.Board.in_check():
            while not self.Board.place_move(piece, move):
                print("The {} king is in check".format(self.Board.board[self.Board.in_check()[0]][self.Board.in_check()[1]].Color))
            #making piece and move out of range again so it asks for both again
                piece = (8, 8)
                move = (8, 8)
                while not self.Board.is_occupied(piece) or self.Board.get_color(piece) != self.turn:
                    print("It is {}'s turn to move".format(self.turn))
                    piece = self.get_piece()
                    if not self.Board.is_occupied(piece) or self.Board.get_color(piece) != self.turn:
                        self.Board.print_board()
                        print("The square you selected does not have a valid piece.")
                
                while move not in self.Board.board[piece[0]][piece[1]].available_moves(self.Board.board):
                    move = self.get_move()
                    if move not in self.Board.board[piece[0]][piece[1]].available_moves(self.Board.board):
                        self.Board.print_board()
                        print("The move you entered is not valid.")
                self.Board.place_move(piece, move)
                if not self.Board.place_move(piece, move):
                    self.Board.print_board()
                    print("You are in Check!")
        else:
            while not self.Board.is_occupied(piece) or self.Board.get_color(piece) != self.turn:
                print("It is {}'s turn to move".format(self.turn))
                piece = self.get_piece()
                if not self.Board.is_occupied(piece) or self.Board.get_color(piece) != self.turn:
                    self.Board.print_board()
                    print("The square you selected does not have a valid piece.")
            
            while move not in self.Board.board[piece[0]][piece[1]].available_moves(self.Board.board):
                move = self.get_move()
                if move not in self.Board.board[piece[0]][piece[1]].available_moves(self.Board.board):
                    self.Board.print_board()
                    print("The move you entered is not valid.")
        #places move
        self.Board.place_move(piece, move)
        #switches turns
        if self.turn == Game.white_pieces:
            self.turn = Game.black_pieces
        else:
            self.turn = Game.white_pieces
    
    def get_piece(self):
        """
        Gets the first part of the move from the player whose turn
        it is by asking for the position of the piece they want to move

        returns the move's corresponding position as a tuple with two
        elements, the index of the row and the file on the board
        """
        row_input = None
        file_input = None
        #white pieces turn
        if self.turn == Game.white_pieces: 
            #get the piece's position that the player wants to move
            while row_input not in Game.row_dict or file_input not in Game.file_dict:
                file_input = str(input("Please enter the file of the piece: "))
                row_input = str(input("Please enter the row of the piece: "))
                if row_input not in Game.row_dict or file_input not in Game.file_dict:
                    print("The position you entered is invalid. \n")
            row = Game.row_dict[row_input]
            file = Game.file_dict[file_input]
            #putting the inputs into a tuple for the move
            piece = (row, file)

        #black pieces turn
        if self.turn == Game.black_pieces:   
            while row_input not in Game.row_dict or file_input not in Game.file_dict:
                file_input = str(input("Please enter the file of the piece: "))
                row_input = str(input("Please enter the row the piece: "))
                if row_input not in Game.row_dict or file_input not in Game.file_dict:
                    print("The position you entered is invalid. \n")
            row = Game.row_dict[row_input]
            file = Game.file_dict[file_input]
            #putting the inputs into a tuple for the move
            piece = (row, file)
        #returns the piece tuple
        return piece
    
    def get_move(self):
        """
        Gets the second part of the move from the player whose turn it 
        is by asking for the position they want to move their piece to.

        returns the move's corresponding position as a tuple with two
        elements, the index of the row and the file on the board
        """
        row_input = None
        file_input = None
        #white pieces turn
        if self.turn == Game.white_pieces: 
            print("Where do you want to move to?")
            #get the position the player wants to move to
            while row_input not in Game.row_dict or file_input not in Game.file_dict:
                file_input = str(input("Please enter the file of the move: "))
                row_input = str(input("Please enter the row the move: "))
                if row_input not in Game.row_dict or file_input not in Game.file_dict:
                    print("The move you entered is invalid. \n")
            row = Game.row_dict[row_input]
            file = Game.file_dict[file_input]
            #putting the inputs into a tuple for the move
            move = (row, file)

        #black pieces turn
        if self.turn == Game.black_pieces: 
            print("Where do you want to move to?") 
            while row_input not in Game.row_dict or file_input not in Game.file_dict:
                file_input = str(input("Please enter the file of the move: "))
                row_input = str(input("Please enter the row the move: "))
                if row_input not in Game.row_dict or file_input not in Game.file_dict:
                    print("The move you entered is invalid. \n")
            row = Game.row_dict[row_input]
            file = Game.file_dict[file_input]
            #putting the inputs into a tuple for the move
            move = (row, file)
        #returns the piece tuple
        return move
    def announce_winner(self):
        """
        prints out a message for the winner
        """
        print("Congratulations {} has won the game!".format(self.Board.checkmate()))
        return
    def play(self):
        """
        This method starts the game.
        """
        while not self.Board.checkmate():
            self.play_turn()
        #show the board at the end of the game
        self.Board.print_board()
        self.announce_winner()

"""
TODO:
making the game play DONE; 
making a winner (finding checkmate)  should be easy 
with available_moves of the King with the protected method there nowDONE (sorta)
adding the PGN as a subclass of Board which should just change the way the board is displayed (will use PGN notation instead)
UPDATING PAWNS # OF MOVES - DONE
"""                   
"""
a = Game()
a.Board.print_board()

print(a.Board.board[3][0].position)
print(a.Board.board[3][0].Color)
print(type(a.Board.board[3][0]))

print(a.Board.board[3][0].available_moves(a.Board.board))
a.play_turn() """

Game().play()

#print(a.board)
#print(a.board[0][0].Color)