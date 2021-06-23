# -*- coding: utf-8 -*-
""" Module for battle implementation

This module demonstrates battle core.

"""
from random import randint, seed


class Battle:
    """ Battle core

    Args:
        armies(list): data from json.
        seed_value(int): data from json, needed for replays

    """
    def __init__(self, armies: list, seed_value: int):
        self.armies = armies
        seed(seed_value)

    def alive_armies(self) -> None:
        """ Check if armies in list is alive

        """
        self.armies = [army for army in self.armies if army.is_alive()]

    def start(self) -> None:
        """ Implementation of the battle

        """
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
