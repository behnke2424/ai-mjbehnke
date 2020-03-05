import unittest

from const import Const


class ConstTest(unittest.TestCase):
 
    def testRow(self):
        Const.rowOk(0)
        Const.rowOk(Const.ROWS-1)
        self.assertRaises(ValueError,lambda : Const.rowOk(-1))
        self.assertRaises(ValueError,lambda : Const.rowOk(Const.ROWS))

    def testCol(self):
        Const.colOk(0)
        Const.colOk(Const.COLS-1)
        self.assertRaises(ValueError,lambda : Const.colOk(-1))
        self.assertRaises(ValueError,lambda : Const.colOk(Const.COLS))

    def testState(self):
        Const.stateOk(Const.STATE_TURN_GOAT)
        Const.stateOk(Const.STATE_TURN_TIGER)
        Const.stateOk(Const.STATE_WIN_GOAT)
        Const.stateOk(Const.STATE_WIN_TIGER)
        Const.stateOk(Const.STATE_DRAW)
        self.assertRaises(ValueError,lambda : Const.stateOk(-1))

    def testMark(self):
        Const.markOk(Const.MARK_NONE)
        Const.markOk(Const.MARK_GOAT)
        Const.markOk(Const.MARK_TIGER)

if __name__ == '__main__':
    unittest.main()
