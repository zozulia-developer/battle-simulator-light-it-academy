from models.BaseStrategy import BaseStrategy


class StrongestStrategy(BaseStrategy):
    def __init__(self, type_of):
        super().__init__(type_of)

    def target(self, assault_army, arr_target):
        print('ass_name', assault_army.name)
        print('arr_t', arr_target)
        # target_armies = [filter(lambda army: assault_army.name != army.name, arr_target)]
        target_armies = [army for army in arr_target if assault_army.name != army.name]
        print('first_t_a', target_armies)
        # print('t_a', sorted([i.get_power() for i in target_armies[0]]))
        # target_army = target_armies.sort(key=lambda a, b: a.get_power() - b.get_power())
        target_army = sorted([i.get_power() for i in target_armies])
        print('len', len(target_army))
        print('ta', target_army)
        target_army = target_army[len(target_army) - 1]
        # print('ta0', [i for i in target_armies[0]])
        # target_squad = target_army.squads.sort(key=lambda a, b: a.get_power() - b.get_power())
        print('armies', target_armies)
        target_squad = sorted([i.get_power() for i in target_armies.squads])
        target_squad = target_squad[len(target_squad) - 1]
        return {target_army, target_squad}
