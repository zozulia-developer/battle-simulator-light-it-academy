import json
from core.battle import Battle
from factory.ArmyFactory import ArmyFactory


class MainApp:
    @staticmethod
    def main():
        with open("data/data.json", "r") as f:
            data = json.load(f)

        armies_factory = ArmyFactory.get_instance()
        arr_armies = armies_factory.create_armies(data['armies'])
        battle = Battle(arr_armies)
        battle.start()


if __name__ == "__main__":
    MainApp.main()
