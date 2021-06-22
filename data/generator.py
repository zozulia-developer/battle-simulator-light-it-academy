from random import randint, choice, seed
import json


class DataGenerator:
    def __init__(self, seed_value, number_of_armies, strategy_per_army, number_of_squads_per_army, number_of_units_per_squad):
        self.number_of_armies = number_of_armies
        self.strategy_per_army = strategy_per_army
        self.number_of_squads_per_army = number_of_squads_per_army
        self.number_of_units_per_squad = number_of_units_per_squad
        self.data = {"armies": []}
        seed(seed_value)

    def generate(self):
        for army in range(self.number_of_armies):
            self.data["armies"].append({"squads": []})
            self.data["armies"][army].update({"strategy": self.strategy_per_army})
            self.data["armies"][army].update({"name": f'Army #{army+1}'})
            for squad in range(self.number_of_squads_per_army):
                self.data["armies"][army]["squads"].append({"units": []})
                self.data["armies"][army]["squads"][squad].update({"type_unit": choice(["soldiers", "vehicles"])})
                for unit in range(self.number_of_units_per_squad):
                    if self.data["armies"][army]["squads"][squad]["type_unit"] == "soldiers":
                        self.data["armies"][army]["squads"][squad]["units"].append({
                                "health": 100,
                                "recharge": randint(1, 100)
                            })
                    elif self.data["armies"][army]["squads"][squad]["type_unit"] == "vehicles":
                        self.data["armies"][army]["squads"][squad]["units"] \
                            .append({
                                "health": 100,
                                "recharge": randint(1, 100),
                                "operators": [{
                                    "health": 100,
                                    "recharge": randint(1, 100)} for _ in range(randint(1, 3))]
                            })
        with open('data/data.json', 'w') as f:
            json.dump(self.data, f, indent=2)
