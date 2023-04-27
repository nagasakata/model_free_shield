import pprint

import gym
from stable_baselines3.common.monitor import Monitor

from src.logic.dfa2game_translator import dfa_to_game
from src.logic.ltl2dfa_translator import ltl_to_dfa_spot
from src.logic.solve_game import  solve_game
from src.wrappers.model_free_shield_wrapper import ModelFreeShieldWrapper
from src.shields.model_free_shield import ModelFreeShield


class WaterTankModelFreeShield:

    def __init__(self, env, ltl_formula):
        self.env = env
        self.ltl_formula = ltl_formula
        self.game = dfa_to_game(ltl_to_dfa_spot(ltl_formula), ['OPEN'], ['OPEN'])

        pprint.pprint(self.game.transitions)

        modified_transition = dict()
        modified_transition[(1,0,0)] = 2
        modified_transition[(1,0,1)] = 3
        modified_transition[(1,1,0)] = 2
        modified_transition[(1,1,1)] = 3
        print(modified_transition, "this is modified")

        for i in self.game.transitions:
            for j in self.game.transitions:
                if (self.game.transitions[i] == j[0]) & (not (j[0], i[2], j[1]) in modified_transition):
                    modified_transition[(j[0], i[2], j[1])] = self.game.transitions[j]
           
        pprint.pprint(modified_transition)

        self.game.setTransitions(modified_transition)
        solved_game = solve_game(self.game)

        print("this is win_strategy")
        print(solved_game[1])

        '''
        new_win_strategy = dict()
        for (start, action_1) in solved_game[1]:
            for j in solved_game[1][(start, action_1)]:
                if (start, action_1, j) in modified_transition:
                    new_win_strategy[(start, j)] = solved_game[1][(modified_transition[start, action_1, j], j)]
        '''
                    
        pprint.pprint(vars(self.game))

        print("yahho")
        #pprint.pprint(new_win_strategy)

        #self.wrapper = Monitor(gym.make(env))
        self.wrapper = ModelFreeShieldWrapper(Monitor(gym.make(env)), ModelFreeShield(self.game, solved_game[0], solved_game[1]))


    def get_wrapper(self):
        return self.wrapper