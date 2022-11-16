from abc import ABC
from enum import Enum
import pandas
from Unit import Unit


class Price(Unit):

    def __init__(self, id: int, name: str = "Price"):
        super().__init__(id, name)

    '''
    def describe(self):
        output = pandas.read_csv('./csv/FeedGrains.csv', usecols=['SC_Unit_ID', 'SC_Unit_Desc'])
        for raw in output:
            if raw[0] == self.id:
                return raw[1]
    '''
