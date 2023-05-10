from abc import ABCMeta
import sys
from typing import Set, Dict, List
from src.model.safety_game import SafetyGame

import copy


class ModelFreeShield(metaclass=ABCMeta):
    def __init__(self, game:SafetyGame, win_set:Set[int], win_strategy:Dict[int, List[int]]) -> None:
        self.game = game
        self.win_set = win_set
        self.win_strategy = win_strategy
        self.s = self.game.getInitialState()
        self.count = 0
        self.reset()

    def reset(self):    
        self.state = self.game.getInitialState()

    def preemptive(self, action):
        print(self.state, action)
        print(self.state, action, "next, you can use", self.win_strategy[(self.state, action)])
        #self.s = copy.copy(self.state)
        #print("self.s is", self.s)
        #print("preemptive", action)
        return self.win_strategy[(self.state, action)]

    def move(self, env_action, cont_action):
        print("state", self.state, "env_action", env_action, "cont_action", cont_action)
        '''
        if self.s != self.state:
            print("self.state is", self.state, "self.s is", self.s)
            sys.exit()
        '''
        self.state = self.game.getSuccessor(self.state, env_action, cont_action)
