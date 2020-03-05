import unittest

from const import Const
from move import Move
from game import Game

class MoveTest(unittest.TestCase):
 
    def testPlacement(self):
        row = 1
        col = 2
        move = Move(Const.MARK_GOAT,row,col,row,col)
        self.assertTrue(move.placement)
        self.assertRaises(ValueError,lambda : Move(Const.MARK_TIGER,row,col,row,col))

    def testMovement(self):
        m=Const.MARK_GOAT
        r=1
        c=1
        move=Move(m,r,c,r+0,c+1)
        self.assertFalse(move.placement)
        move=Move(m,r,c,r+1,c+0)
        self.assertFalse(move.placement)
        move=Move(m,r,c,r+0,c-1)
        self.assertFalse(move.placement)
        move=Move(m,r,c,r-1,c+0)
        self.assertFalse(move.placement)

        m=Const.MARK_GOAT
        r=0
        c=0
        self.assertRaises(ValueError,lambda : Move(m,r,c,r-1,c-1))
        self.assertRaises(ValueError,lambda : Move(m,r,c,r-1,c+1))
        self.assertRaises(ValueError,lambda : Move(m,r,c,r+1,c-1))
        move=Move(m,r,c,r+1,c+1)

if __name__ == '__main__':
    unittest.main()
