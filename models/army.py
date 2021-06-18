from functools import reduce


class Army:
    def __init__(self, squads, strategy, name):
        self.squads = squads
        self.strategy = strategy
        self.name = name

    def is_alive(self):
        return any(squad.is_alive() for squad in self.squads)

    def filter_alive_squads(self):
        self.squads = [squad for squad in self.squads if squad.is_alive()]

    def get_power(self):
        return reduce(lambda a, b: a + b.get_power(), self.squads, 0)
