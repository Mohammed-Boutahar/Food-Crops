from Unit import Unit
import pandas

class Weight(Unit):

    def __init__(self, id: int, multiplier: float, name: str = "Weight"):
        super().__init__(id, name)
        self.multiplier = multiplier


