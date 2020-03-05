# SmartGoatAgent
# Matt Behnke
# Dr. MacEvoy
# CSCI 486
# 5 March 2019
from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List, Optional
from hungrytigeragent import HungryTigerAgent
import random

#Find corners
def checkCorners(move):
    if(str(move) == 'Ga1' or str(move) == 'Ge1' or str(move) == 'Ga5' or str(move) == 'Ge5'):
        return move
    return None

def block(goatMoves, tigerMove: str):
    # See if we can safely block a capture
    for goatMove in goatMoves:
        strGoatMove = str(goatMove)
        if(len(strGoatMove) == 3):
            # This is a placement
            if(tigerMove in strGoatMove):
                return goatMove
        else:
            # This is a movement (capture)
            strGoatMove = "".join([strGoatMove[4], strGoatMove[5]])
            if tigerMove in strGoatMove:
                return goatMove
    return None
    

class SmartGoatAgent(Agent):
    #Constructors 
    def __init__(self, game: Game):
        super(SmartGoatAgent, self).__init__(game, Const.MARK_GOAT)
        self._hungryTigerAgent = HungryTigerAgent(game)

    #Check Corners
    def checkCorners(self, moves):
        for move in moves:
            if(str(move) == 'Ga1' or str(move) == 'Ge1' or str(move) == 'Ga5' or str(move) == 'Ge5'):
                return move
        return None
                
    
    def propose(self) -> Move:
        # Get Moves
        moves = self.game.goatMoves()

        # List of potential moves
        safe : List[Move]=[]
        wins : List[Move]=[]
        loses : List[Move]=[]
        draws : List[Move]=[]
        scared : List[Move]=[]
        blocks : List[Move]=[]
        cornerGrab : List[Move]=[]
        
        # Look ahead       
        for move in moves:
            self.game.play(move)
            tigerMove : Optional[Move] = self._hungryTigerAgent.propose() \
                if self.game.state == Const.STATE_TURN_TIGER else None
            playedState : int = self.game.state
            self.game.unplay(move)

            # See if we can block a tiger capture
            blockMove = None
            if tigerMove.capture:
                endPlacement = str(tigerMove)
                endPlacement = "".join([endPlacement[4], endPlacement[5]])
                blockMove = block(moves, endPlacement)

            # Choose a block or corner over a safe move
            if playedState == Const.STATE_WIN_GOAT:
                wins.append(move)
            elif playedState == Const.STATE_WIN_TIGER:
                loses.append(move)
            elif blockMove != None:
                blocks.append(blockMove)
            elif checkCorners(move) != None:
                cornerGrab.append(move)
            elif not tigerMove.capture:
                safe.append(move)
            elif playedState == Const.STATE_DRAW:
                draws.append(move)
            else:
                scared.append(move)

        # Return the Move
        if len(wins) != 0:
            return random.choice(wins) 
        elif len(blocks) != 0:
            return random.choice(blocks)
        elif len(cornerGrab) != 0:
            return random.choice(cornerGrab)
        elif len(safe) != 0:
            return random.choice(safe)
        elif len(draws) != 0:
            return random.choice(draws)
        elif len(scared) != 0:
            print(scared)
            return random.choice(scared)
        else:
            return random.choice(moves)