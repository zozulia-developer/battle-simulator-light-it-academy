from random import randrange


class Unit:
    """Each unit represents either a soldier or a vehicle maned by a predetermined number of soldiers

    """

    def __init__(self, health, recharge):
        self.health = health  # Represents the health of the unit
        self.recharge = recharge  # Represents the number of ms required to recharge the unit for an attack

    def is_alive(self):
        """ Check if Unit is alive """
        if self.health > 0:
            return True
        else:
            return False


class Soldier(Unit):
    """Soldiers are units that have an additional property

    """

    def __init__(self):
        self.experience = 0  # Represents the soldier experience
        Unit.__init__(self, 100, randrange(100, 2000))

    def success_attack(self):
        """ Soldiers attack success probability """
        return 0.5 * (1 + self.health/100) * randrange(50 + self.experience, 100) / 100

    def damage_amount(self):
        """ The amount of damage a soldier can afflict """
        return 0.05 + self.experience / 100

    def do_attack(self, enemy):
        pass

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0


class Vehicle(Unit):
    """A battle vehicle

    """

    def __init__(self):
        self.operators = randrange(1, 3)  # The number of soldiers required to operate the vehicle
        Unit.__init__(self, 100, randrange(1000, 2000))

    def success_attack(self):
        pass

    def damage_amount(self):
        pass


class Squad:
    """Squads are consisted out of a number of units (soldiers or vehicles), that behave as a coherent group

    """

    pass


class Army:
    pass
