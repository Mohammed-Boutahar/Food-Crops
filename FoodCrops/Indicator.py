import pandas
from Describable import Describable
from IndicatorGroup import IndicatorGroup
from Unit import Unit


class Indicator(Describable):
	def __init__(self, id:str, frequency:int, frequencyDesc:str, geoLocation:str, indicatorGroup:IndicatorGroup, unit:Unit):
		self.id = id
		self.unit = unit
		self.indicatorGroup = indicatorGroup
		self.frequency = frequency
		self.frequencyDesc = frequencyDesc
		self.geoLocation = geoLocation


	def describe(self):
		return self.id, self.frequencyDesc, self.geoLocation, self.unit.describe()

'''
class Indicator(Describable):
    def __init__(self, id: int, frequency: int, frequencyDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                 unit: Unit):
        self.id = id
        self.frequency = frequency
        self.frequencyDesc = frequencyDesc
        self.geoLocation = geogLocation
        self.indicatorGroup = indicatorGroup
        self.unit = unit


    def describe(self):
        sortie = pandas.read_csv('./csv/FeedGrains.csv', usecols=['SC_Attribute_ID', 'SC_Attribute_Desc', 'SC_GeographyIndented_Desc',
                                                                  'SC_Group_Desc'])
        for raw in sortie:
            if raw[0] == self.id:
                return "Description de l'indicateur " + self.id + " :\n" + "\t Nom de l'indicateur : " + raw[
                    1] + "\n\t frequence de meusure : " + self.frequencyDesc + "\n\t Zone geographique : " + raw[
                           2] + "\n\t Groupe de l'indicateur : " + sortie[
                           3] + "\n\t Unite de mesure de l'indicateur : " + self.unit.describe()
'''