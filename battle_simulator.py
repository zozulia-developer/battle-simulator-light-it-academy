# -*- coding: utf-8 -*-
""" Battle simulator

This simulator is supposed to determine a battle outcome based on probability calculations.
Once the simulator is started all the army squads will start attacking each other until there is only one army left.

Example:
        $ python battle_simulator.py

"""
import json
from core.battle import Battle
from factory.army_factory import ARMY_FACTORY
from data import generator


class MainApp:
    """ MainApp

    """
    @staticmethod
    def main() -> None:
        """ Main implementation

        """
        with open("config.json", "r") as file:
            cfg = json.load(file)

        generate_info = generator.DataGenerator(
            cfg["seed"],
            cfg["number_of_armies"],
            cfg["strategy_per_army"],
            cfg["number_of_squads_per_army"],
            cfg["number_of_units_per_squad"])
        generate_info.generate()

        with open("data/data.json", "r") as file:
            data = json.load(file)

        arr_armies = ARMY_FACTORY.create_armies(data['armies'])
        battle = Battle(arr_armies, cfg["seed"])
        battle.start()


if __name__ == "__main__":
    MainApp.main()
