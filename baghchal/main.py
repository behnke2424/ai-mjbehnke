from hungrytigeragent import HungryTigerAgent
from game import Game
import random
from matchup import Matchup
from hungrytigeragent import HungryTigerAgent
from scaredgoatagent import ScaredGoatAgent
from stats import Stats
from playoff import Playoff
from elusiveGoatAgent import elusiveGoatAgent
from congoat import ConserveGoatAgent
from aggressivegoatagent import AggressiveGoatAgent
from sidehugginggoat import SideHuggingGoat
from SmartGoatAgent import SmartGoatAgent
from randomagent import RandomAgent
from const import Const
from goatAgrosAgent import GoatAgrosAgent
from occamsgoatagent import OccamsGoatAgent
from minmaxagent import MinMaxAgent

game = Game()
playoff = Playoff(trials = 1000)

# playoff.addGoatAgent("elusive goat",elusiveGoatAgent(game))
# playoff.addGoatAgent("conservative goat",ConserveGoatAgent(game))
# playoff.addGoatAgent("aggressive goat", AggressiveGoatAgent(game))
# playoff.addGoatAgent("side hugging goat", SideHuggingGoat(game))
playoff.addGoatAgent("smart goat", SmartGoatAgent(game))
# playoff.addGoatAgent("agros goat",GoatAgrosAgent(game))
# playoff.addGoatAgent("occams goat",OccamsGoatAgent(game))
# playoff.addGoatAgent("random goat",RandomAgent(game,Const.MARK_GOAT))
# playoff.addGoatAgent("minmax 1 goat",MinMaxAgent(game=game,side=Const.MARK_GOAT,maxDepth=1))
#playoff.addGoatAgent("minmax 2 goat",MinMaxAgent(game=game,side=Const.MARK_GOAT,maxDepth=2))
#playoff.addGoatAgent("minmax 3 goat",MinMaxAgent(game=game,side=Const.MARK_GOAT,maxDepth=3))

# playoff.addTigerAgent("random tiger",RandomAgent(game,Const.MARK_TIGER))
playoff.addTigerAgent("hungry tiger",HungryTigerAgent(game))
# playoff.addGoatAgent("minmax 1 tiger",MinMaxAgent(game=game,side=Const.MARK_TIGER,maxDepth=1))
# playoff.addGoatAgent("minmax 2 tiger",MinMaxAgent(game=game,side=Const.MARK_TIGER,maxDepth=2))
# playoff.addGoatAgent("minmax 3 tiger",MinMaxAgent(game=game,side=Const.MARK_TIGER,maxDepth=3))

playoff.play()
