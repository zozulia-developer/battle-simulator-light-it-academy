class BaseStrategy:
    def __init__(self, type_of):
        self.type_of = type_of

    def target(self):
        raise Exception("target() method is undefined")