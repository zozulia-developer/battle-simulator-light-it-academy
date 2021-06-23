# -*- coding: utf-8 -*-
""" Module for weakest strategy

This module demonstrates implementation of weakest strategy.

"""
from models.base_strategy import BaseStrategy


class WeakestStrategy(BaseStrategy):
    """Represents weakest strategy

    """

    def target(self, assault_army, arr_target) -> dict:
        """ Select target army and target squad

        Returns:
             dict: The return value. Target army, target squad.

        """
        target_armies = [army for army in arr_target if assault_army.name != army.name]
        target_army = sorted(target_armies, key=lambda army: army.get_power())[0]
        target_squad = sorted(target_army.squads, key=lambda squad: squad.get_power())[0]

        return {'target_army': target_army, 'target_squad': target_squad}
