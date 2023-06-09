import unittest
from pprint import pprint

from src.wrappers.model_free_shield_wrapper import ModelFreeShieldWrapper
from src.shields.model_free_shield import ModelFreeShield
from src.logic.dfa2game_translator import dfa_to_game
from src.logic.ltl2dfa_translator import ltl_to_dfa_spot
from benchmarks.pacman.pacman_specifications import safety_formula_try

class TestPacman(unittest.TestCase):
    """
    test the behave of the pacman
    """

    def test_pacman_move(self):
        dfa = ltl_to_dfa_spot(safety_formula_try())
        pprint(dfa.transitions)

        game = dfa_to_game(dfa, ['LEFT_APPROACH', 'RIGHT_APPROACH', 'LEFT_WALL', 'RIGHT_WALL'], ['LEFT_GO', 'RIGHT_GO'])
        pprint(game.transitions)

        self.assertEqual(game.getStates(), [1, 2, 3, 4])


if __name__ == "__main__":
        unittest.main()
