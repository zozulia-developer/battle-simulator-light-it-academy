from random import randint, seed


class Battle:
    armies = []

    def __init__(self, armies: dict):
        self.armies = armies
        seed(228)  # for replays

    def alive_armies(self) -> None:
        self.armies = [army for army in self.armies if army.is_alive()]

    def start(self) -> None:
        while len(self.armies) > 1:
            armies = self.armies
            assault_army = armies[randint(0, len(armies) - 1)]
            assault_squad = assault_army.squads[randint(0, len(assault_army.squads) - 1)]
            target = assault_army.strategy.target(assault_army, armies)
            target_army = target['target_army']
            target_squad = target['target_squad']

            if assault_squad.success_attack() > target_squad.success_attack():
                damage = assault_squad.make_damage()
                assault_squad.start_recharge()
                target_squad.get_damage(damage)
                assault_squad.time_recharge()
                assault_squad.inc_exp_for_units()
                target_squad.filter_alive_units()
                target_army.filter_alive_squads()
                self.alive_armies()

        print(f'{self.armies[0].name} is Winner!')
