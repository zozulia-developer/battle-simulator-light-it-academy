from random import randrange


class Unit:
    """Each unit represents either a soldier or a vehicle maned by a predetermined number of soldiers.
    """
    def __init__(self):
        self.health = 100  # Represents the health of the unit
        self.recharge = range(100, 2000)  # Represents the number of ms required to recharge the unit for an attack


class Soldier(Unit):
    """Soldiers are units that have an additional property
    """
    def __init__(self):
        super().__init__()
        self.experience = 0  # Represents the soldier experience

    def attack(self):
        """Soldiers attack success probability"""
        return 0.5 * (1 + self.health/100) * randrange(50 + self.experience, 100) / 100

    def damage(self):
        """The amount of damage a soldier can afflict"""
        return 0.05 + self.experience / 100


class Vehicle(Unit):
    """A battle vehicle
    """
    def __init__(self):
        super().__init__()
        self.operators = None  # The number of soldiers required to operate the vehicle
        self.recharge = range(1000, 2000)  # The recharge property for a vehicle must be greater than 1000 (ms)

    def attack(self):
        pass

    def damage(self):
        pass


class Squad:
    """Squads are consisted out of a number of units (soldiers or vehicles), that behave as a coherent group
    """
    pass
