import gym
from atari_representation_learning_master.atariari.benchmark.wrapper import AtariARIWrapper
env = AtariARIWrapper(gym.make('MsPacmanNoFrameskip-v4'))
obs = env.reset()

count = 0

for _ in range(10000):
    observation, reward, terminated, info = env.step(env.action_space.sample())

    print(info['lives'], info['labels']['player_x'], info['labels']['player_y'], terminated, count)

    count += 1

    if terminated:
        env.reset()

env.close()