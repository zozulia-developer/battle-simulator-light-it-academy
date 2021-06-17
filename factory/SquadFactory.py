import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from VehicleFactory import VehicleFactory
from models.squad import Squad
from SoldierFactory import SoldierFactory

instance = None


class SquadFactory:
    def __init__(self):
        if instance:
            pass
        else:
            self.instance = instance

    @staticmethod
    def get_instance():
        return SquadFactory

    def create_squad(self, data):
        if data.type_of == 'vehicles':
            vehicle = VehicleFactory.get_instance()
            return Squad(data.type_of, vehicle.create_vehicles(data.units))
        elif data.type_of == 'soldiers':
            soldiers = SoldierFactory.get_instance()
            return Squad(data.type_of, soldiers.create_soldiers(data.units))

    def create_squads(self, arr):
        return arr.map(lambda i: self.create_squad(i))
