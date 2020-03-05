from game import Game
from move import Move

class Agent:
    def __init__(self, game : Game, side : int):
        self._game = game
        self._side = side

    @property
    def game(self) -> Game:
        return self._game

    @game.setter
    def game(self,value) -> None:
        self._game = value

    @property
    def side(self) -> int:
        return self._side

    @side.setter
    def side(self,value) -> None:
        self._side = value

    def propose(self) -> Move:
        raise ValueError("nope.")
