import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from models.vehicle import Vehicle
from factory.SoldierFactory import SoldierFactory


instance = None


class VehicleFactory:
    def __init__(self):
        if instance:
            pass
        else:
            self.instance = instance

    @staticmethod
    def get_instance():
        return VehicleFactory()

    def create_vehicle(self, data):
        soldier = SoldierFactory.get_instance()
        return Vehicle(data['health'], data['recharge'], soldier.create_soldiers(data['operators']))

    def create_vehicles(self, arr):
        return [self.create_vehicle(i) for i in arr]
