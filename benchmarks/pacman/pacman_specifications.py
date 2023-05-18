from enum import Enum

class Observations(Enum):
    RIGHT_APPROACH = 0    # valve is open
    LEFT_APPROACH = 1   # water level <= 0
    UP_APPROACH = 2    # water level >= capacity
    DOWN_APPROACH = 3
    RIGHT_GO = 4
    LEFT_GO = 5
    UP_GO = 6
    DOWN_GO = 7
    RIGHT_WALL = 8
    LEFT_WALL = 9
    UP_WALL = 10
    DOWN_WALL = 11
    NO_MOVE = 12



right_go = f'G ({Observations.RIGHT_APPROACH} → X ((!{Observations.RIGHT_GO}) ∧ ({Observations.NO_MOVE})))'
left_go = f'G ({Observations.LEFT_APPROACH} → X ((!{Observations.LEFT_GO}) ∧ ({Observations.NO_MOVE})))'
up_go = f'G ({Observations.UP_APPROACH} → X ((!{Observations.UP_GO}) ∧ ({Observations.NO_MOVE})))'
down_go = f'G ({Observations.DOWN_APPROACH} → X ((!{Observations.DOWN_GO}) ∧ ({Observations.NO_MOVE})))'

enemy_approach = f'({right_go}) ∧ ({left_go}) ∧ ({up_go}) ∧ ({down_go})'

right_wall = f'G ({Observations.RIGHT_WALL} → X ((!{Observations.RIGHT_GO}) ∧ ({Observations.NO_MOVE})))'
left_wall = f'G ({Observations.LEFT_WALL} → X ((!{Observations.LEFT_GO}) ∧ ({Observations.NO_MOVE})))'
up_wall = f'G ({Observations.UP_WALL} → X ((!{Observations.UP_GO}) ∧ ({Observations.NO_MOVE})))'
down_wall = f'G ({Observations.DOWN_WALL} → X ((!{Observations.DOWN_GO}) ∧ ({Observations.NO_MOVE})))'

wall_is_there = f'({right_wall}) ∧ ({left_wall}) ∧ ({up_wall}) ∧ ({down_wall})'

#no_move = f'G({Observations.NO_MOVE})'

#remove
#if_cant_go = f'G ((({Observations.RIGHT_APPROACH} ∨ {Observations.RIGHT_WALL}) ∧ ({Observations.LEFT_APPROACH} ∨ {Observations.LEFT_WALL}) ∧ ({Observations.UP_APPROACH} ∨ {Observations.UP_WALL}) ∧ ({Observations.DOWN_APPROACH} ∨ {Observations.DOWN_WALL})) → X (({Observations.RIGHT_GO}) ∨ ({Observations.LEFT_GO}) ∨ ({Observations.UP_GO}) ∨ ({Observations.DOWN_GO})))'


def safety_formula():
    return f'({enemy_approach}) ∧ ({wall_is_there})'

def safety_formula_try():
    return f'({right_go}) ∧ ({left_go})'
