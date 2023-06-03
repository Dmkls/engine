from MathLevel.Point import *
from MathLevel.CoordinateSystem import *
from MathLevel.BilinearForm import *
from MathLevel.VectorSpace import *
from Entity import *

from Exceptions.exceptionsGame import *


class EntitiesList:

    def __init__(self, entities):
        if isinstance(entities, list):
            self.entities = entities
        else:
            raise WRONG_INPUT.MESSAGE("list[Entity]", type(self))

    def append(self, entity):
        if isinstance(entity, Entity):
            self.entities.append(entity)
        else:
            raise WRONG_INPUT.MESSAGE("Entity", type(self))

    def remove(self, entity):
        if isinstance(entity, Entity): #identifier
            self.entities.remove(entity)
        else:
            raise WRONG_INPUT.MESSAGE("Entity", type(self))

    def get(self, id):
        for i in self.entities:
            if i.identifier == id:
                return i

    def exec(self, func):
        if str(type(func)) == "<class 'function'>":
            for i in self.entities:
                func(i)
        else:
            raise WRONG_INPUT.MESSAGE("function(Entity)", type(self))

    def __getitem__(self, item):
        return self.get(item)