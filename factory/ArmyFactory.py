import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from factory.SquadFactory import SquadFactory
from models.army import Army
from factory.StrategyFactory import StrategyFactory

instance = None


class ArmyFactory:
    def __init__(self):
        if instance:
            pass
        else:
            self.instance = instance

    @staticmethod
    def get_instance():
        return ArmyFactory()

    def create_army(self, data):
        squads = SquadFactory.get_instance()
        squads = squads.create_squads(data['squads'])

        strategy = StrategyFactory.get_instance()
        strategy = strategy.create_strategy(data['strategy'])

        return Army(squads, strategy, data['name'])

    def create_armies(self, arr):
        return [self.create_army(i) for i in arr]
