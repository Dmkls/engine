from MathLevel.Point import *
from MathLevel.CoordinateSystem import *
from MathLevel.BilinearForm import *
from MathLevel.VectorSpace import *

from Exceptions.exceptionsGame import *


class Ray:

    def __init__(self, cs, initialpt, direction):
        if isinstance(cs, CoordinateSystem):
            if isinstance(initialpt, Point):
                if isinstance(direction, Vector):
                    self.cs = cs
                    self.initialpt = initialpt
                    self.direction = direction
                else:
                    raise WRONG_INPUT.MESSAGE("Vector", type(direction))
            else:
                raise WRONG_INPUT.MESSAGE("Point", type(initialpt))
        else:
            raise WRONG_INPUT.MESSAGE("CoordinateSystem", type(cs))