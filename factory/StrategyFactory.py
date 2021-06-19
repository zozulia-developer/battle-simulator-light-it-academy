from strategy.RandomStrategy import RandomStrategy
from strategy.StrongestStrategy import StrongestStrategy
from strategy.WeakestStrategy import WeakestStrategy


class StrategyFactory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return StrategyFactory()

    def create_strategy(self, data):
        if data == 'random':
            return RandomStrategy(data)
        elif data == 'strongest':
            return StrongestStrategy(data)
        else:
            return WeakestStrategy(data)
