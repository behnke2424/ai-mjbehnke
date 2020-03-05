# really good tiger agent

from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List, Optional
from hungrytigeragent import HungryTigerAgent
import random

def isClose(goat, tiger):
    if goat[0] == tiger[0]+1 or goat[0] == tiger[0]-1:
        return True
    if goat[1] == tiger[1]+1 or goat[1] == tiger[1]-1:
        return True
    return False

#goat moves randomly until next move can be near tiger
    #row or column is + or - row or column of tiger
#goat chooses this move unless it is capture

class GoatAgrosAgent(Agent):
    def __init__(self, game : Game):
        super(GoatAgrosAgent, self).__init__(game,Const.MARK_GOAT)
        self._hungryTigerAgent = HungryTigerAgent(game)
    def propose(self) -> Move:
        moves = self.game.goatMoves()
        hoard : List[Move]=[]
        c = False
        for move in moves:
            self.game.play(move)
            tigerMove : Optional[Move] = self._hungryTigerAgent.propose() \
                if self.game.state == Const.STATE_TURN_TIGER else None #why would this return None??
            playedState : int = self.game.state #will use this to implement
            #get tiger coordinates              #scaredgoatagent if beneficial
            if playedState == Const.STATE_TURN_TIGER:
                tigerCol = tigerMove.fromCol
                tigerRow = tigerMove.fromRow
                tigerPick = (tigerRow, tigerCol)
                if tigerMove.capture != True:
                    c = True
            self.game.unplay(move)
            goatPick = (move.toRow, move.toCol)
            if isClose(goatPick, tigerPick):
                hoard.append(move)
       
        if len(hoard) != 0:
            return random.choice(hoard)
        else:
            return random.choice(moves)