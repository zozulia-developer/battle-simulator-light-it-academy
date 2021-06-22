from models.BaseStrategy import BaseStrategy


class WeakestStrategy(BaseStrategy):
    """Represents weakest strategy

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
        target_army = sorted(target_armies, key=lambda army: army.get_power())[0]
        target_squad = sorted(target_army.squads, key=lambda squad: squad.get_power())[0]

        return {'target_army': target_army, 'target_squad': target_squad}
