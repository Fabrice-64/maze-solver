from enum import IntFlag, auto

class Border(IntFlag):
    """
    Border class defines the corners and intersections of the maze squares.
    Intflag class enumerates constants, which can be combined with bitwise comparrison operators.

    - dead_end(): a dead end has always 3 sides.
    - intersection(): an intersection has only 2 sides.
    """
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def corner(self) -> bool:
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.LEFT,
            self.BOTTOM | self.RIGHT,
        )
    
    @property
    def dead_end(self) -> bool:
        return self.bit_count() == 3
    
    @property
    def intersection(self) -> bool:
        return self.bit_count() < 2