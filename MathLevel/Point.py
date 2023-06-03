from Vector import *
from Exceptions.exceptionsMath import *


class Point(Vector):

    def __mul__(self, other):
        raise "POINT_UNKNOWN_OPERATION"

    def __truediv__(self, other):
        raise "POINT_UNKNOWN_OPERATION"

    def __invert__(self):
        raise "POINT_UNKNOWN_OPERATION"