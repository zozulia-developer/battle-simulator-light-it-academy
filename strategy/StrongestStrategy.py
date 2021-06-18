from models.BaseStrategy import BaseStrategy


class StrongestStrategy(BaseStrategy):
    def __init__(self, type_of):
        super().__init__(type_of)

    def target(self, assault_army, arr_target):
        target_armies = [army for army in arr_target if assault_army.name != army.name]
        target_army = sorted(target_armies, key=lambda army: army.get_power(), reverse=True)[0]
        target_squad = sorted(target_army.squads, key=lambda squad: squad.get_power(), reverse=True)[0]
        return {'target_army': target_army, 'target_squad': target_squad}
