from enum import Enum
import math
import pprint

from src.model.mdp import MDP
from benchmarks.common.generic import BooleanIOManager

__author__ = "Ezequiel Castellano <ezequiel.castellano@gmail.com>"
__status__ = "experimental"
__version__ = "0.0.1"
__date__ = "02 November 2020"


class AgentActions(Enum):
    RIGHT_GO = 0
    LEFT_GO = 1
    UP_GO = 2


class EnvironmentActions(Enum):
    RIGHT_APPROACH = 0
    LEFT_APPROACH = 1
    UP_APPROACH = 2


class Observations(Enum):
    ACTION_0 = 0
    ACTION_1 = 1
    ACTION_2 = 2
    ACTION_3 = 3
    ACTION_4 = 4
    ACTION_5 = 5
    ACTION_6 = 6
    ACTION_7 = 7


class PacmanInputOutputManager(BooleanIOManager):

    def __init__(self):
        super().__init__(AgentActions, EnvironmentActions, Observations)

    def act0(self, output: int) -> bool:
        return self.evaluate_output(output)(Observations.ACTION_0.name)

    def act1(self, output: int) -> bool:
        return self.evaluate_output(output)(Observations.ACTION_1.name)

    def act2(self, output: int) -> bool:
        return self.evaluate_output(output)(Observations.ACTION_2.name)
    
    def act3(self, output: int) -> bool:
        return self.evaluate_output(output)(Observations.ACTION_3.name)

    def act4(self, output: int) -> bool:
        return self.evaluate_output(output)(Observations.ACTION_4.name)

    def act5(self, output: int) -> bool:
        return self.evaluate_output(output)(Observations.ACTION_5.name)

    def act6(self, output: int) -> bool:
        return self.evaluate_output(output)(Observations.ACTION_6.name)

    def act7(self, output: int) -> bool:
        return self.evaluate_output(output)(Observations.ACTION_7.name)
    
    def is_error(self, output: int) -> bool:
        return self.act7(output)
