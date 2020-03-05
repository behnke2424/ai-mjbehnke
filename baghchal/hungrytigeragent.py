from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List
import random

class HungryTigerAgent(Agent):
    def __init__(self, game : Game):
        super(HungryTigerAgent, self).__init__(game,Const.MARK_TIGER)
    def propose(self) -> Move:
        moves = self.game.tigerMoves()
        captures : List[Move]=[]
        for move in moves:
            if move.capture:
                captures.append(move)
        if len(captures) != 0:
            return random.choice(captures) 
        else:
            return random.choice(moves)
