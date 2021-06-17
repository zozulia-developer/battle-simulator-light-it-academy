class Army:
    def __init__(self, squads, strategy, name):
        self.squads = squads
        self.strategy = strategy
        self.name = name

    def is_alive(self):
        return any(squad.is_alive() for squad in self.squads)

    def filter_alive_squads(self):
        self.squads = self.squads.filter(lambda squad: squad.is_alive())

    def get_power(self):
        return self.squads.reduce(lambda a, b: a + b.het_power(), 0)
