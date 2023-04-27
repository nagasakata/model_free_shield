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

        self.game = dfa_to_game(ltl_to_dfa_spot(ltl_formula), ["LEFT_APPROACH", "RIGHT_APPROACH", "UP_APPROACH", "DOWN_APPROACH"],["LEFT_GO", "RIGHT_GO", "UP_GO", "DOWN_GO"])
        solved_game = solve_game(self.game)

        pprint.pprint(solved_game[1])

        train_env = Monitor(gym.make(env))
        train_env.env._max_episode_steps = 4000

        self.wrapper = ModelFreeShieldWrapper(train_env, ModelFreeShield(self.game, solved_game[0], solved_game[1]))


    def get_wrapper(self):
        return self.wrapper