# -*- coding: utf-8 -*-
""" Module for army factory

This module demonstrates army builder.

"""
from models.army import Army

from factory.squad_factory import SquadFactory
from factory.strategy_factory import StrategyFactory


def create_army(data: dict) -> object:
    """ Create army from squads and set strategy

    Args:
        data(dict): data from json.

    Returns:
        object: new Army.

    """
    squads = SquadFactory.get_instance()
    squads = squads.create_squads(data['squads'])

    strategy = StrategyFactory.get_instance()
    strategy = strategy.create_strategy(data['strategy'])

    return Army(squads, strategy, data['name'])


class ArmyFactory:
    """ Army builder

    """

    @staticmethod
    def get_instance() -> object:
        """ Get instance of ArmyFactory

        Returns:
            object: The return value.

        """
        return ARMY_FACTORY

    @staticmethod
    def create_armies(arr: list) -> list:
        """ Create armies implementation

        Args:
            arr(list): array with data from json.

        Returns:
            list: list of armies.

        """
        return [create_army(i) for i in arr]


ARMY_FACTORY = ArmyFactory()
