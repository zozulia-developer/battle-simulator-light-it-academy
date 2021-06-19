from time import monotonic
from random import Random


class Unit:
    """Each unit represents either a soldier or a vehicle maned by a predetermined number of soldiers

    """
    _random = Random(228)

    def __init__(self, health, recharge):
        self.health = health  # Represents the health of the unit
        self.recharge = recharge  # Represents the number of ms required to recharge the unit for an attack
        self.attack_ready = True
        self.recharge_time = 0

    def is_alive(self):
        """ Check if Unit is alive """
        return self.health > 0

    def start_recharge(self):
        """ Start recharging """
        self.attack_ready = False if self.attack_ready else True
        self.recharge_time = monotonic()

    def get_health(self):
        """ Get health of the unit """
        return self.health

    def set_health(self, val):
        """ Set health of the unit """
        if val <= 0:
            self.health = 0
        elif val >= 100:
            self.health = 100
        else:
            self.health = val

    def time_recharge(self):
        """ Recharging time """
        time = monotonic()
        if time - self.recharge_time > self.recharge:
            self.start_recharge()

    def is_ready(self, time):
        return time - self.recharge_time >= self.recharge
