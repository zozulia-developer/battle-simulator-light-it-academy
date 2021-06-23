# -*- coding: utf-8 -*-
""" Module for soldier factory

This module demonstrates soldier builder.

"""
from models.soldier import Soldier


def create_soldier(data: dict) -> object:
    """ Create soldier from json data

    Args:
        data(dict): data from json.

    Returns:
        object: new Soldier.

    """
    return Soldier(data['health'], data['recharge'])


class SoldierFactory:
    """ Soldier builder

    """
    @staticmethod
    def get_instance() -> object:
        """ Get instance of SoldierFactory

        Returns:
            object: The return value.

        """
        return SOLDIER_FACTORY

    @staticmethod
    def create_soldiers(arr: list) -> list:
        """ Create soldiers implementation

        Args:
            arr(list): array with data from json.

        Returns:
            list: list of soldiers.

        """
        return [create_soldier(i) for i in arr]


SOLDIER_FACTORY = SoldierFactory()
