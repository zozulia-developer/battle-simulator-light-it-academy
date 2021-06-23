# -*- coding: utf-8 -*-
""" Module for random strategy

This module demonstrates implementation of random strategy.

"""
from random import randint
from models.base_strategy import BaseStrategy


class RandomStrategy(BaseStrategy):
    """Represents random strategy

    """

    def target(self, assault_army, arr_target) -> dict:
        """ Select target army and target squad

        Returns:
             dict: The return value. Target army, target squad.

        """
        target_armies = [army for army in arr_target if assault_army.name != army.name]
        target_army = target_armies[randint(0, len(target_armies) - 1)]
        target_squad = target_army.squads[randint(0, len(target_army.squads) - 1)]

        return {'target_army': target_army, 'target_squad': target_squad}
