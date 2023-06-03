from Matrix import *
from Exceptions.exceptionsMath import *

class Vector(Matrix):

    def dim(self):
        return max(self.n, self.m)

    def to(self):  # возвращект коорднаты вектора в виде одномерного массива
        if self.n == 1 and self.m == 1:
            if isinstance(self.elements[0], list):
                return [self.elements[0][0]]
        if self.n != 1:
            buffVector = self.transpose()
            return buffVector.elements
        else:
            elements = []
            for i in range(self.m):
                elements.append(self.elements[i])
            return elements

    def scalar_product(self, v1):
        if isinstance(self, Vector) and (v1, Vector):
            if self.dim() == v1.dim():
                sum = 0
                elements1 = self.to()
                elements2 = v1.to()
                for i in range(self.dim()):
                    sum += elements1[i] * elements2[i]
                return sum
            raise "VectorException.VECTOR_WRONG_SIZES(self.dim(), v1.dim())"
        raise "UNKNOWN_OPERATION.MESSAGE('Scalar product', type(self), type(v1))"

    def vector_product(self, other):
        if isinstance(other, Vector):
            if self.dim() == other.dim() and self.dim() == 3:
                i = Vector([1, 0, 0])
                j = Vector([0, 1, 0])
                k = Vector([0, 0, 1])
                elements1 = self.to()
                elements2 = other.to()
                calculteMatrix = Matrix([[i, j, k], elements1, elements2])
                det = calculteMatrix.determinant()
                return det
            raise "VECTOR_PRODUCT_WRONG_SIZES"
        raise "UNKNOWN_OPERATION.MESSAGE('Scalar product', type(self), type(v1))"

    def length(self):
        elements = self.to()
        length = 0
        for i in range(len(elements)):
            length += elements[i]**2
        length = length ** (1/2)
        return length.__round__(accuracy)

    def normalize(self):
        return self / self.length()

    def __mod__(self, other):
        if isinstance(other, Vector):
            return self.scalar_product(other)
        raise "UNKNOWN_OPERATION.MESSAGE('Scalar product', type(self), type(v1))"

    def __pow__(self, other):
        if isinstance(other, Vector):
            if self.dim() == other.dim():
                return self.vector_product(other)
            raise "VectorException.VECTOR_WRONG_SIZES(self.dim(), other.dim())"
        raise "UNKNOWN_OPERATION.MESSAGE('Vector product', type(self), type(v1))"

    def __getitem__(self, key):
        if isinstance(key, int):
            elements = self.to()
            return elements[key]
        raise TypeError

    def __setitem__(self, key, value):
        if isinstance(key, int):
            n = self.n
            m = self.m
            if n == 1 and m == 1:
                if isinstance(self.elements[0], list):
                    self.elements[0][0] = value
                else:
                    self.elements[0] = value
            elif n == 1:
                self.elements[key] = value
            elif m == 1:
                self.elements[key][0] = value
        raise TypeError
