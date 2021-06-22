from functools import reduce


class Squad:
    """ Squads are consisted out of a number of units (soldiers or vehicles), that behave as a coherent group

    Args:
        type_unit (str): type of unit: vehicles or soldiers.
        units (list): list of units.

    """

    def __init__(self, type_unit: str, units: list):
        self.type_unit = type_unit
        self.units = units

    def success_attack(self) -> float:
        """ Calculation of success attack

        Returns:
            float: The return value.

        """
        return reduce(lambda a, b: a * b.success_attack(), self.units, 1) ** (1 / len(self.units))

    def get_damage(self, dmg: float) -> None:
        """ Calculate how many damage get the squad

        Args:
            dmg (float): value of damage that squad receive.

        """
        dmg = dmg / len(self.units)
        for i in self.units:
            i.get_damage(dmg)

    def start_recharge(self) -> None:
        """ Start recharging for every unit

        """
        units = [el for el in self.units if el.is_ready]
        for el in units:
            el.start_recharge()

    def time_recharge(self) -> None:
        """ Time of recharge for every unit

        """
        units = [el for el in self.units if not el.is_ready]
        for el in units:
            el.time_recharge()

    def make_damage(self) -> float:
        """ Calculation of making damage

        Returns:
            float: The return value.

        """
        return reduce(lambda a, b: a + b.make_damage(), self.units, 0)

    def is_alive(self) -> bool:
        """ Check if squad is alive

        Returns:
             bool: The return value. True for success, False otherwise.

        """
        return any(el.is_alive() for el in self.units)

    def filter_alive_units(self) -> None:
        """ Filter for alive units

        """
        self.units = [unit for unit in self.units if unit.is_alive()]

    def get_power(self) -> float:
        """ Calculate power of squad

        Returns:
             float: The return value.

        """
        return reduce(lambda a, b: a + b.get_power(), self.units, 0)

    def inc_exp_for_units(self) -> None:
        """ Incrementing experience for units

        """
        for unit in self.units:
            unit.set_experience()
