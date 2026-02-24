"""Superclass of piece"""


class Piece():
    def __init__(self, team='w'):
        self.name_long:"str"   = 'Piece'
        self.name_short:"str"  = 'P'
        self.team:"str"        = team
        self.point_value:"int" = 10
        
        pass
    
    @property
    def name(self) -> "str":
        return self.name_short
    