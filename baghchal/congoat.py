#Agent By Dunski

from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List
import random

class ConserveGoatAgent(Agent):
    def __init__(self, game : Game):
        super(ConserveGoatAgent, self).__init__(game,Const.MARK_GOAT)
    def propose(self) -> Move:
        moves = self.game.goatMoves()
        placements : List[Move]=[]
        for move in moves:
            if move.placement:
                if self.game._placed < Const.GOAT_PLACEMENTS:
                    for row in range(Const.ROWS):
                        for col in range(Const.COLS):
                            for dir in Const.DIRS[(row,col)]:
                                toRow : int = row+1*dir[0]
                                toCol : int = col+1*dir[1]
                                if self.game._board[toRow][toCol] == Const.MARK_GOAT:
                                    placements.append(move)
        if len(placements) != 0:
            return random.choice(placements);
        else:
            return random.choice(moves);
