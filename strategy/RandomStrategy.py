from models.BaseStrategy import BaseStrategy
from random import randint


class RandomStrategy(BaseStrategy):
    """Represents random strategy

    Args:
        type_unit (str): unit type.

    """
    def __init__(self, type_unit: str):
        super().__init__(type_unit)

    def target(self, assault_army, arr_target) -> dict:
        """ Select target army and target squad

        Returns:
             dict: The return value. Target army, target squad.

        """
        target_armies = [army for army in arr_target if assault_army.name != army.name]
        target_army = target_armies[randint(0, len(target_armies) - 1)]
        target_squad = target_army.squads[randint(0, len(target_army.squads) - 1)]

        return {'target_army': target_army, 'target_squad': target_squad}
