from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List
import random

class AggressiveGoatAgent(Agent):
    def __init__(self, game : Game):
        super(AggressiveGoatAgent, self).__init__(game,Const.MARK_GOAT)
    def propose(self) -> Move:
        moves = self.game.goatMoves()
        safeMoves : List[Move]=[]
        safeMovesPriority : List[int]=[]
        for move in moves:
            self.game.play(move)
            tigerMoves = self.game.tigerMoves()
            captures : List[Move]=[]
            for tMove in tigerMoves:
                if tMove.capture:
                    captures.append(move)
            if len(captures) == 0:
                safeMoves.append(move)
                safeMovesPriority.append(len(tigerMoves))
            self.game.unplay(move)
        bestMoves : List[Move]=[]
        if len(safeMoves) != 0:
            bestPriority = min(safeMovesPriority)
            for i in range(len(safeMoves)):
                if safeMovesPriority[i] == bestPriority:
                    bestMoves.append(safeMoves[i])
        else:
            bestMoves = moves
        return random.choice(bestMoves)
