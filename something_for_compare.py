import gym
from stable_baselines3 import PPO, MYPPO

from atari_representation_learning_master.atariari.benchmark.wrapper import AtariARIWrapper
from benchmarks.pacman.pacman_env import PacmanEnv

from pprint import pprint

from stable_baselines3.common.monitor import Monitor
'''
# 学習環境の準備
game = "Pacman-v0"
env = Monitor(gym.make(game))
'''
env = AtariARIWrapper(gym.make('MsPacmanNoFrameskip-v4'))

# モデルの準備
model = MYPPO('MlpPolicy', env, verbose=1)

# 学習の実行
model.learn(total_timesteps=128000)

# 推論の実行
state = env.reset()
while True:
    # 学習環境の描画
    env.render()

    # モデルの推論
    action, _ = model.predict(state, deterministic=True)

    # 1ステップ実行
    state, rewards, done, info = env.step(action)

    # エピソード完了
    if done:
        break

# 学習環境の解放
env.close()