from models.BaseStrategy import BaseStrategy


class WeakestStrategy(BaseStrategy):
    def __init__(self, type_of):
        super().__init__(type_of)

    def target(self, assault_army, arr_target):
        # target_armies = arr_target.filter(lambda army: assault_army.name != army.name)
        target_armies = [filter(lambda army: assault_army.name != army.name, arr_target)]
        target_army = target_armies.sort(key=lambda a, b: a.get_power() - b.get_power())[0]
        target_squad = target_army.squads.sort(key=lambda a, b: a.get_power() - b.get_power())[0]
        return {target_army, target_squad}
