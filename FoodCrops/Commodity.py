import pandas
from Describable import Describable
from CommodityGroup import CommodityGroup

class Commodity(Describable):
    def __init__(self, id: int, group: CommodityGroup, name: str):
        self.id = id
        self.group = group
        self.name = name


    def describe(self):
        return self.name, self.group
        # sortie = pandas.read_csv('./csv/FeedGrains.csv', usecols= ['SC_Commodity_ID','SC_Commodity_Desc','SC_GroupCommod_Desc'])
        # for raw in sortie:
        #     if raw[0] == self.id:
        #         return raw[1]+" "+raw[2]
