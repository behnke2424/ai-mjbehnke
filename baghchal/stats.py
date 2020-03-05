from matchup import Matchup
from const import Const

class Stats:
    DEFAULT_TRIALS : int = 24
    def __init__(self, matchup : Matchup, trials : int = DEFAULT_TRIALS):
        self._matchup : Matchup = matchup
        self._trials : int = trials
        self._goatWins : int = 0
        self._tigerWins : int = 0
        self._draws : int = 0

    def playAll(self) -> None:
        for turn in range(self._trials):
            self._matchup.game.reset()
            while not self._matchup.over:
                self._matchup.turn()
            if self._matchup.game.state == Const.STATE_WIN_GOAT:
                self._goatWins += 1
            elif self._matchup.game.state == Const.STATE_WIN_TIGER:
                self._tigerWins += 1
            else:
                self._draws += 1

    def summarize(self):
        print("goat wins: " + str(self._goatWins) + " tiger wins: " + str(self._tigerWins) + " draws: " + str(self._draws))

        