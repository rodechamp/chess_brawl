"""Square superclass"""


ALPHABET = 'abcdefgh'

from .piece import Piece

class Square():
    def __init__(self, row:int=0, column:int=0):
        self.is_occupied:"bool" = False
        self.piece:"Piece"      = None
        
        self.row:"int"          = row
        self.column:"int"       = column
        
        pass
    
    """Diagnostics"""
    
    @property
    def is_black_square(self) -> bool:
        if (self.row + self.column)&2 == 0:
            return True
        else:
            return False
    
    
    @property
    def is_white_square(self) -> bool:
        return not self.is_black_square
    
    
    @property
    def name(self) -> str:
        return '{column}{row}'.format(column=ALPHABET[self.column], row=self.row+1)
    
    
    """SET and GET"""
    
    def set_piece(self, piece:"Piece") -> None:
        self.piece = piece