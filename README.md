# Requirements
- there aren't any requirements to run my code, nothing needed to be installed, it is all done
without importing any libraries, etc. (beside the unittests)

# Limitations
- just specific way of inputting moves: 
When inputting, use the chess files such that file 'a' would be column of index 0
 and row 1 would be row of index 7 in an 8x8 matrix

The program will prompt you for the FILE of a PIECE to move, 
 then a ROW of a PIECE, then it will ask you where you want to move to and prompt you for the
 FILE of the square you want to move to, then the ROW of the square you want to move to.

- the only way to select a different piece after entering anything is only if you only 
 entered the FILE for the PIECE you picked to move, if u want a different piece you can put in 
 an invalid ROW and it should prompt you to pick the FILE and ROW for the piece again. once you 
 enter a valid position for a piece, you will be locked into moving that piece.

- for the print_board() method in the Board class, the dictionary of unicode chess pieces are actually swapped
 from what they said they were from where i copy and pasted the symbols in from ; the 'white' pieces in 
 self.pieces_w are actually the black pieces, but they appear white in my vscode terminal, so I put them for the 
 white piece dictionary. If you run the game using the board option, and it has black pieces at the bottom of the board
 and white pieces at the top, then the dictionaries need to be swapped with each other.

- specific chess stuff that isn't in this (even though i tried to add as much stuff that seamed plausible/doable)
 no en passant (isn't in the list of legal moves)
 no castling 
   - if you really want to castle you can manually do it while the other player just moves one of their pieces away and back 
    to the same spot
 no stalemate checks

 
 even though i was able to fix a specific checkmate that is/ is similar to backrank checkmates;
 finding the checkmates is still not fully how it would be on a real chess website/game
 if a king is in check and has no legal moves while in check, it will consider it checkmate
 - this means that if a king is in a position where its in check and it can't move, then no matter what
 my program will consider it checkmate; even if another piece could block or take the piece putting the king in check



- kinda important one: if you pick a piece that has no legal moves available i.e. a rook/bishop/queen/king as the first move,
the code will just keep asking you for moves since no move you enter will be legal, so if you do this, just ctrl+c it and rerun!

# How to run/use program
should be a 'two' player game and there is no chess ai or anything like this, moves will only be played with inputs

this was somewhat kind of explained in the limitations, but basically just run the chess_game.py file
and it will prompt you if you want it to display as a Board (0) or a PGN (1)
after this, you will just be inputting the pieces you want to move and the moves until someone wins.
the inputs are done so that it asks you for the file of either the piece/move, and then the row of the piece/move
the input for the file should be a lowercase letter as they would be for a standard chessboard, and 
the row should be input as an integer 1-8 inclusive. the input you are putting in is the position as it appears
on the board as previously explained (if you chose the board display)  

there are no supported command line arguments

## Contents

This repository should contain the following folders/files:
- chess_game.py
- chess_test.py

The `chess_test.py` file contains all the tests.
The `chess_game.py` file contains the main chess board.