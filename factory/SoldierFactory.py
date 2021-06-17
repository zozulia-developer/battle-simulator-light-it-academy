import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from models.soldier import Soldier

instance = None


class SoldierFactory:
    def __init__(self):
        if instance:
            pass
        else:
            self.instance = instance

    @staticmethod
    def get_instance():
        return SoldierFactory

    def create_soldier(self, data):
        return Soldier(data.health, data.recharge)

    def create_soldiers(self, arr):
        return arr.map(lambda i: self.create_soldier(i))
