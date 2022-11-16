from Unit import Unit
import pandas


class Ratio(Unit):

    def __init__(self, id: int, multiplier: float, name: str = "Weight"):
        super().__init__(id, name)
        self.multiplier = multiplier
'''
    def describe(self):
        output = pandas.read_csv('./csv/FeedGrains.csv', usecols=['SC_Unit_ID', 'SC_Unit_Desc'])
        for raw in output:
            if raw[0] == self.id:
                return raw[1]
'''
