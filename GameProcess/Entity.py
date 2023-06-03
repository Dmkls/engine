from MathLevel.Point import *
from MathLevel.CoordinateSystem import *
from MathLevel.BilinearForm import *
from MathLevel.VectorSpace import *

from Exceptions.exceptionsGame import *


class Entity:

    def __init__(self, cs):
        if isinstance(cs, CoordinateSystem):
            self.cs = cs
            self.identifier = None
            self.properties = {}
        else:
            WRONG_INPUT.MESSAGE("CoordinateSystem", type(cs))

    def set_property(self, prop, value):
        if isinstance(prop, str):
            self.properties[prop] = value
            self.__setattr__(prop, value)
        else:
            raise WRONG_INPUT.MESSAGE("str", type(prop))

    def get_property(self, prop):
        if isinstance(prop, str):
            return self.properties[prop]
        else:
            raise WRONG_INPUT.MESSAGE("str", type(prop))

    def remove_property(self, prop):
        if isinstance(prop, str):
            self.properties.pop(prop)
        else:
            raise WRONG_INPUT.MESSAGE("str", type(prop))

    def __getitem__(self, key):
        return self.get_property(key)

    def __setitem__(self, key, value):
        return self.set_property(key, value)