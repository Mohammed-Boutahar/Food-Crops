from abc import ABC, abstractmethod
from enum import Enum


class Describable(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def describe(self) -> str:
        pass
