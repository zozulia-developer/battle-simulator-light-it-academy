from random import randrange


class WeakestStrategy:
    def __init__(self, type_of):
        super(type_of)

    def target(self, assault_army, arr_target):
        target_armies = arr_target.filter(lambda army: assault_army.name != army.name)
        target_army = target_armies.sorted(key=lambda a, b: a.get_power() - b.get_power())[0]
        target_squad = target_army.squads.sorted(key=lambda a, b: a.get_power() - b.get_power())[0]
        return {target_army, target_squad}
