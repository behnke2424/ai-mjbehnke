from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List, Optional
from hungrytigeragent import HungryTigerAgent
import random

class ScaredGoatAgent(Agent):
    def __init__(self, game : Game):
        super(ScaredGoatAgent, self).__init__(game,Const.MARK_GOAT)
        self._hungryTigerAgent = HungryTigerAgent(game)
    def propose(self) -> Move:
        moves = self.game.goatMoves()
        safe : List[Move]=[]
        wins : List[Move]=[]
        loses : List[Move]=[]
        draws : List[Move]=[]
        scared : List[Move]=[]
        for move in moves:
            self.game.play(move)
            tigerMove : Optional[Move] = self._hungryTigerAgent.propose() \
                if self.game.state == Const.STATE_TURN_TIGER else None
            playedState : int = self.game.state
            self.game.unplay(move)

            if playedState == Const.STATE_WIN_GOAT:
                wins.append(move)
            elif playedState == Const.STATE_WIN_TIGER:
                loses.append(move)
            elif playedState == Const.STATE_DRAW:
                draws.append(move)
            elif not tigerMove.capture:
                safe.append(move)
            else:
                scared.append(move)
        if len(wins) != 0:
            return random.choice(wins) 
        elif len(safe) != 0:
            return random.choice(safe)
        elif len(draws) != 0:
            return random.choice(draws)
        elif len(scared) != 0:
            return random.choice(scared)
        else:
            return random.choice(moves)
        
