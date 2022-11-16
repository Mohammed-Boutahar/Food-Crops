from Unit import Unit
import pandas


class Count(Unit):

    def __init__(self, id: int, what: str, name: str = "Count"):
        super().__init__(id, name)
        self.what = what

    def describe(self):
        output = pandas.read_csv('./csv/FeedGrains.csv', usecols=['SC_Unit_ID', 'SC_Unit_Desc'])
        for raw in output:
            if raw[0] == self.id:
                return raw[1]
