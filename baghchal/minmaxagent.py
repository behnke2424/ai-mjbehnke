import random

from typing import Optional, Tuple, List, Set

from const import Const
from move import Move
from game import Game
from agent import Agent
from hungrytigeragent import HungryTigerAgent
from aggressivegoatagent import AggressiveGoatAgent
class MinMaxAgent(Agent):
    DEFAULT_MAX_DEPTH : int = 2

    def __init__(self,game : Game, side : int, maxDepth : int = DEFAULT_MAX_DEPTH):
        super(MinMaxAgent, self).__init__(game,side)
        self._simpleTigerAgent : Agent = HungryTigerAgent(game)
        self._simpleGoatAgent : Agent = AggressiveGoatAgent(game)
        self._maxDepth : int = maxDepth

    @property
    def game(self) -> Game:
        return self._game

    @game.setter
    def game(self,value) -> None:
        self._game = value
        self._simpleTigerAgent.game = value
        self._simpleGoatAgent.game = value

    def minmax(self,depth : int) -> Tuple[Move,float, Move, float]:
        moves = self._game.moves
        first = True
        minValue : float =  1.0
        maxValue : float = -1.0
        minMove  : Move = moves[0]
        maxMove  : Move = moves[0]
        for move in moves:
            self._game.play(move)
            value = self.evaluate(depth)
            self._game.unplay(move)
            if first or value < minValue:
                minValue = value
                minMove = move
            if first or maxValue < value:
                maxValue = value
                maxMove = move
            if first:
                first = False
        return (minMove,minValue,maxMove,maxValue)

    def proposeMin(self,depth : int) -> Move:
        (minMove,minValue,maxMove,maxValue) = self.minmax(depth)
        return minMove
        
    def proposeMax(self,depth : int) -> Move:
        (minMove,minValue,maxMove,maxValue) = self.minmax(depth)
        return maxMove

    def evaluateMax(self,depth : int) -> float:
        (minMove,minValue,maxMove,maxValue) = self.minmax(depth)
        return maxValue

    def evaluateMin(self,depth : int) -> float:
        (minMove,minValue,maxMove,maxValue) = self.minmax(depth)
        return minValue

    def evaluateEndgame(self) -> float:
        if not self._game.over:
            raise ValueError("game is not over")

        if self._game.state == Const.STATE_WIN_GOAT:
            if self._side == Const.MARK_GOAT:
                return 1.0
            else:
                return -1.0
        elif self._game.state == Const.STATE_WIN_TIGER:
            if self._side == Const.MARK_TIGER:
                return 1.0
            else:
                return -1.0
        else:
            return 0.0

    def evaluateFuture(self,depth : int) -> float:
        if self._side == Const.MARK_GOAT:
            if self._game.state == Const.STATE_TURN_GOAT:
                return self.evaluateMax(depth)
            else:
                return self.evaluateMin(depth)
        else:
            if self._game.state == Const.STATE_TURN_TIGER:
                return self.evaluateMax(depth)
            else:
                return self.evaluateMin(depth)

    def evaluateHeuristic(self) -> float:
        moves : List[Move] = []
        while not self._game.over:
            if self._game.state == Const.STATE_TURN_GOAT:
                move = self._simpleGoatAgent.propose()
            else:
                move = self._simpleTigerAgent.propose()

            moves.append(move)
            self._game.play(move)
        value : float = self.evaluateEndgame()
        while len(moves) > 0:
            self._game.unplay(moves.pop())
        return value

    def evaluate(self,depth : int) -> float:
        if self._game.over:
            return self.evaluateEndgame()
        elif depth >= self._maxDepth:
            return self.evaluateHeuristic()
        else:
            return self.evaluateFuture(depth+1)

    def propose(self) -> Move:
        if self._game.over:
            raise ValueError("propose on finished game")
        if self.side == Const.MARK_GOAT:
            if self._game.state == Const.STATE_TURN_GOAT:
                return self.proposeMax(0)
            else:
                return self.proposeMin(0)
        else:
            if self._game.state == Const.STATE_TURN_TIGER:
                return self.proposeMax(0)
            else:
                return self.proposeMin(0)