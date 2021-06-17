from factory.VehicleFactory import VehicleFactory
from models.squad import Squad
from factory.SoldierFactory import SoldierFactory

instance = None


class SquadFactory:
    def __init__(self):
        if instance:
            pass
        else:
            self.instance = instance

    @staticmethod
    def get_instance():
        return SquadFactory()

    def create_squad(self, data):
        if data['type_of'] == 'vehicles':
            vehicle = VehicleFactory.get_instance()
            return Squad(data['type_of'], vehicle.create_vehicles(data['units']))
        elif data['type_of'] == 'soldiers':
            soldiers = SoldierFactory.get_instance()
            return Squad(data['type_of'], soldiers.create_soldiers(data['units']))

    def create_squads(self, arr):
        return [self.create_squad(i) for i in arr]
