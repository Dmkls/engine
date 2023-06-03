from Vector import *


def test___init___int_vector():
    # Arrange
    n = 3
    elements = [[0], [0], [0]]

    # Act
    result = Vector(n)

    # Assert
    assert result.elements == elements


def test___init__matrix_vector():
    # Arrange
    elements = [[1], [2], [3]]

    # Act
    result = Vector([[1], [2], [3]])

    # Assert
    assert result.elements == elements


def test___init__list_vector():
    # Arrange
    elements = [1, 2, 3]

    # Act
    result = Vector([1, 2, 3])

    # Assert
    assert result.elements == elements


def test_transpose_vector():
    # Arrange
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([[1], [2], [3]])

    # Act
    result = vector1.transpose()

    # Assert
    assert result == vector2

def test_gram():
    # Arrange
    v1 = Vector([2, 1, 4])
    v2 = Vector([4, 1, 0])
    v3 = Vector([9, 3, 7])
    matrix = Matrix([[21, 9, 49], [9, 17, 39], [49, 39, 139]])

    # Act
    result = Matrix.gram(v1, v2, v3)

    # Assert
    assert result == matrix