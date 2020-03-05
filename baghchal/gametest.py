import unittest
from typing import List

from const import Const
from game import Game
from move import Move


class GameTest(unittest.TestCase):
 
    def testTigerMove(self):
        game = Game()
        moves = game.tigerMoves()
        self.assertEqual(len(moves),12)

    def testGoatMove(self):
        game = Game()
        moves = game.goatMoves()
        self.assertEqual(len(moves),Const.ROWS*Const.COLS-4)

    def testCountPlacementMoves(self):
        game = Game()
        placements = 0
        while True:
            moves = game.goatMoves()
            move0=moves[0]
            if not move0.placement:
                break
            placements += 1
            game.play(move0)
            moves = game.tigerMoves()
            move0 = moves[0]
            game.play(move0)
        self.assertEqual(placements,Const.GOAT_PLACEMENTS)
        

if __name__ == '__main__':
    unittest.main()
