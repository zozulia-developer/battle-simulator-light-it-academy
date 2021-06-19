from models.BaseStrategy import BaseStrategy
from random import randint


class RandomStrategy(BaseStrategy):
    def __init__(self, type_of):
        super().__init__(type_of)

    def target(self, assault_army, arr_target):
        target_armies = [army for army in arr_target if assault_army.name != army.name]
        target_army = target_armies[randint(0, len(target_armies) - 1)]

        target_squad = target_army.squads[randint(0, len(target_army.squads) - 1)]
        return {'target_army': target_army, 'target_squad': target_squad}
