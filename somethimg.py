from benchmarks.pacman.pacman_specifications import safety_formula_try
from src.logic.ltl2dfa_translator import ltl_to_dfa_spot
from src.logic.dfa2game_translator import dfa_to_game
from src.logic.solve_game import solve_game

from pprint import pprint

dfa = ltl_to_dfa_spot(safety_formula_try())
pprint(dfa)

game = dfa_to_game(dfa, ['LEFT_APPROACH', 'RIGHT_APPROACH'], ['LEFT_GO', 'RIGHT_GO'])
pprint(game)

solved_game = solve_game(game)
pprint(solved_game)