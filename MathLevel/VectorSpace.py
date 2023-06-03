from Vector import *
from Exceptions.exceptionsMath import *


class VectorSpace:

    def __init__(self, basis):
        if isinstance(basis, list):
            for i in range(len(basis)):
                if not isinstance(basis[i], Vector):
                    raise TypeError
                self.basis = basis

    def scalar_product(self, v1, v2):
        if isinstance(v1, Vector) and (v2, Vector):
            if v1.dim() == v2.dim():
                if len(self.basis) == v1.dim():
                    res = (v1 * Matrix.gram(self.basis))%v2
                    return res
                raise "MatrixException.MATRIX_WRONG_SIZES(v1.n, v1.m, self.n, self.m)"
            raise "VectorException.VECTOR_WRONG_SIZES(v1.dim(), v2.dim())"
        raise "UNKNOWN_OPERATION.MESSAGE('Scalar product', type(v1), type(v2))"

    def vector_product(self, v1, v2):
        if isinstance(v1, Vector) and (v2, Vector):
            if v1.dim() == v2.dim():
                if v1.dim() == 3:
                    if len(self.basis) == v1.dim():
                        elements1 = v1.to()
                        elements2 = v2.to()
                        calculteMatrix = Matrix([[self.basis[0], self.basis[1], self.basis[2]], elements1, elements2])
                        det = calculteMatrix.determinant()
                        return det
                raise "VectorException.VECTOR_PRODUCT_WRONG_SIZES"
            raise "VECTOR_PRODUCT_WRONG_SIZES(v1.dim(), v2.dim())"
        raise "UNKNOWN_OPERATION.MESSAGE('Vector product', type(v1), type(v2))"

    def as_vector(self, pt):
        if isinstance(pt, Point):
            n = len(self.basis)
            buffMatrix = Matrix(n)
            for i in range(n):
                buffMatrix.elements[i] = self.basis[i].elements
            buffMatrix = buffMatrix.transpose()

        if buffMatrix.n == buffMatrix.m:
            if buffMatrix.determinant():
                n = buffMatrix.n
                determinant = buffMatrix.determinant()
                if n == 1:
                    return buffMatrix / (2 * determinant)
                elif n == 2:
                    line_1 = [self.elements[1][1], -self.elements[0][1]]
                    line_2 = [-self.elements[1][0], self.elements[0][0]]
                    buffMatrix = Matrix([line_1, line_2])
                    buffMatrix /= buffMatrix.determinant()
                    return buffMatrix
                else:
                    buffMatrix = Matrix(n)
                    for i in range(n):
                        for j in range(n):
                            buffMatrix.elements[i][j] = self.elements[i][j]
                    e = Matrix.identity(n)
                    for i in range(n - 1):
                        if abs(buffMatrix.elements[i][i]) == 0:
                            swap = 0
                            for j in range(i + 1, n):
                                if buffMatrix.elements[j][i] != 0:
                                    buffMatrix.elements[j], buffMatrix.elements[i] = \
                                        buffMatrix.elements[i], buffMatrix.elements[j]
                                    e.elements[j], e.elements[i] = e.elements[i], e.elements[j]
                                    swap = 1
                                    break
                            if swap != 1:
                                return 0
                        k = buffMatrix.elements[i][i]
                        for j in range(e.m):
                            buffMatrix.elements[i][j] /= k
                            e.elements[i][j] /= k  # +
                        for j in range(i + 1, n):
                            k = buffMatrix.elements[j][i]
                            for t in range(e.m):
                                buffMatrix.elements[j][t] -= k * buffMatrix.elements[i][t]
                                e.elements[j][t] -= k * e.elements[i][t]
                    k = buffMatrix.elements[n - 1][n - 1]
                    for i in range(n):
                        buffMatrix.elements[n - 1][i] /= k
                        e.elements[n - 1][i] /= k

                    for i in range(2, n + 1):
                        for j in range(i, n + 1):
                            k = buffMatrix.elements[-j][-i + 1]
                            buffMatrix.elements[-j][-i + 1] = 0
                            for t in range(n):
                                e.elements[-j][t] -= k * e.elements[-i + 1][t]
                    for i in range(e.n):
                        for j in range(e.m):
                            e.elements[i][j] = round(e.elements[i][j], accuracy+3)
                    return e
            raise "MATRIX_IS_SINGULAR"
        raise "NOT_SQUARE_MATRIX(self.n, self.m)"