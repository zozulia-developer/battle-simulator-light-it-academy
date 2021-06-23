# -*- coding: utf-8 -*-
""" Base strategy

"""


class BaseStrategy:
    """ Base strategy

    """
    def __init__(self, type_unit: str):
        self.type_unit = type_unit

    def target(self, assault_army: dict, arr_target: dict) -> None:
        """ Raise an error if target function is not implemented

        Args:
            assault_army (dict): dict.
            arr_target (dict): dict.

        """
        raise NotImplementedError("target() method is undefined")
