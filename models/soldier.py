from random import randint
from .unit import Unit


class Soldier(Unit):
    """Soldiers are units that have an additional property

    Args:
        health (int): soldier health.
        recharge (int): soldier recharge.

    """

    def __init__(self, health: int, recharge: int):
        super().__init__(health, recharge)
        self.experience = 0

    def get_experience(self) -> int:
        """ Get experience for soldier

        Returns:
             int: The return value.

        """
        return self.experience

    def set_experience(self) -> None:
        """ Set experience for soldier

        """
        if self.experience > 50:
            self.experience = 50
        else:
            self.experience += 1

    def success_attack(self) -> float:
        """ Calculation of success attack

        Returns:
            float: The return value.

        """
        return 0.5 * (1 + self.health/100) * randint(50 + self.experience, 101) / 100

    def make_damage(self) -> float:
        """ Calculation of making damage

        Returns:
            float: The return value.

        """
        return 0.05 + self.experience / 100

    def get_power(self) -> float:
        """ Calculate power of soldier

        Returns:
             float: The return value.

        """
        return self.health + self.experience + self.make_damage()

    def get_damage(self, damage: float) -> None:
        """ Calculate how many damage get the vehicle

        Args:
            damage (float): value of damage that soldier receive.

        """
        self.health -= damage
        if self.health < 0:
            self.health = 0
