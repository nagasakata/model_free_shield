from abc import ABC

import gym

from src.shields.model_free_shield import ModelFreeShield

class ModelFreeShieldWrapper(gym.Wrapper, ABC):

    def __init__(self, env, shield:ModelFreeShield):
        self.env = env
        self.shield = shield
        self.latest_observation = 0
        super().__init__(env)

    def reset(self):
        #print("now", self.shield.state, "----------------------------------------------------------------")
        return self.env.reset()

    def step(self, cont_action):
        #print("wrapper cont_action", cont_action)
        next_state, reward, done, info = self.env.step(cont_action)
        self.shield.move(self.latest_observation, cont_action)
        self.latest_observation = info['p1_action']
        #print("step latest_observation is", self.latest_observation)
        #print("step", self.shield.state)

        return next_state, reward, done, info

    def get_shield_disabled_actions(self):
        #print("disabled latest_observation is", self.latest_observation)
        #print("disabled", self.shield.state)
        preemptive_action = self.shield.preemptive(self.latest_observation)
        action_list = self.shield.game.getPlayer2Alphabet()
        ban_action = []
        for action in action_list:
            if not action in preemptive_action:
                ban_action.append(action)
        return ban_action