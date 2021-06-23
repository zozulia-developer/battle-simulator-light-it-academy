# -*- coding: utf-8 -*-
""" Module for data generator

This module demonstrates how data is generated.

"""
from random import randint, choice, seed
import json


def make_soldier() -> dict:
    """ Create soldier

    Returns:
        dict: health and recharge data for soldier.

    """
    return {
        "health": 100,
        "recharge": randint(1, 100)
    }


def make_vehicle() -> dict:
    """ Create vehicle

    Returns:
        dict: health, recharge and operators data for vehicle.

    """
    return {
        "health": 100,
        "recharge": randint(1, 100),
        "operators": [{
            "health": 100,
            "recharge": randint(1, 100)} for _ in range(randint(1, 3))]
    }


UNIT_FACTORY = {
    "vehicle": make_vehicle,
    "soldier": make_soldier
}


class DataGenerator:
    """ Create data from config for json file

    Args:
        seed_val(int): data for replays.
        armies(int): number of armies.
        strategy(str): strategy name.
        squads_per_army(int): number of squads.
        units_per_squad(int): number of units.

    """
    def __init__(self, seed_val: int, armies: int, strategy: str, squads_per_army: int, units_per_squad: int):
        self.armies = armies
        self.strategy = strategy
        self.squads_per_army = squads_per_army
        self.units_per_squad = units_per_squad
        self.data = {"armies": []}
        seed(seed_val)

    def generate(self) -> None:
        """ Generate data from config and write it to json file

        """
        armies = self.data["armies"]
        for army_id in range(self.armies):
            squads = []
            army = {
                "squads": squads,
                "strategy": self.strategy,
                "name": f'Army #{army_id+1}'
            }
            armies.append(army)
            for squad in range(self.squads_per_army):
                units = []
                unit_type = choice(["soldiers", "vehicles"])
                squad = {
                    "units": units,
                    "type_unit": unit_type
                }
                squads.append(squad)
                for _ in range(self.units_per_squad):
                    if unit_type == "soldiers":
                        units.append(UNIT_FACTORY["soldier"]())
                    elif unit_type == "vehicles":
                        units.append(UNIT_FACTORY["vehicle"]())

        with open('data/data.json', 'w') as f:
            json.dump(self.data, f, indent=2)
