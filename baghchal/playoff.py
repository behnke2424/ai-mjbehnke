from typing import Dict
from agent import Agent
from matchup import Matchup
from stats import Stats

class Playoff:
    def __init__(self, trials : int = 10):
        self._goatAgents : Dict[str,Agent] = dict()
        self._tigerAgents : Dict[str,Agent] = dict()
        self._trials : int = trials

    def addGoatAgent(self,name : str,agent : Agent) -> None:
        self._goatAgents[name]=agent

    def addTigerAgent(self,name : str,agent : Agent) -> None:
        self._tigerAgents[name]=agent

    def play(self):
        for goatAgentName in self._goatAgents:
            for tigerAgentName in self._tigerAgents:
                goatAgent : Agent = self._goatAgents[goatAgentName]
                tigerAgent : Agent = self._tigerAgents[tigerAgentName]
                matchup : Matchup = Matchup()
                matchup.tigerAgent = tigerAgent
                matchup.goatAgent = goatAgent
                stats : Stats = Stats(matchup,self._trials)
                try:
                    stats.playAll()
                    print(f"{goatAgentName} vs. {tigerAgentName}: ")
                    stats.summarize()
                except:
                    print(f"{goatAgentName} vs. {tigerAgentName}: failed")
                    raise


    