from factory.VehicleFactory import VehicleFactory
from models.squad import Squad
from factory.SoldierFactory import SoldierFactory


class SquadFactory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return SquadFactory()

    def create_squad(self, data):
        if data['type_unit'] == 'vehicles':
            vehicle = VehicleFactory.get_instance()
            return Squad(data['type_unit'], vehicle.create_vehicles(data['units']))
        elif data['type_unit'] == 'soldiers':
            soldiers = SoldierFactory.get_instance()
            return Squad(data['type_unit'], soldiers.create_soldiers(data['units']))

    def create_squads(self, arr):
        return [self.create_squad(i) for i in arr]
