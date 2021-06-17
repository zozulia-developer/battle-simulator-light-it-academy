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
        return SoldierFactory()

    def create_soldier(self, data):
        return Soldier(data['health'], data['recharge'])

    def create_soldiers(self, arr):
        return [self.create_soldier(i) for i in arr]
