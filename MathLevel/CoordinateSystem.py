from Point import *
from VectorSpace import *


class CoordinateSystem:

    def __init__(self, initial_point, space):
        if isinstance(initial_point, Point) and isinstance(space, VectorSpace):
            self.initial_point = initial_point
            self.space = space
        else:
            raise TypeError