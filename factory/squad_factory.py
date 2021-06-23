# -*- coding: utf-8 -*-
""" Module for squad factory

This module demonstrates squad builder.

"""
from models.squad import Squad

from factory.soldier_factory import SOLDIER_FACTORY
from factory.vehicle_factory import VEHICLE_FACTORY


def create_squad(data: dict) -> object:
    """ Create squad from json data

    Args:
        data(dict): data from json.

    Returns:
        object: new Squad.

    """
    if data['type_unit'] == 'vehicles':
        vehicle = VEHICLE_FACTORY
        return Squad(data['type_unit'], vehicle.create_vehicles(data['units']))

    if data['type_unit'] == 'soldiers':
        soldiers = SOLDIER_FACTORY
        return Squad(data['type_unit'], soldiers.create_soldiers(data['units']))


class SquadFactory:
    """ Squad builder

    """
    @staticmethod
    def get_instance() -> object:
        """ Get instance of SquadFactory

        Returns:
            object: The return value.

        """
        return SQUAD_FACTORY

    @staticmethod
    def create_squads(arr: list) -> list:
        """ Create squads implementation

        Args:
            arr(list): array with data from json.

        Returns:
            list: list of squads.

        """
        return [create_squad(i) for i in arr]


SQUAD_FACTORY = SquadFactory()
