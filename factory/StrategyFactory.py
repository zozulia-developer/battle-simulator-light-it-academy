from strategy.RandomStrategy import RandomStrategy
from strategy.StrongestStrategy import StrongestStrategy
from strategy.WeakestStrategy import WeakestStrategy

instance = None


class StrategyFactory:
    def __init__(self):
        if instance:
            pass
        else:
            self.instance = instance

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
