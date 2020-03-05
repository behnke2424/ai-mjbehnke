from agent import Agent
from const import Const
from game import Game
from typing import List, Optional
from move import Move
from hungrytigeragent import HungryTigerAgent
import random   

class OccamsGoatAgent(Agent):
    def __init__(self, game : Game):
        super(OccamsGoatAgent, self).__init__(game,Const.MARK_GOAT)
        self._hungryTigerAgent = HungryTigerAgent(game)
    def propose(self) -> Move:  
        moves = self.game.goatMoves()
        safe : List[Move]=[]
        wins : List[Move]=[]
        loses : List[Move]=[]
        draws : List[Move]=[]
        scared : List[Move]=[]
        # returns first possible place for goat to go, starting at a1 each time. 
        # one way to make this faster, is if we know a goat has gone and been placed and NOT captured, remove that from list of moves
        # pretty sure this would only affect computation speeds, not really benefit gameplay
        if self.game._turns == 0:
            return moves[1]
        else:
            #return moves[0]
            for move in moves: 
                self.game.play(move)        
                tigerMove : Optional[Move] = self._hungryTigerAgent.propose() \
                    if self.game.state == Const.STATE_TURN_TIGER else None
                playedState : int = self.game.state
                self.game.unplay(move)

                if playedState == Const.STATE_WIN_GOAT:
                    wins.append(move)
                elif playedState == Const.STATE_TURN_TIGER:
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
        