from models.BaseStrategy import BaseStrategy


class StrongestStrategy(BaseStrategy):
    def __init__(self, type_of):
        super().__init__(type_of)

    def target(self, assault_army, arr_target):
        print('ass_name', assault_army.name)
        print('arr_t', arr_target)
        print('arr_t+', arr_target[0].squads[0].type_of)
        target_armies = [filter(lambda army: assault_army.name != army.name, arr_target)]
        print('t_a', [i.get_power() for i in target_armies[0]])
        target_army = target_armies.sort(key=lambda a, b: a.get_power() - b.get_power())
        target_army = target_army[len(target_army) - 1]
        target_squad = target_army.squads.sort(key=lambda a, b: a.get_power() - b.get_power())
        target_squad = target_squad[len(target_squad) - 1]
        return {target_army, target_squad}
