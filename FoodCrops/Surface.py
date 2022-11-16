from Unit import Unit
import pandas

class Surface(Unit):

    def __init__(self, id: int, name: str = "Surface"):
        super().__init__(id, name)

'''
    def describe(self):
        output = pandas.read_csv('FeedGrains.csv', usecols=['SC_Unit_ID', 'SC_Unit_Desc'])
        for raw in output:
            if output[0] == self.id:
                return output[1]
'''
