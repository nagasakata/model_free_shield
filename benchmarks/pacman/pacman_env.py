from pprint import pprint
import gym

from atari_representation_learning_master.atariari.benchmark.wrapper import AtariARIWrapper
from benchmarks.common.evaluate import LOGGER
from benchmarks.pacman.pacman_arena import PacmanInputOutputManager
from benchmarks.pacman.pacman_specifications import safety_formula
from src.logic.dfa2game_translator import get_assigned_transition
from src.logic.ltl2dfa_translator import ltl_to_dfa_spot

class PacmanEnv(gym.Env):

    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self):
        super(PacmanEnv, self).__init__()
        self.env = AtariARIWrapper(gym.make('MsPacmanNoFrameskip-v4'))
        self.env.reset()
        self.penalty = 1.0
        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space
        self.io_manager = PacmanInputOutputManager()
        self.action_assign = get_assigned_transition(ltl_to_dfa_spot(safety_formula()), 
                                                          ["LEFT_APPROACH", "RIGHT_APPROACH", "UP_APPROACH", "DOWN_APPROACH", "LEFT_WALL", "RIGHT_WALL", "UP_WALL", "DOWN_WALL"], 
                                                          ["LEFT_GO", "RIGHT_GO", "UP_GO", "DOWN_GO"])
        self.die = 0
        self.max_score = 0
        self.lives_before = 3
        self.score = 0
        self.count = 0
    
    def reset(self):
        LOGGER.debug('Resetting')
        return self.env.reset()
        

    def set_penalty(self, penalty: float):
        assert penalty >= 1.0
        self.penalty = penalty
        print("hey set_penalty")


    def _seed(seed=None):
        print("hey _seed")


    def decode(state):
        print("hey decode")


    def render(self, mode='human'):
        print("hey render")

    def _change_is_possible(self):
        print("hey _change_is_possible")

    def valid_move(self, p1_action):
        print("hey valid_model")

    def step(self, player1_action_int: int):
        print("hey! hey!")
        observation, reward, done, info = self.env.step(player1_action_int)
        self.count += 1
        #print(self.count, "回目")

        if info['lives'] < self.lives_before:
            self.die += 1
            self.lives_before = info['lives']
            print("pacman is dead TAT")
        elif info['lives'] == 3:
            self.lives_before = 3

        if info['labels']['player_score'] > self.max_score:
            self.max_score = info['labels']['player_score']

        self.score = info['labels']['player_score']

        player_position = (info['labels']['player_x'], info['labels']['player_y'])

        enemy_position_list = [(info['labels']['enemy_sue_x'], info['labels']['enemy_sue_y']),
                               (info['labels']['enemy_inky_x'], info['labels']['enemy_inky_y']),
                               (info['labels']['enemy_pinky_x'], info['labels']['enemy_pinky_y']),
                               (info['labels']['enemy_blinky_x'], info['labels']['enemy_blinky_y'])]
        
        allowed_side, allowed_vertival, allowed_side2, allowed_vertival2 = 15, 15, 10, 10
        assigned_transition_dict = {'LEFT_APPROACH': False, 'RIGHT_APPROACH': False,
                                    'UP_APPROACH': False, 'DOWN_APPROACH': False,
                                    'LEFT_WALL': False, 'RIGHT_WALL': False,
                                    'UP_WALL':False, 'DOWN_WALL': False}

        for pos in enemy_position_list:
            if (player_position[0] < pos[0]) & (pos[0] - player_position[0] < allowed_side) and (abs(pos[1] - player_position[1]) < allowed_vertival2):
                assigned_transition_dict['RIGHT_APPROACH'] = True
            if (player_position[0] > pos[0]) & (player_position[0] - pos[0] < allowed_side) and (abs(pos[1] - player_position[1]) < allowed_vertival2):
                assigned_transition_dict['LEFT_APPROACH'] = True
            if (player_position[1] < pos[1]) & (pos[1] - player_position[1] < allowed_vertival) and (abs(pos[0] - player_position[0]) < allowed_side2):
                assigned_transition_dict['DOWN_APPROACH'] = True
            if (player_position[1] > pos[1]) & (player_position[1] - pos[1] < allowed_vertival) and (abs(pos[0] - player_position[0]) < allowed_side2):
                assigned_transition_dict['UP_APPROACH'] = True
        

        print(observation[player_position[1]-1][player_position[0] - 12][0], observation[player_position[1]-1][player_position[0]-5])
        print(observation[player_position[1]+12][player_position[0] - 12][0], observation[player_position[1]+12][player_position[0]-5][0])
        print(observation[player_position[1]][player_position[0] - 13][0], observation[player_position[1]+11][player_position[0]-13][0])
        print(observation[player_position[1]][player_position[0] - 4][0], observation[player_position[1]+11][player_position[0]-4][0])
        if (observation[player_position[1]-1][player_position[0] - 12][0] == 228) or (observation[player_position[1]-1][player_position[0]-5][0]) == 228:
            assigned_transition_dict['UP_WALL'] = True

        if (observation[player_position[1]+12][player_position[0] - 12][0] == 228) or (observation[player_position[1]+12][player_position[0]-5][0] == 228):
            assigned_transition_dict['DOWN_WALL'] = True

        if (observation[player_position[1]][player_position[0] - 13][0] == 228) or (observation[player_position[1]+11][player_position[0]-13][0] == 228):
            assigned_transition_dict['LEFT_WALL'] = True

        if (observation[player_position[1]][player_position[0] - 4][0] == 228) or (observation[player_position[1]+11][player_position[0]-4][0] == 228):
            assigned_transition_dict['RIGHT_WALL'] = True


        print("pacman position", player_position, "enemy position", enemy_position_list, player1_action_int)
        print(assigned_transition_dict)

        for i in self.action_assign[0]:
            if self.action_assign[0][i] == assigned_transition_dict:
                info['p1_action'] = i
                print(self.action_assign[0][i])
                break

        cont_action_dict = {'LEFT_GO': False, 'RIGHT_GO': False,
                            'UP_GO': False, 'DOWN_GO': False}
        if player1_action_int == 0:
            pass
        elif player1_action_int == 1:
            cont_action_dict['UP_GO'] = True
        elif player1_action_int == 2:
            cont_action_dict['RIGHT_GO'] = True
        elif player1_action_int == 3:
            cont_action_dict['LEFT_GO'] = True
        elif player1_action_int == 4:
            cont_action_dict['DOWN_GO'] = True
        elif player1_action_int == 5:
            cont_action_dict['UP_GO'] = True
            cont_action_dict['RIGHT_GO'] = True
        elif player1_action_int == 6:
            cont_action_dict['UP_GO'] = True
            cont_action_dict['LEFT_GO'] = True
        elif player1_action_int == 7:
            cont_action_dict['DOWN_GO'] = True
            cont_action_dict['RIGHT_GO'] = True
        elif player1_action_int == 8:
            cont_action_dict['DOWN_GO'] = True
            cont_action_dict['LEFT_GO'] = True

        for i in self.action_assign[1]:
            if self.action_assign[1][i] == cont_action_dict:
                info['p2_action'] = i
                break

        '''
        infoで返すべき情報
        現在の敵と自分の位置関係に対応するenvironment action
        '''
        return observation, reward, done, info
    

    def disabled(self, action_list):
        forgive_action_list = []
        action_dict = {0:[], 1:['UP_GO'], 2:['RIGHT_GO'], 3:['LEFT_GO'], 4:['DOWN_GO'], 5:['UP_GO', 'RIGHT_GO'], 6:['UP_GO', 'LEFT_GO'], 7:['DOWN_GO', 'RIGHT_GO'], 8:['DOWN_GO', 'LEFT_GO']}
        
        for preemptive in action_list:
            sub_action = []
            for j in action_dict:
                sub_action.append(j)
            now_preemptive = self.action_assign[1][preemptive]
            for key_act in now_preemptive:
                if now_preemptive[key_act]:
                    pass
                else:
                    for i in action_dict:
                        if key_act in action_dict[i]:
                            if i in sub_action:
                                sub_action.remove(i)
            for forgive_action in sub_action:
                if forgive_action not in forgive_action_list:
                    forgive_action_list.append(forgive_action)

        ban_action = []
        
        for act in list(action_dict.keys()):
            if act not in forgive_action_list:
                ban_action.append(act)

        print(ban_action)

        return ban_action
