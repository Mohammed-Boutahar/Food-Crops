from Describable import Describable
from Commodity import Commodity
from Indicator import Indicator


class Measurement(Describable):
    id=1
    def __init__(self, id: int, year: int, value: float, timeperiodId: int, timeperiodDescr: str, commodity: Commodity,
                 indicator: Indicator):
        # static generated id
        Measurement.id += 1
        self.id = Measurement.id
        self.year = year
        self.value = value
        self.timeperiodId = timeperiodId
        self.timeperiodDescr = timeperiodDescr
        self.commodity = commodity
        self.indicator = indicator

    def describe(self) -> str:
        return self.id , self.year , self.timeperiodId , self.timeperiodDescr , self.value , self.commodity , self.indicator


'''
    def describe(self):
        sortie = pandas.read_csv('./csv/FeedGrains.csv', usecols=['Year_ID', 'Amount', 'Timeperiod_ID', 'Timeperiod_Desc'])
        for raw in sortie:
            if raw[0] == self.year and raw[2] == self.timeperiodId:
                return raw[1] + " " + raw[3] + " " + self.commodity.describe() + " " + self.indicator.describe()
'''
