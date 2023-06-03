from Math import *
from Exceptions.exceptionsMath import *


class Matrix:

    def __init__(self, *args):
        l = len(args)
        if l == 1:
            if isinstance(args[0], Vector):
                self.n = args[0].n
                self.m = args[0].m
                self.elements = []
                for i in range(args[0].dim()):
                    self.elements.append(args[0].elements[i])
            elif isinstance(args[0], int):
                self.n = args[0]
                if isinstance(self, Matrix):
                    self.m = args[0]
                if isinstance(self, Vector):
                    self.m = 1
                self.elements = []
                for i in range(self.n):
                    self.elements.append([])
                    for j in range(self.m):
                        self.elements[i].append(0)
            elif isinstance(args[0], list):
                if isinstance(args[0][0], list):
                    self.n = len(args[0])
                    self.m = len(args[0][0])
                elif isinstance(args[0][0], int) or isinstance(args[0][0], float):
                    self.n = 1
                    self.m = len(args[0])
                self.elements = args[0]
            else:
                if isinstance(self, Point):
                    raise "POINT_WRONG_INPUT"
                elif isinstance(self, Vector):
                    raise "VECTOR_WRONG_INPUT"
                raise "MATRIX_WRONG_INPUT"
        elif l == 2:
            if isinstance(self, Vector):
                raise "VECTOR_WRONG_INPUT"
            elif isinstance(args[0], int) and isinstance(args[1], int):
                self.n = args[0]
                self.m = args[1]
                self.elements = []
                for i in range(self.n):
                    self.elements.append([])
                    for j in range(self.m):
                        self.elements[i].append(0)
        else:
            if isinstance(self, Point):
                raise "POINT_WRONG_INPUT"
            elif isinstance(self, Vector):
                raise "VECTOR_WRONG_INPUT"
            raise "MATRIX_WRONG_INPUT"

    def __add__(self, other):
        if isinstance(self, Point) and isinstance(other, Point):
            raise "POINT_UNKNOWN_OPERATION"
        if isinstance(other, Vector):
            if other.dim() == self.dim():
                buffObject = Vector(self.dim())
                elements1 = self.to()
                elements2 = other.to()
                for i in range(self.dim()):
                    buffObject.elements[i][0] = elements1[i] + elements2[i]
                if isinstance(self, Point) or isinstance(other, Point):
                    buffObject = Point(buffObject)
                return buffObject
            raise "VECTOR_WRONG_SIZES(self.dim(), other.dim())"
        if isinstance(other, Matrix):
            if other.n == self.n and other.m == self.m:
                buffMatrix = Matrix(self.n, self.m)
                for i in range(self.n):
                    for j in range(self.m):
                        buffMatrix.elements[i][j] = self.elements[i][j] + other.elements[i][j]
                return buffMatrix
            raise "MATRIX_WRONG_SIZES(self.n, self.m, other.n, other.m)"
        raise "UNKNOWN_OPERATION.MESSAGE('Addition', type(self), type(other)"

    def __mul__(self, other):
        if isinstance(self, Vector):
            if self.n == 1:
                if isinstance(other, int) or isinstance(other, float):
                    buffVector = self.transpose()
                    buffVector *= other
                    buffVector = buffVector.transpose()
                    return buffVector
            if isinstance(other, Matrix) and not isinstance(other, Vector):
                if self.dim() == other.n or other.n == 1:
                    if self.n == other.n:
                        self.transpose()
                    buffVector = Vector(other.m)
                    for i in range(other.m):
                        for j in range(other.n):
                            buffVector.elements[i][0] += self[j] * other.elements[j][i]
                    return buffVector
                raise "MATRIX_WRONG_SIZES(self.n, self.m, other.n, other.m)"
        if isinstance(other, Matrix):
            if self.m == other.n:
                buffMatrix = Matrix(self.n, other.m)
                for i in range(self.n):
                    for j in range(other.m):
                        for k in range(self.m):
                            buffMatrix.elements[i][j] += self.elements[i][k] * other.elements[k][j]
                        buffMatrix.elements[i][j] = round(buffMatrix.elements[i][j], accuracy)
                return buffMatrix
            raise "MATRIX_WRONG_SIZES(self.n, self.m, other.n, other.m)"
        elif isinstance(other, float) or isinstance(other, int):
            if isinstance(self, Vector):
                buffObject = Vector(self.n)
            elif isinstance(self, Matrix):
                buffObject = Matrix(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    buffObject.elements[i][j] = (self.elements[i][j] * other).__round__(accuracy)
            return buffObject
        raise "UNKNOWN_OPERATION.MESSAGE('Multiplication', type(self), type(other)"

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        if isinstance(self, Point) and isinstance(other, Point):
            raise "POINT_UNKNOWN_OPERATION"
        if ((isinstance(other, Vector) and self.dim() == other.dim()) or
                (isinstance(other, Matrix) and (self.n == other.n) and (self.m == other.m))):
            return self + -other
        raise "UNKNOWN_OPERATION.MESSAGE('Subtraction', type(self), type(other)"

    def __invert__(self):  # ~
        if not isinstance(self, Vector) and not isinstance(self, Point):
            return self.inverse()
        else:
            raise "UNKNOWN_OPERATION.MESSAGE('Inversion', type(self)"

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if other != 0:
                return self * (1 / other)
            raise ZeroDivisionError
        elif isinstance(other, Matrix):
            if not isinstance(other, Vector):
                return self * ~other
        raise "UNKNOWN_OPERATION.MESSAGE('Division', type(self), type(other)"

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.elements[key]
        raise TypeError

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self[key] = value
        raise TypeError

    def __eq__(self, other):
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if self.elements == other.elements:
                return True
            return False

    def get_minor(self, lines, rows):
        if isinstance(lines, list) and isinstance(rows, list):
            for i in range(len(lines)):
                if not isinstance(lines[i], int):
                    raise TypeError
            for i in range(len(rows)):
                if not isinstance(rows[i], int):
                    raise TypeError
            if (self.n - len(lines) == 0) or (self.m - len(rows) == 0):
                return Matrix(0)
            buffMatrix = Matrix(self.n - len(lines), self.m - len(rows))
            k = 0
            for i in range(self.n):
                if not (i in lines):
                    l = 0
                    for j in range(self.m):
                        if not (j in rows):
                            buffMatrix.elements[k][l] = self.elements[i][j]
                            l += 1
                    k += 1
            return buffMatrix
        raise TypeError

    def determinant(self):
        if self.n == self.m:
            elements = self.elements
            n = self.n
            if n == 1:
                return elements[0][0]
            elif n == 2:
                return elements[0][0] * elements[1][1] - \
                    elements[0][1] * elements[1][0]
            elif n == 3:
                det = elements[0][0] * (elements[1][1] * elements[2][2] - elements[1][2]*elements[2][1]) - \
                      elements[0][1] * (elements[1][0] * elements[2][2] - elements[1][2] * elements[2][0]) + \
                      elements[0][2] * (elements[1][0] * elements[2][1] - elements[1][1] * elements[2][0])
                return det
            else:
                elements = []
                for i in range(n):
                    elements.append([])
                    for j in range(n):
                        elements[i].append(self.elements[i][j])
                dlc = 1
                for i in range(n - 1):
                    if elements[i][i] == 0:
                        swap = 0
                        for j in range(i + 1, n):
                            if elements[j][i] != 0:
                                elements[j], elements[i] = elements[i], elements[j]
                                swap = 1
                                dlc *= -1
                                break
                        if swap != 1:
                            return 0
                    k = elements[i][i]
                    if k != 0:
                        dlc *= k
                        for j in range(n):
                            elements[i][j] /= k
                        for j in range(i + 1, n):
                            k = elements[j][i]
                            for t in range(i, n):
                                elements[j][t] -= k * elements[i][t]
                return elements[n - 1][n - 1] * dlc.__round__(10)
        raise "NOT_SQUARE_MATRIX(self.n, self.m)"

    def inverse(self):
        if self.n == self.m:
            if self.determinant():
                n = self.n
                determinant = self.determinant()
                if n == 1:
                    return self / (2 * determinant)
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

    @staticmethod
    def identity(n):
        if isinstance(n, int):
            identityMatrix = Matrix(n)
            for i in range(n):
                identityMatrix.elements[i][i] = 1
            return identityMatrix
        raise TypeError

    def transpose(self):
        if isinstance(self, Vector):
            n = self.n
            m = self.m
            if m == 1 and n == 1:
                buffVector = Vector(1)
                if isinstance(self.elements[0], int) or isinstance(self.elements[0], float):
                    buffVector.elements[0][0] = self.elements[0]
                    return buffVector
                else:
                    buffVector.elements[0] = self.elements[0][0]
                    return buffVector
            elements = []
            for i in range(max(n, m)):
                elements.append(self.elements[i])
            if n == 1:
                for i in range(m):
                    elements[i] = [elements[i]]
            else:
                for i in range(n):
                    elements[i] = elements[i][0]
            buffVector = Vector(elements)
            return buffVector
        elif isinstance(self, Matrix):
            buffMatrix = Matrix(self.m, self.n)
            for i in range(self.n):
                for j in range(self.m):
                    buffMatrix.elements[j][i] = self.elements[i][j]
            return buffMatrix
        raise TypeError

    def norm(self):
        sum = 0
        for i in range(self.n):
            for j in range(self.m):
                sum += self.elements[i][j] ** 2
        return sum ** (1 / 2)

    @staticmethod
    def gram(*args):
        if isinstance(args[0], list):
            args = args[0]
        n = len(args)
        for i in range(n):
            if not isinstance(args[i], Vector) or args[i].dim() != n:
                raise "error"
        buffMatrix = Matrix(n)
        for i in range(n):
            for j in range(n):
                buffMatrix.elements[i][j] = args[i] % args[j]
        return buffMatrix

    @staticmethod
    def get_rotation_matrix(i, j, angle, n):
        if isinstance(i, int) and isinstance(j, int):
            if isinstance(angle, int) or isinstance(angle, float):
                if isinstance(n, int):
                    buffMatrix = Matrix.identity(n)
                    buffMatrix.elements[i][i] = round(cos(angle), accuracy)
                    buffMatrix.elements[j][j] = round(cos(angle), accuracy)
                    buffMatrix.elements[i][j] = round(((-1)**(i+j))*sin(angle), accuracy)
                    buffMatrix.elements[j][i] = round(((-1)**(i+j+1))*sin(angle), accuracy)
                    return buffMatrix
        raise TypeError

    @staticmethod
    def get_teit_bryan_matrix(angle1, angle2, angle3):
        if isinstance(angle1, int) or isinstance(angle1, float):
            if isinstance(angle2, int) or isinstance(angle2, float):
                if isinstance(angle3, int) or isinstance(angle3, float):
                    rx = Matrix.get_rotation_matrix(1, 2, angle1, 3)
                    ry = Matrix.get_rotation_matrix(0, 2, angle2, 3)
                    rz = Matrix.get_rotation_matrix(0, 1, angle3, 3)
                    buffMatrix = rx * ry * rz
                    return buffMatrix
        raise TypeError