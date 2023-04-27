from abc import ABC

import gym

from src.shields.model_free_shield import ModelFreeShield

class ModelFreeShieldWrapper(gym.Wrapper, ABC):

    def __init__(self, env, shield:ModelFreeShield):
        self.env = env
        self.shield = shield
        self.latest_observation = 1
        super().__init__(env)

    def reset(self):
        return self.env.reset()

    def step(self, cont_action):
        #print("wrapper cont_action", cont_action)
        next_state, reward, done, info = self.env.step(cont_action)
        self.shield.move(info['p1_action'], info['p2_action'])
        self.latest_observation = info['p1_action']
        #print("step latest_observation is", self.latest_observation)
        #print("step", self.shield.state)

        return next_state, reward, done, info

    def get_shield_disabled_actions(self):
        #print("disabled latest_observation is", self.latest_observation)
        #print("disabled", self.shield.state)
        preemptive_action = self.shield.preemptive(self.latest_observation)
        ban_action = self.env.disabled(preemptive_action)
        #print(ban_action, "this is banneed actions")
        return ban_action