from enum import Enum
import gym

from src.model import reactive_system

class EmergencyVehicle(Enum):
    approaching = 1
    away = 0

class HighwayLight(Enum):
    gh = 0
    rh = 1

class FarmLight(Enum):
    gf = 0
    rf = 1

class Obserbations(Enum):
    HIGHWAY = 0
    FARM = 1
    EMERGENCY = 2

class SignalEnv(gym.Env):
    def __init__(self):
        self.WINDOW_SIZE = 600

    def reset(self):
        return 0
    
    def step(self, action_index):
        return 0