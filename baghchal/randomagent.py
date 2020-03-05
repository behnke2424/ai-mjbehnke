from agent import Agent
from game import Game
from const import Const
from move import Move
import random

class RandomAgent(Agent):
    def __init__(self,game : Game, side : int):
        super(RandomAgent, self).__init__(game,side)
    def propose(self) -> Move:
        if self.side == Const.MARK_GOAT:
            moves = self.game.goatMoves()
            return random.choice(moves)
        else:
            moves = self.game.tigerMoves()
            return random.choice(moves)
