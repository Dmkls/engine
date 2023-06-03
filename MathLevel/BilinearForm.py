from Vector import *
from Exceptions.exceptionsMath import *


def BilinearForm(matrix, v1, v2):
    if isinstance(matrix, Matrix) and isinstance(v1, Vector) and isinstance(v2, Vector):
        if matrix.n == matrix.m:
            if v1.dim() == v2.dim():
                if matrix.n == v1.dim():
                    sum = 0
                    for i in range(matrix.n):
                        for j in range(matrix.n):
                            sum += matrix.elements[i][j] * v1[i] * v2[j]
                    return sum
                raise "MatrixException.MATRIX_WRONG_SIZES(matrix.n, matrix.m, v1.n, v1.m)"
            raise "VectorException.VECTOR_WRONG_SIZES(v1.dim(), v2.dim())"
        raise "MatrixException.NOT_SQUARE_MATRIX(matrix.n, matrix.m)"
    raise TypeError