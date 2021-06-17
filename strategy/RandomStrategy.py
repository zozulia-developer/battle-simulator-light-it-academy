from models.BaseStrategy import BaseStrategy
from random import randrange


class RandomStrategy(BaseStrategy):
    def __init__(self, type_of):
        super().__init__(type_of)

    def target(self, assault_army, arr_target):
        target_armies = [filter(lambda army: assault_army.name != army.name, arr_target)]
        target_army = target_armies[randrange(0, len(target_armies) - 1)]

        target_squad = target_army['squads'][randrange(0, len(target_army['squads']) - 1)]
        return {target_army, target_squad}