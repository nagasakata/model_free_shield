from src.model.safety_game import SafetyGame

import pprint, copy

# should repair something

def solve_game(game:SafetyGame):
    safe_state = game.safeStates

    action_1 = game.getPlayer1Alphabet() # environment observation
    action_2 = game.getPlayer2Alphabet() # agent action

    while True:
        winning_strategy = dict()
        winning_state = copy.copy(safe_state)

        for (start, p1_now, p2_now) in game.transitions:
            for  p1_action in action_1:
                for p2_action in action_2:
                    if (game.transitions[(start, p1_now, p2_now)], p1_action, p2_action) in game.transitions:
                        if (start, p1_now) in winning_strategy:
                            if not p2_action in winning_strategy[(start, p1_now)]:
                                winning_strategy[(start, p1_now)].append(p2_action)
                        else:
                            winning_strategy[(start, p1_now)] = [p2_action]

        break 
            

        '''
        for q in winning_state:
            for a1 in action_1:
                for a2 in action_2:
                    if (q, a1, a2) in game.transitions:
                        if game.transitions[(q, a1, a2)] in safe_state:
                            if (q, a1) in winning_strategy:
                                winning_strategy[(q, a1)].append(a2)
                            else:
                                winning_strategy[(q, a1)] = [a2]

        if safe_state == winning_state:
            break
        safe_state = winning_state
        '''

    #cpprint.pprint(winning_strategy)

    return winning_state, winning_strategy
