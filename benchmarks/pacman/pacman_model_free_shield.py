import pprint

import gym
from atari_representation_learning_master.atariari.benchmark.wrapper import AtariARIWrapper
from stable_baselines3.common.monitor import Monitor

from src.logic.dfa2game_translator import dfa_to_game
from src.logic.ltl2dfa_translator import ltl_to_dfa_spot
from src.logic.solve_game import  solve_game
from src.wrappers.model_free_shield_wrapper import ModelFreeShieldWrapper
from src.shields.model_free_shield import ModelFreeShield

class PacmanModelFreeShield:
    def __init__(self, env, ltl_formula):
        self.env = env

        self.game = dfa_to_game(ltl_to_dfa_spot(ltl_formula), 
                                ["LEFT_APPROACH", "RIGHT_APPROACH", "UP_APPROACH", "DOWN_APPROACH", "LEFT_WALL", "RIGHT_WALL", "UP_WALL", "DOWN_WALL"],
                                ["LEFT_GO", "RIGHT_GO", "UP_GO", "DOWN_GO", "NO_MOVE"])

        solved_game = solve_game(self.game)

        count, i_sub = 0, 0
        winning_strategy = {}
        for i in range(15):
            for j in range(255):
                if (i+1, j) in solved_game[1]:
                    winning_strategy[(i+1, j)] = solved_game[1][(i+1, j)]
                else:
                    winning_strategy[(i+1, j)] = [1]
                    self.game.add_transition(i+1, j, 1, i+1)
        
        pprint.pprint(vars(self.game))

        pprint.pprint(winning_strategy)
        print("THIS IS SSS")

        train_env = Monitor(gym.make(env))
        train_env.env._max_episode_steps = 4000

        self.wrapper = ModelFreeShieldWrapper(train_env, ModelFreeShield(self.game, solved_game[0], winning_strategy))


    def get_wrapper(self):
        return self.wrapper
