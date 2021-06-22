class BaseStrategy:
    def __init__(self, type_unit):
        self.type_unit = type_unit

    def target(self, assault_army, arr_target):
        raise Exception("target() method is undefined")
