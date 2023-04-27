import gym
import pprint
from atariari.benchmark.wrapper import AtariARIWrapper
env = AtariARIWrapper(gym.make('MsPacmanNoFrameskip-v4'))
obs = env.reset()
obs, reward, done, info = env.step(1)
print(obs)
print(reward)
print(done)
pprint.pprint(info)