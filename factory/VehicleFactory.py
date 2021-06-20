import os
import sys
from models.vehicle import Vehicle
from factory.SoldierFactory import SoldierFactory

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class VehicleFactory(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return VehicleFactory()

    def create_vehicle(self, data):
        soldier = SoldierFactory.get_instance()
        return Vehicle(data['health'], data['recharge'], soldier.create_soldiers(data['operators']))

    def create_vehicles(self, arr):
        return [self.create_vehicle(i) for i in arr]
