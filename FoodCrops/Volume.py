import pandas
# from StringIO import StringIO

from Unit import Unit


class Volume(Unit):

    def __init__(self, id: int, name: str = "Volume"):
        super().__init__(id, name)


