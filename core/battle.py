from random import randrange


class Battle:
    armies = []

    def __init__(self, armies):
        self.armies = armies

    def alive_armies(self):
        self.armies = self.armies.filter(lambda army: army.is_alive())

    def start(self):
        while len(self.armies) > 1:
            armies = self.armies
            assault_army = armies[randrange(0, len(armies - 1))]
            assault_squad = assault_army.squads[randrange(0, len(assault_army.squads) - 1)]
            target = assault_army.strategy.target(assault_army, armies)
            target_army = target.target_army
            target_squad = target.target_squad

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
