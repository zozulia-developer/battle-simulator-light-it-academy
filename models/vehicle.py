from random import randint
from functools import reduce
from .unit import Unit


class Vehicle(Unit):
    """A battle vehicle

    """

    def __init__(self, health, recharge, operators):
        super().__init__(health, recharge)
        self.total_health = 100
        self.operators = operators  # The number of soldiers required to operate the vehicle

    def success_attack(self):
        gavg = reduce(lambda a, b: a * b.success_attack(), self.operators, 1) ** (1 / len(self.operators))
        return 0.5 * (1 + self.health / 100) * gavg

    def make_damage(self):
        return 0.1 + (reduce(lambda a, b: a + b.get_experience(), self.operators, 0) / 100)

    def set_total_health(self):
        self.total_health = ((reduce(lambda a, c: a + c.health, self.operators, 0) / len(
            self.operators)) + self.health) / 2

    def get_damage(self, dmg):
        self.set_total_health()
        self.health = self.health - dmg * 0.6
        if len(self.operators) == 1:
            self.operators[0].health -= dmg * 0.2
            return self.operators[0].health
        random_operator = randint(0, len(self.operators) - 1)
        for operator in self.operators:
            operator.get_damage(dmg * 0.1)
        self.operators[random_operator].health -= dmg * 0.1

    def set_experience(self):
        for i in self.operators:
            i.set_experience()

    def is_alive(self):
        return True if self.total_health > 0 and self.health > 0 else False

    def get_power(self):
        return reduce(lambda a, b: a + b.get_power(), self.operators, 0)
