from typing import List, Tuple, Dict, Set
from src.model import DFA, SafetyGame

import numpy as np

import pprint


def dfa_to_game(dfa:DFA, player1:list, player2:list):
    player1_dict = assign_int(player1)
    player2_dict = assign_int(player2)

    new_transition = assign_transition(dfa.transitions, player1_dict, player2_dict, player1, player2)

    return_game = SafetyGame(list(player1_dict.keys()), list(player2_dict.keys()))
    return_game.setSafeStates(dfa.safeStates)
    return_game.setTransitions({})
    for start in new_transition:
        for trans in new_transition[start]:
            return_game.add_transition(start, trans[0], trans[1], new_transition[start][trans])


    return return_game

def assign_int(proposition:list):

    transition_dict = dict()
    pro_length = len(proposition)

    for i in range(np.power(2, pro_length)):
        transition_dict[i] = dict()
        i_sub = i
        for j in range(pro_length):
            if np.power(2, (pro_length - j - 1)) <= i_sub:
                transition_dict[i][proposition[j]] = True
                i_sub = i_sub - np.power(2, (pro_length - j - 1))
            else:
                transition_dict[i][proposition[j]] = False

    return transition_dict

def assign_transition(transitions:dict, player1:dict, player2:dict, player1_alphabet:list, player2_alphabet:list):
    pprint.pprint(player1)
    pprint.pprint(player2)
    trans_len = 0
    player1_trans_dict, player2_trans_dict, return_trans_dict = dict(), dict(), dict()

    for start_state in transitions:
        return_trans_dict[start_state] = {}
        for pro_bool in transitions[start_state]:
            will_translate_sub, will_translate = [], []
            will_translate_sub.append(dict(pro_bool))

            for trans_sub in will_translate_sub:
                for alphabet1 in player1_alphabet:
                    if alphabet1 not in trans_sub:
                        add_trans_true = dict(trans_sub, **{alphabet1:True})
                        add_trans_false = dict(trans_sub, **{alphabet1:False})
                        will_translate_sub.append(add_trans_true)
                        will_translate_sub.append(add_trans_false)
                        break

            for trans_sub in will_translate_sub:
                for alphabet2 in player2_alphabet:
                    if alphabet2 not in trans_sub:
                        add_trans_true = dict(trans_sub, **{alphabet2:True})
                        add_trans_false = dict(trans_sub, **{alphabet2:False})
                        will_translate_sub.append(add_trans_true)
                        will_translate_sub.append(add_trans_false)
                        if len(add_trans_false) >= trans_len:
                            trans_len = len(add_trans_false)
                        break

            for trans in will_translate_sub:
                if len(trans) == trans_len:
                    will_translate.append(trans)

            for i in will_translate:
                for trans_now in i:
                    if trans_now in player1_alphabet:
                        player1_trans_dict[trans_now] = i[trans_now]
                    if trans_now in player2_alphabet:
                        player2_trans_dict[trans_now] = i[trans_now]

                for player1_assigned in player1:
                    if player1_trans_dict == player1[player1_assigned]:
                        for player2_assigned in player2:
                            if player2_trans_dict == player2[player2_assigned]:
                                return_trans_dict[start_state][(player1_assigned, player2_assigned)] = transitions[start_state][pro_bool]
                            else:
                                continue
                            break
                    else:
                        continue
                    break

    return return_trans_dict

def get_assigned_transition(dfa:DFA, player1:list, player2:list):
    player1_dict = assign_int(player1)
    player2_dict = assign_int(player2)

    return player1_dict, player2_dict
