from typing import Set,Dict,Tuple,List

def ConstDirCache(rows : int, cols : int) -> Dict[Tuple[int,int],List[Tuple[int,int]]]:
    cache : Dict[Tuple[int,int],List[Tuple[int,int]]] = {}
    for row in range(rows):
        for col in range(cols):
            dirs : List[Tuple[int,int]] = []
            if row > 0: dirs.append((-1,0))
            if row < rows-1: dirs.append((1,0))
            if col > 0: dirs.append((0,-1))
            if col < cols-1: dirs.append((0,1))
            if (row + col) % 2 == 0:
                if (row > 0 and col > 0): dirs.append((-1,-1))
                if (row < rows-1 and col < cols-1): dirs.append((1,1))
                if (row > 0 and col < cols-1): dirs.append((-1,1))
                if (row < rows-1 and col > 0): dirs.append((1,-1))
            cache[(row,col)]=dirs
    return cache


class Const:
    ROWS : int = 5
    COLS : int = 5
    GOAT_CAPTURES_FOR_TIGER_WIN : int = 5
    MAX_MOVES_WITHOUT_CAPTURE : int = 50
    GOAT_PLACEMENTS : int = 20

    MARK_NONE : int = 0
    MARK_GOAT : int = 1
    MARK_TIGER : int = 2

    STATE_TURN_GOAT : int = 1
    STATE_TURN_TIGER : int = 2
    STATE_WIN_GOAT : int = 3
    STATE_WIN_TIGER : int = 4
    STATE_DRAW : int = 5
    
    STATES : Set[int] = set([STATE_TURN_GOAT, STATE_TURN_TIGER,STATE_WIN_GOAT,STATE_WIN_TIGER,STATE_DRAW])
    MARKS : Set[int] = set([MARK_NONE,MARK_GOAT,MARK_TIGER])

    DIRS : Dict[Tuple[int,int],List[Tuple[int,int]]] = ConstDirCache(ROWS,COLS)

    @classmethod
    def rowOk(cls,row : int) -> None:
        if row < 0 or row >= cls.ROWS:
            raise ValueError("row (" + str(row) + ") must be between 0 and " + str(Const.ROWS-1))

    @classmethod
    def colOk(cls,col : int) -> None:
        if col < 0 or col >= cls.COLS:
            raise ValueError("column (" + str(col) + ") must be between 0 and " + str(Const.COLS-1))

    @classmethod
    def markOk(cls,mark : int) -> None:
        if not mark in cls.MARKS:
            raise ValueError("mark (" + str(mark) + ") must be NONE, GOAT or TIGER")

    @classmethod
    def markStr(cls,mark : int) -> str:
        if mark == cls.MARK_GOAT: return "G"
        if mark == cls.MARK_TIGER: return "T"
        if mark == cls.MARK_NONE: return " "
        return "?"

    @classmethod
    def stateOk(cls,state : int) -> None:
        if not state in cls.STATES:
            raise ValueError("state (" + str(state) + ") must be TURN_GOAT, TURN_TIGER, WIN_GOAT, WIN_TIGER or DRAW")

    @classmethod
    def stateStr(cls,state : int) -> str:
        if state == cls.STATE_TURN_GOAT: return "goat's turn"
        if state == cls.STATE_TURN_TIGER: return "tiger's turn"
        if state == cls.STATE_WIN_GOAT: return "goat won"
        if state == cls.STATE_WIN_TIGER: return "tiger won"
        if state == cls.STATE_DRAW: return "draw"
        return "unknown state (" + str(state) + ")"
