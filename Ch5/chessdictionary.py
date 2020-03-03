"""
Chess Dictionary Validator
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} 
to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False 
depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, 
and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 
'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect 
when a bug has resulted in an improper chess board.
"""

chessBoard = {'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen', 'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
            'a7': 'bpawn', 'b7': 'bpawn', 'c7': 'bpawn', 'd7': 'bpawn', 'e7': 'bpawn', 'f7': 'bpawn', 'g7': 'bpawn', 'h7': 'bpawn',
            'a6': '', 'b6': '', 'c6': '', 'd6': '', 'e6': '', 'f6': '', 'g6': '', 'h6': '',
            'a5': '', 'b5': '', 'c5': '', 'd5': '', 'e5': '', 'f5': '', 'g5': '', 'h5': '',
            'a4': '', 'b4': '', 'c4': '', 'd4': '', 'e4': '', 'f4': '', 'g4': '', 'h4': '',
            'a3': '', 'b3': '', 'c3': '', 'd3': '', 'e3': '', 'f3': '', 'g3': '', 'h3': '',
            'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn', 'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn',
            'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen', 'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook'}

def isValidChessBoard(board):
    for k in board.keys():
        if k not in chessBoard.keys():
            return False
    for v in board.values():
        if v not in chessBoard.values():
            return False
        else:
            return True

# still have to program in duplicate key detection and duplicate value detection for each pieces

test = {'a8': 'lajsdlfk', 'a7': 'bbishop'}

print (isValidChessBoard(test))