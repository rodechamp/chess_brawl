"""Board superclass"""

# dimension of a chess board
DIM_BOARD:"int" = 8
MAXINDEX_BOARD:"int" = DIM_BOARD-1

from .class_square import Square

from .piece import Piece

class Board():
    def __init__(self):
        
        # a chess board has 8 x 8 squares
        self.squares:"list[list[Square]]" = []
        for row in range(DIM_BOARD):
            row_list = []
            for column in range(DIM_BOARD):
                row_list.append( 
                        Square(
                            row=MAXINDEX_BOARD-row, # rows are numbered in reverse, so that print of
                            column=column
                            ) 
                    )
            self.squares.append(row_list)
        
        pass
    
    
    
    
    
    """Visuals"""
    
    def print_square_names(self) -> None:
        """Printing the board to the command line"""
        for line in self.squares:
            for ss in line:
                print(ss.name, end=' ')
            print()

    
    """Setup"""
    
    def setup_test(self) -> None:
        for row_index, row in enumerate(self.squares):
            if row_index > 2:
                break
            else:
                for square in row:
                    square.set_piece( Piece )