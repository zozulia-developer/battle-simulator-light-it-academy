from random import randrange
from .unit import Unit


class Soldier(Unit):
    """Soldiers are units that have an additional property

    """

    def __init__(self, health, recharge):
        super().__init__(health, recharge)
        self.experience = 0  # Represents the soldier experience

    def get_experience(self):
        return self.experience

    def set_experience(self):
        if self.experience > 50:
            self.experience = 50
        else:
            self.experience += 1

    def success_attack(self):
        """ Soldiers attack success probability """
        return 0.5 * (1 + self.health/100) * randrange(50 + self.experience, 100) / 100

    def make_damage(self):
        """ The amount of damage a soldier can afflict """
        return 0.05 + self.experience / 100

    def get_power(self):
        return self.health + self.experience + self.make_damage()

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
