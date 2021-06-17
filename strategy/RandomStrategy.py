from random import randrange

class RandomStrategy:
    def __init__(self, type_of):
        super(type_of)

    def target(self, assault_army, arr_target):
        target_armies = arr_target.filter(lambda army: assault_army.name != army.name)
        target_army = target_armies[randrange(0, len(target_armies) - 1)]

        target_squad = target_army.squads[randrange(0, len(target_army.squads) - 1)]
        return {target_army, target_squad}