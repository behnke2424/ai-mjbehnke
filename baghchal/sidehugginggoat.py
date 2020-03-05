from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List
import random

class SideHuggingGoat(Agent):
    def __init__(self, game : Game):
        super(SideHuggingGoat, self).__init__(game, Const.MARK_GOAT)
    def propose(self) -> Move:
        moves = self.game.goatMoves()
        for move in moves:
            if move._toCol == move._fromCol and move._toCol == 0:
                return move
            if move._toCol == move._fromCol and move._toCol == Const.COLS-1:
                return move
            if move._toRow == move._fromRow and move._toRow ==  0:
                return move
            if move._toRow == move._fromRow and move._toRow == Const.ROWS-1:
                return move
        return random.choice(moves)       