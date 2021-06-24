# -*- coding: utf-8 -*-
""" Module for battle implementation

This module demonstrates battle core.

"""
import logging
from time import time
from random import randint, seed

logging.basicConfig(filename='./battle.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S', level=logging.INFO)


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
        iteration = 0
        start_time = time()
        logging.info('--- The Battle begin!!! ---')
        while len(self.armies) > 1:
            armies = self.armies
            assault_army = armies[randint(0, len(armies) - 1)]
            assault_squad = assault_army.squads[randint(0, len(assault_army.squads) - 1)]
            target = assault_army.strategy.target(assault_army, armies)
            target_army = target['target_army']
            target_squad = target['target_squad']
            iteration += 1
            logging.info(f"Iteration #{iteration}")
            logging.info(f"{assault_army.name} attack --> {target_army.name}\n")

            if assault_squad.success_attack() > target_squad.success_attack():
                damage = assault_squad.make_damage()
                assault_squad.start_recharge()
                target_squad.get_damage(damage)
                assault_squad.time_recharge()
                assault_squad.inc_exp_for_units()
                target_squad.filter_alive_units()
                target_army.filter_alive_squads()
                self.alive_armies()
        end_time = time()
        logging.info(f'{self.armies[0].name} is Winner!')
        logging.info(f'Battle time: {end_time - start_time:.2f}sec')
        print(f'{self.armies[0].name} is Winner!')
