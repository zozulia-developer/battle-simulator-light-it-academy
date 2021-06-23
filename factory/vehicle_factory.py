# -*- coding: utf-8 -*-
""" Module for vehicle factory

This module demonstrates vehicle builder.

"""
from models.vehicle import Vehicle
from factory.soldier_factory import SOLDIER_FACTORY


def create_vehicle(data: dict) -> object:
    """ Create vehicle from json data

    Args:
        data(dict): data from json.

    Returns:
        object: new Vehicle.

    """
    soldier = SOLDIER_FACTORY
    return Vehicle(data['health'], data['recharge'], soldier.create_soldiers(data['operators']))


class VehicleFactory:
    """ Vehicle builder

    """
    @staticmethod
    def get_instance() -> object:
        """ Get instance of VehicleFactory

        Returns:
            object: The return value.

        """
        return VEHICLE_FACTORY

    @staticmethod
    def create_vehicles(arr: list) -> object:
        """ Create vehicles implementation

        Args:
            arr(list): array with data from json.

        Returns:
            list: list of vehicles.

        """
        return [create_vehicle(i) for i in arr]


VEHICLE_FACTORY = VehicleFactory()
