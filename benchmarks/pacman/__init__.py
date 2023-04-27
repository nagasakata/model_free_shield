from gym.envs.registration import register

register(
    id='Pacman-v0',
    max_episode_steps=1000,
    entry_point='benchmarks.pacman.pacman_env:PacmanEnv'
)