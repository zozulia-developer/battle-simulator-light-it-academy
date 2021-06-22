from time import monotonic


class Unit:
    """Represents either a soldier or a vehicle

    Args:
        health (int): unit health.
        recharge (int): unit recharge.

    """

    def __init__(self, health: int, recharge: int):
        self.health = health
        self.recharge = recharge
        self.attack_ready = True
        self.recharge_time = 0

    def is_alive(self) -> bool:
        """ Check if Unit is alive

        Returns:
             bool: The return value. True for success, False otherwise.

        """
        return self.health > 0

    def start_recharge(self) -> None:
        """ Start recharging

        """
        self.attack_ready = False if self.attack_ready else True
        self.recharge_time = monotonic()

    def get_health(self) -> int:
        """ Get health of the unit

        Returns:
             int: The return value.

        """
        return self.health

    def set_health(self, val: int) -> None:
        """ Set health of the unit

        Args:
            val (int): value of the health that need to set.

        """
        if val <= 0:
            self.health = 0
        elif val >= 100:
            self.health = 100
        else:
            self.health = val

    def time_recharge(self) -> None:
        """ Recharging time

        """
        time = monotonic()
        if time - self.recharge_time > self.recharge:
            self.start_recharge()

    def is_ready(self, time: int) -> int:
        """ Check if unit is ready

        Args:
            time (int): time.

        """
        return time - self.recharge_time >= self.recharge
