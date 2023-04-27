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


right_go = f'G ({Observations.RIGHT_APPROACH} → X (!{Observations.RIGHT_GO}))'
left_go = f'G ({Observations.LEFT_APPROACH} → X (!{Observations.LEFT_GO}))'
up_go = f'G ({Observations.UP_APPROACH} → X (!{Observations.UP_GO}))'
down_go = f'G ({Observations.DOWN_APPROACH} → X (!{Observations.DOWN_GO}))'

#remove
#if_cant_go = f'G (((!{Observations.RIGHT_GO}) ∧ (!{Observations.LEFT_GO}) ∧ (!{Observations.UP_GO}) ∧ (!{Observations.DOWN_GO})) → !((!{Observations.RIGHT_GO}) ∧ (!{Observations.LEFT_GO}) ∧ (!{Observations.UP_GO}) ∧ (!{Observations.DOWN_GO})))'


def safety_formula():
    return f'({right_go}) ∧ ({left_go}) ∧ ({up_go}) ∧ ({down_go})'