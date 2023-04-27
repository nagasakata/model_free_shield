import unittest
import itertools

from benchmarks.water_tank.water_tank_arena import Observations, WaterTankInputOutputManager, \
    WaterTankPropBuilder, AgentActions, EnvironmentActions
from benchmarks.water_tank.water_tank_specifications import safety_formula2
from benchmarks.water_tank.water_tank_stabilizing_shield import WaterTankStabilizingShield



class TestWaterTankArena(unittest.TestCase):

    def test_game(self) -> None:
        shield = WaterTankStabilizingShield(f'WaterTank-c{100}-i{50}-v0', safety_formula2())
        self.assertEqual(shield.game.getPlayer1Alphabet(), [0,1])
        self.assertEqual(shield.game.getPlayer2Alphabet(), [0,1])


    def test_winning_strategy(self) -> None:
        #int(AgentActions.OPEN.value), int(AgentActions.OPEN.value)
        shield = WaterTankStabilizingShield(f'WaterTank-c{100}-i{50}-v0', safety_formula2())
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.OPEN.value)), [int(AgentActions.CLOSE.value), int(AgentActions.OPEN.value),])
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.CLOSE.value)), [int(AgentActions.CLOSE.value), int(AgentActions.OPEN.value)])
        shield.get_wrapper().shield.move(AgentActions.OPEN.value, AgentActions.OPEN.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.OPEN.value)), [int(AgentActions.CLOSE.value), int(AgentActions.OPEN.value)])
        shield.get_wrapper().shield.move(AgentActions.OPEN.value, AgentActions.CLOSE.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.CLOSE.value)), [int(AgentActions.CLOSE.value)])
        shield.get_wrapper().shield.move(AgentActions.CLOSE.value, AgentActions.CLOSE.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.CLOSE.value)), [int(AgentActions.CLOSE.value)])
        shield.get_wrapper().shield.move(AgentActions.CLOSE.value, AgentActions.CLOSE.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.CLOSE.value)), [int(AgentActions.CLOSE.value), int(AgentActions.OPEN.value)])
        shield.get_wrapper().shield.move(AgentActions.CLOSE.value, AgentActions.CLOSE.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.CLOSE.value)), [int(AgentActions.CLOSE.value), int(AgentActions.OPEN.value)])
        shield.get_wrapper().shield.move(AgentActions.CLOSE.value, AgentActions.OPEN.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.OPEN.value)), [int(AgentActions.OPEN.value)])
        shield.get_wrapper().shield.move(AgentActions.OPEN.value, AgentActions.OPEN.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.OPEN.value)), [int(AgentActions.OPEN.value)])
        shield.get_wrapper().shield.move(AgentActions.OPEN.value, AgentActions.OPEN.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.OPEN.value)), [int(AgentActions.CLOSE.value), int(AgentActions.OPEN.value)])
        shield.get_wrapper().shield.move(AgentActions.OPEN.value, AgentActions.OPEN.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.OPEN.value)), [int(AgentActions.CLOSE.value), int(AgentActions.OPEN.value)])
        shield.get_wrapper().shield.move(AgentActions.OPEN.value, AgentActions.CLOSE.value)
        self.assertEqual(shield.get_wrapper().shield.preemptive(int(AgentActions.CLOSE.value)), [int(AgentActions.CLOSE.value)])
