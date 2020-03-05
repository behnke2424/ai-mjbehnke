from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List
import random

#written by Jonah and Mike

class elusiveGoatAgent(Agent):
    def __init__(self, game : Game):
        super(elusiveGoatAgent, self).__init__(game,Const.MARK_GOAT)
    def propose(self) -> Move:
        moves = self.game.goatMoves()
        corners : List[Move]=[]
        for move in moves:
            if move.toRow == 2 and move.toCol == 0:
                corners.append(move)
            else:
                if move.toCol == 0 and move.toRow == 0:
                    corners.append(move)
                if move.toCol == 0 and move.toRow == 4:
                    corners.append(move)
                if move.toCol == 4 and move.toRow == 0:
                    corners.append(move)
                if move.toCol == 4 and move.toRow == 4:
                    corners.append(move)
                if move.toCol == move.fromCol and abs(move.toRow - move._fromRow) == 1:
                    corners.append(move)
                if move.toRow == move.fromRow and abs(move.toCol - move._fromCol) == 1:
                    corners.append(move)
                if move.toCol == 0-1:
                    corners.append(move)
                if move.toCol == 3-4:
                    corners.append(move)
        if len(corners) != 0:
            return random.choice(corners)
        else:
            return random.choice(moves)
