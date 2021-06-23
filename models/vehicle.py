# -*- coding: utf-8 -*-
""" Module for vehicle model

This module demonstrates model of vehicle.

"""
from random import randint
from functools import reduce
from .unit import Unit


class Vehicle(Unit):
    """ A battle vehicle

    Args:
        health (int): vehicle health.
        recharge (int): vehicle recharge.
        operators (list): number of operators 1-3.

    """

    def __init__(self, health: int, recharge: int, operators: list):
        super().__init__(health, recharge)
        self.total_health = 100
        self.operators = operators

    def success_attack(self) -> float:
        """ Calculation of success attack

        Returns:
            float: The return value.

        """
        gavg = reduce(lambda a, b: a * b.success_attack(), self.operators, 1) ** (1 / len(self.operators))
        return 0.5 * (1 + self.health / 100) * gavg

    def make_damage(self) -> float:
        """ Calculation of making damage

        Returns:
            float: The return value.

        """
        return 0.1 + (reduce(lambda a, b: a + b.get_experience(), self.operators, 0) / 100)

    def set_total_health(self) -> None:
        """ Set total health of vehicle, operators, units

        """
        self.total_health = ((reduce(lambda a, c: a + c.health, self.operators, 0) / len(
            self.operators)) + self.health) / 2

    def get_damage(self, dmg: float) -> None:
        """ Calculate how many damage get the vehicle

        Args:
            dmg (float): value of damage that vehicle receive.

        """
        self.set_total_health()
        self.health = self.health - dmg * 0.6
        if len(self.operators) == 1:
            self.operators[0].health -= dmg * 0.2
            return self.operators[0].health
        random_operator = randint(0, len(self.operators) - 1)
        for operator in self.operators:
            operator.get_damage(dmg * 0.1)
        self.operators[random_operator].health -= dmg * 0.1

    def set_experience(self) -> None:
        """ Set experience for operators

        """
        for i in self.operators:
            i.set_experience()

    def is_alive(self) -> bool:
        """ Check if vehicle is alive

        Returns:
             bool: The return value. True for success, False otherwise.

        """
        return True if self.total_health > 0 and self.health > 0 else False

    def get_power(self) -> float:
        """ Calculate power of vehicle

        Returns:
             float: The return value.

        """
        return reduce(lambda a, b: a + b.get_power(), self.operators, 0)
