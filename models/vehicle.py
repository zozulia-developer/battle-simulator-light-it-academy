from random import randrange
from unit import Unit


class Vehicle(Unit):
    """A battle vehicle

    """

    def __init__(self, health, recharge, operators):
        super().__init__(health, recharge)
        self.total_health = 100
        self.operators = operators  # The number of soldiers required to operate the vehicle

    def success_attack(self):
        gavg = self.operators.reduce(lambda a, b: a * b.success_attack(), 1) ** (1 / len(self.operators))
        return 0.5 * (1 + self.health / 100) * gavg

    def make_damage(self):
        return 0.1 + (self.operators.reduce(lambda a, b: a + b.get_experience(), 0) / 100)

    def set_total_health(self):
        self.total_health = ((self.operators.reduce(lambda a, c: a + c.health, 0) / len(self.operators)) + self.health) / 2

    def get_damage(self, dmg):
        self.set_total_health()
        self.health = self.health - dmg * 0.6
        if len(self.operators == 1):
            self.operators[0].health -= dmg * 0.2
            return self.operators[0].health
        random_operator = randrange(0, len(self.operators) - 1)
        for operator in self.operators:
            operator.get_damage(dmg * 0.1)
        self.operators[random_operator].health -= dmg * 0.1

    def set_experience(self):
        for i in self.operators:
            i.set_experience(1)

    def is_alive(self):
        return True if self.total_health > 0 and self.health > 0 else False

    def get_power(self):
        return self.operators.reduce(lambda a, b: a + b.get_power(), 0)
