import os
import sys
from factory.SquadFactory import SquadFactory
from models.army import Army
from factory.StrategyFactory import StrategyFactory

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class ArmyFactory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

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
