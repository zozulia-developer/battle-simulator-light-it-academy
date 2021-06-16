class Squad:
    """Squads are consisted out of a number of units (soldiers or vehicles), that behave as a coherent group

    """

    def __init__(self, type, units):
        self.type = type
        self.units = units

    def success_attack(self):
        return self.units.reduce(lambda a, b: a * b.success_attack(), 1) ** (1 / len(self.units))

    def get_damage(self, dmg):
        dmg = dmg / len(self.units)
        for i in self.units:
            i.get_damage(dmg)

    def start_recharge(self):
        units = self.units.filter(lambda el: el.isReady)
        for el in units:
            el.start_recharge()

    def time_recharge(self):
        units = self.units.filter(lambda el: not el.isReady)
        for el in units:
            el.time_recharge()

    def make_damage(self):
        return self.units.reduce(lambda a, b: a + b.make_damage(), 0)

    def is_alive(self):
        return any(el.is_alive() for el in self.units)

    def filter_alive_units(self):
        self.units = self.units.filter(lambda unit: unit.is_alive())

    def get_power(self):
        return self.units.reduce(lambda a, b: a + b.get_power(), 0)

    def inc_exp_for_units(self):
        for unit in self.units:
            unit.set_experience()
