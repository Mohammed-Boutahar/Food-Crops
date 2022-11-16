import math
from IndicatorGroup import IndicatorGroup
from CommodityGroup import CommodityGroup
from Unit import Unit
import pandas as pd
from FoodCropFactory import FoodCropFactory


class FoodCropsDataset(object):
    def __init__(self):
        self.indicators = {}
        self.units = {}
        self.commodities = {}
        self.measurements = {}


    def load(self, datasetPath: str):

        print("Chargement du jeu")
        dataframe = pd.read_csv(datasetPath)
        i = 1
        for index, row in dataframe.iterrows():
            # pour sauter les lignes vides du csv
            if math.isnan(row[2]):
                continue
            # create unit
            # for unit we have :
            # 4,5,12,14,31-> price
            # 2,10,44 -> surface
            # 1,3,17,18 -> volume
            # 6,11,13,45, -> ratio
            # 7,8,9,41 -> weight
            # 15,16,46 -> count

            if row[11] in self.units:
                unit = self.units[row[11]]
            else:
                if row[11] in (4, 5, 12, 14, 31):
                    unit = FoodCropFactory.createPrice(row[11])
                elif row[11] in (2, 10, 44):
                    unit = FoodCropFactory.createSurface(row[11])
                elif row[11] in (1, 3, 17, 18):
                    unit = FoodCropFactory.createVolume(row[11])
                elif row[11] in (6, 11, 13, 45):
                    unit = FoodCropFactory.createRatio(row[11], row[12])
                elif row[11] in (7, 8, 9, 41):
                    unit = FoodCropFactory.createWeight(1000, row[11])
                else:
                    unit = FoodCropFactory.createCount("count", row[11])

                self.units[row[11]] = unit

            # create indicator
            # check for existence before create
            if row[9] in self.indicators:
                indicator = self.indicators[row[9]]
            else:
                self.indicators[row[9]] = FoodCropFactory.createIndicator(row[9], row[14], row[15], row[6].strip(), IndicatorGroup(row[0]), unit)
                indicator = self.indicators[row[9]]


            # create commodity
            # check for existence before
            if row[7] in self.commodities:
                commodity = self.commodities[row[7]]
            else:
                self.commodities[row[7]] = FoodCropFactory.createCommodity(CommodityGroup(row[2]), row[7], row[8])
                commodity = self.commodities[row[7]]

            self.measurements[index] = FoodCropFactory.createMeasurement(index, row[13], row[18], row[16], row[17],
                                                                    commodity.describe(), indicator.describe())

            print(i,"/463119 ")
            i+=1

        print(self.measurements)

        print("fin")

    def findMeasurements(self, indicator : IndicatorGroup, geoLocation : str, unit : Unit, commodity : CommodityGroup):
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        lt = []  ## On remplira cette liste par toutes les mesures

        for cle, valeur in self.commodities.items():
            for mesure in valeur:
                lt.append(mesure)

        if (commodity == None):
            l1 = lt
        else:
            for cle, valeur in self.commodities.items():
                if (cle == commodity):
                    for mesure in valeur:
                        l1.append(mesure)

        if (indicator == None):
            l2 = lt
        else:
            for cle, valeur in self.indicators.items():
                if (cle == indicator):
                    for mesure in valeur:
                        l2.append(mesure)

        if (geoLocation == None):
            l3 = lt
        else:
            for cle, valeur in self.measurements.items():
                if (cle == geoLocation):
                    for mesure in valeur:
                        l3.append(mesure)

        if (unit == None):
            l4 = lt
        else:
            for cle, valeur in self.units.items():
                if (cle == unit):
                    for mesure in valeur:
                        l4.append(mesure)

        s1 = set(l1)
        s2 = set(l2)
        s3 = set(l3)
        s4 = set(l4)

        s = s1 & s2 & s3 & s4
        l = list(s)

        return l

