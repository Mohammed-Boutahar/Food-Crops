from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from Measurement import Measurement
from Commodity import Commodity
from Indicator import Indicator
from Surface import Surface
from Volume import Volume
from Weight import Weight
from Price import Price
from Count import Count
from Ratio import Ratio
from Unit import Unit

unitsRegistry = dict()
indicatorsRegistry = {}
commodityRegistry = {}
class FoodCropFactory(object):
    def __init__(self):
        super().__init__()
        self.unitsRegistry = {} , unitsRegistry
        self.indicatorsRegistry={} , indicatorsRegistry
        self.commodityRegistry={} , commodityRegistry



    @staticmethod
    def createVolume(id: int) -> Unit:
        if id not in unitsRegistry:
            unitsRegistry[id] = Volume(id)

        return unitsRegistry[id]

    @staticmethod
    def createPrice(id: int) -> Unit:
        if id not in unitsRegistry:
            unitsRegistry[id] = Price(id)

        return unitsRegistry[id]

    @staticmethod
    def createWeight(id: int, weight: float) -> Unit:
        if id not in unitsRegistry:
            unitsRegistry[id] = Weight(id, weight)

        return unitsRegistry[id]

    @staticmethod
    def createSurface(id: int) -> Unit:
        if id not in unitsRegistry:
            unitsRegistry[id] = Surface(id)

        return unitsRegistry[id]

    @staticmethod
    def createCount(id: int) -> Unit:
        if id not in unitsRegistry:
            unitsRegistry[id] = Count(id)

        return unitsRegistry[id]

    @staticmethod
    def createRatio(id: int, multiplier : float) -> Unit:
        if id not in unitsRegistry:
            unitsRegistry[id] = Ratio(id, multiplier)

        return unitsRegistry[id]

    @staticmethod
    def createCommodity(group: CommodityGroup, id: int, name: str) -> Commodity:
        if id not in commodityRegistry:
            commodityRegistry[id] = Commodity(group, id, name)

        return commodityRegistry[id]

    @staticmethod
    def createIndicator(id: int, frequency: int, freqDesc: str, geogLocation: str,
                        indicatorGroup: IndicatorGroup, unit: Unit) -> Indicator:
        if id not in indicatorsRegistry:
            indicatorsRegistry[id] = Indicator(id,frequency,freqDesc,geogLocation,indicatorGroup,unit)

        return indicatorsRegistry[id]

    @staticmethod
    def createMeasurement(id: int, year: int, value: float, timeperiodId: int, timeperiodDesc: str,
                          comodity: Commodity, indicator: Indicator) -> Measurement:
        return Measurement(id, year, value, timeperiodId, timeperiodDesc, comodity, indicator).describe()
