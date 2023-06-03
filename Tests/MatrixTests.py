from Matrix import *


def test___init__int():
    # Arrange
    n = 3
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Act
    result = Matrix(n)

    # Assert
    assert result.elements == matrix


def test___init__n_m():
    # Arrange
    n = 2
    m = 3
    matrix = [[0, 0, 0], [0, 0, 0]]

    # Act
    result = Matrix(n, m)

    # Assert
    assert result.elements == matrix


def test___init__list():
    # Arrange
    matrix = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

    # Act
    result = Matrix(matrix)

    # Assert
    assert result.elements == matrix


def test___add__():
    # Arrange
    matrix1 = Matrix([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
    matrix2 = Matrix([[1, 1, 1], [-2, -2, -2], [2, 2, 2]])
    matrix3 = Matrix([[3, 3, 3], [0, 0, 0], [4, 4, 4]])

    # Act
    result = matrix1 + matrix2

    # Assert
    assert result == matrix3


def test___mul__n_n():
    # Arrange
    matrix1 = Matrix([[1, 1], [-1, 1]])
    matrix2 = Matrix([[1, 1], [1, 1]])
    matrix3 = Matrix([[2, 2], [0, 0]])

    # Act
    result = matrix1 * matrix2

    # Assert
    assert result == matrix3


def test___mul__n_m():
    # Arrange
    matrix1 = Matrix([[2, 3, 1], [5, 4, 0]])
    matrix2 = Matrix([[2, 1, 0], [0, 0, 3], [1, 4, 7]])
    matrix3 = Matrix([[5, 6, 16], [10, 5, 12]])

    # Act
    result = matrix1*matrix2

    # Assert
    assert result == matrix3


def test___mul__num():
    # Arrange
    n = 7
    matrix1 = Matrix([[1, 1, 1], [2, 2, 2]])
    matrix2 = Matrix([[7, 7, 7], [14, 14, 14]])

    # Act
    result = matrix1 * n

    # Assert
    assert result == matrix2


def test___truediv__num():
    # Arrange
    matrix1 = Matrix([[10, 10, 10], [20, 20, 20], [-10, -10, -10]])
    matrix2 = Matrix([[2, 2, 2], [4, 4, 4], [-2, -2, -2]])
    n = 5

    # Act
    result = matrix1 / n

    # Assert
    assert result == matrix2


def test___truediv__matrix():
    # Arrange
    matrix1 = Matrix([[10, 10, 10], [20, 20, 20], [-10, -10, -10]])
    matrix2 = Matrix([[2, 1, 0], [0, 0, 3], [1, 4, 7]])
    matrix3 = Matrix([[4.28571, 0.0, 1.42857], [8.57143, 0.0, 2.85714], [-4.28571, 0.0, -1.42857]])

    # Act
    result = matrix1 / matrix2

    # Assert
    assert result == matrix3


def test___neg__matrix():
    # Arrange
    matrix1 = Matrix([[10, 2, 10], [7, 20, 20], [-10, -10, -10], [20, 10, 20]])
    matrix2 = Matrix([[-10, -2, -10], [-7, -20, -20], [10, 10, 10], [-20, -10, -20]])

    # Act
    result = -matrix1

    # Assert
    assert result == matrix2


def test_get_minor():
    # Arrange
    matrix1 = Matrix([[2, 1, 0], [0, 0, 3], [1, 4, 7]])
    matrix2 = Matrix([[0, 3], [4, 7]])

    # Act
    result = matrix1.get_minor([0], [0])

    # Assert
    assert result == matrix2


def test_determinant():
    # Arrange
    matrix = Matrix([[2, 1, 0], [0, 0, 3], [1, 4, 7]])
    det = -21

    # Act
    result = matrix.determinant()

    # Assert
    assert result == det


def test_determinant1():
    # Arrange
    matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    det = 1

    # Act
    result = matrix.determinant()

    # Assert
    assert result == det


def test_determinant2():
    # Arrange
    matrix = Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    det = -1

    # Act
    result = matrix.determinant()

    # Assert
    assert result == det


def test_identity():
    # Arrange
    n = 5
    matrix = Matrix([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])

    # Act
    result = Matrix.identity(n)

    # Assert
    assert result == matrix


def test_inverse():
    # Arrange
    matrix1 = Matrix([[10, 2, 10], [7, 20, 20], [-10, -10, -10]])
    matrix2 = Matrix([[-0.0, -0.07692308, -0.15384615], [-0.125, -0.0, -0.125], [0.125, 0.07692308, 0.17884615]])

    # Act
    result = matrix1.inverse()

    # Assert
    assert result == matrix2


def test_inverse_mul_():
    # Arrange
    matrix1 = Matrix([[10, 2, 10], [7, 20, 20], [-10, -10, -10]])
    matrix2 = Matrix.identity(3)

    # Act
    result = matrix1 * matrix1.inverse()

    # Assert
    assert result == matrix2


def test_transpose():
    # Arrange
    matrix1 = Matrix([[10, 2, 10], [7, 20, 20], [-10, -10, -10], [20, 10, 20]])
    matrix2 = Matrix([[10, 7, -10, 20], [2, 20, -10, 10], [10, 20, -10, 20]])

    # Act
    result = matrix1.transpose()

    # Assert
    assert result == matrix2


def test_norm():
    # Arrange
    matrix = Matrix([[1, 1, 1], [2, 2, 3], [3, 2, 2], [2, 2, 2]])
    norm = 7

    # Act
    result = matrix.norm()

    # Assert
    assert result == norm


def test_get_rotation_matrix():
    # Arrange
    matrix = Matrix([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, -1]])

    # Act
    result = Matrix.get_rotation_matrix(2, 4, 3.141592, 5)

    # Assert
    assert result == matrix


def test_get_teit_bryan_matrix():
    # Arrange
    matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # Act
    result = Matrix.get_teit_bryan_matrix(3.141592, 3.141592, 3.141592)

    # Assert
    assert result == matrix