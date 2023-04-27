import sys
import argparse

from typing import Union, Type


sys.path.append('../../')
from src.wrappers.model_free_shield_wrapper import ModelFreeShieldWrapper
from benchmarks.pacman.pacman_specifications import safety_formula
from benchmarks.common.train_nopy4j import run
from benchmarks.pacman.pacman_callbacks import PacmanShieldingCallback
from benchmarks.pacman.pacman_model_free_shield import PacmanModelFreeShield

from atari_representation_learning_master.atariari.benchmark.wrapper import AtariARIWrapper

def setup_parser() -> argparse.ArgumentParser:
    """
        Define the parser of the arguments
    """
    parser = argparse.ArgumentParser(description='evaluate dynamic shielding with water_tank benchmarks')
    parser.add_argument('--capacity', type=int, default=100,
                        help='the water tank can be initialized with capacity [20 | 50 | 100]')
    parser.add_argument('--steps', type=int, default=int(2e5),
                        help='Number of steps that each environment is run.')
    parser.add_argument('--learning-rate', type=float, default=1e-4,
                        help='Learning rate.')
    parser.add_argument('--shield', type=str, default='model_free',
                        help='the shield to be used [model_free (default) | no]')
    parser.add_argument('--shield-life', type=int, default=10,
                        help='Frequency of shield reconstruction in terms of episodes.')
    parser.add_argument('--depths', nargs='+', default=[1, 3, 5, 7],
                        help='a list of min-depths for dynamic shield (usage: --depths 0 1 3)')
    parser.add_argument('--penalties', nargs='+', default=[10.0],
                        help='a list of penalties that it is used in no shield (usage: --penalties 0.0 1.0 100.0)')
    parser.add_argument('--pdb', type=bool,
                        help='If enabled, pdb will be launched when there is an exception.')
    parser.add_argument('--use-shield-while-learning', type=bool, default=True,
                        help='if you want to use shild while learning, set True')
    parser.add_argument('--use-shield-while-evaluating', type=bool, default=False,
                        help='if you want to use shield while evaluating, set False')
    parser.add_argument('--times', type=int, default=1,
                        help='times you want to repeat')
    parser.add_argument('--ep_length', type=int, default=4000,
                        help='if you want to change the length of episode, change the value of default')

    return parser

def get_game() -> str:
    return f'Pacman-v{0}'

def get_shield(shield) -> Union[None, Type[ModelFreeShieldWrapper]]:
    if shield == 'model_free':
        return PacmanModelFreeShield
    elif shield == 'no':
        return None
    else:
        raise RuntimeError(f'Unknown shields {shield}')

import traceback, pdb

def info(type, value, tb):
    pdb.pm()


if __name__ == "__main__":
    sys.excepthook = info
 
    parser = setup_parser()
    args = parser.parse_args()

    steps = args.steps
    game = get_game()
    shield = get_shield(args.shield)
    learning_rate = args.learning_rate
    shield_life = args.shield_life
    depths = list(map(int, args.depths))
    penalties = list(map(float, args.penalties))
    no_pdb = not args.pdb
    use_shield_while_learning = args.use_shield_while_learning
    use_shield_while_evaluating = args.use_shield_while_evaluating
    times = args.times
    ep_length = args.ep_length

    run(shield=shield,
        ltl_formula=safety_formula(),
        depths=depths,
        game=game,
        callback=PacmanShieldingCallback,
        penalties=penalties,
        total_steps=steps,
        learning_rate=learning_rate,
        shield_life=shield_life,
        use_shield_while_learning=use_shield_while_learning,
        use_shield_while_evaluation=use_shield_while_evaluating,
        times=times,
        ep_length=ep_length)

    sys.exit(0)