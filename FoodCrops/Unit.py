from abc import ABC
from enum import Enum
from Describable import Describable


class Unit(Describable, ABC):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    # Pas la peine de définir ici la méthode describe !
    def describe(self):
        return self.name
