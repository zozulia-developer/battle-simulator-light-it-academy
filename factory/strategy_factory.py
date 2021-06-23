# -*- coding: utf-8 -*-
""" Module for strategy factory

This module demonstrates strategy builder.

"""
from strategy.random_strategy import RandomStrategy
from strategy.strongest_strategy import StrongestStrategy
from strategy.weakest_strategy import WeakestStrategy


class StrategyFactory:
    """ Strategy builder

    """
    @staticmethod
    def get_instance() -> object:
        """ Get instance of StrategyFactory

        Returns:
            object: The return value.

        """
        return STRATEGY_FACTORY

    def create_strategy(self, data: dict) -> object:
        """ Create strategy from json data

        Args:
            data(dict): data from json.

        Returns:
            object: new Strategy.

        """
        if data == 'random':
            return RandomStrategy(data)

        if data == 'strongest':
            return StrongestStrategy(data)

        if data == 'weakest':
            return WeakestStrategy(data)


STRATEGY_FACTORY = StrategyFactory()
