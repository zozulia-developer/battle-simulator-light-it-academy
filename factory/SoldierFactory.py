from models.soldier import Soldier


class SoldierFactory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return SoldierFactory()

    def create_soldier(self, data):
        return Soldier(data['health'], data['recharge'])

    def create_soldiers(self, arr):
        return [self.create_soldier(i) for i in arr]
