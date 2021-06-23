# -*- coding: utf-8 -*-
""" Module for army model

This module demonstrates model of army.

"""
from functools import reduce


class Army:
    """Represents either a soldier or a vehicle

    Args:
        squads (list): list of squads.
        strategy (str): strategy name.
        name (str): army name.

    """

    def __init__(self, squads: list, strategy: str, name: str):
        self.squads = squads
        self.strategy = strategy
        self.name = name

    def is_alive(self) -> bool:
        """ Check if Army is alive

        Returns:
             bool: The return value. True for success, False otherwise.

        """
        return any(squad.is_alive() for squad in self.squads)

    def filter_alive_squads(self) -> None:
        """ Filter for alive squads

        """
        self.squads = [squad for squad in self.squads if squad.is_alive()]

    def get_power(self) -> float:
        """ Calculate army power

        Returns:
             float: The return value.

        """
        return reduce(lambda a, b: a + b.get_power(), self.squads, 0)
