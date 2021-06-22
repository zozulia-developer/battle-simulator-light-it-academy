import json
from core.battle import Battle
from factory.ArmyFactory import ArmyFactory
from data import generator


class MainApp:
    @staticmethod
    def main():
        with open("config.json", "r") as f:
            cfg = json.load(f)

        generate_info = generator.DataGenerator(
            cfg["seed"],
            cfg["number_of_armies"],
            cfg["strategy_per_army"],
            cfg["number_of_squads_per_army"],
            cfg["number_of_units_per_squad"])
        generate_info.generate()

        with open("data/data.json", "r") as f:
            data = json.load(f)

        armies_factory = ArmyFactory.get_instance()
        arr_armies = armies_factory.create_armies(data['armies'])
        battle = Battle(arr_armies, cfg["seed"])
        battle.start()


if __name__ == "__main__":
    MainApp.main()
