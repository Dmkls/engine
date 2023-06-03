class EngineException(Exception):
    pass


class MatrixException(EngineException):

    MATRIX_WRONG_INPUT = "Matrix with these parameters can not be created"

    MATRIX_IS_SINGULAR = "Inverse matrix can't be found because the matrix is singular"

    @staticmethod
    def MATRIX_WRONG_SIZES(n1, n2, m1, m2):
        return f"Wrong sizes: {n1}x{m1} and {n2}x{m2}"

    @staticmethod
    def NOT_SQUARE_MATRIX(n, m):
        return f"Matrix {n}x{m}. The determinant can't be found because the matrix is not square"


class VectorException(EngineException):

    VECTOR_WRONG_INPUT = "Vector with these parameters can not be created"

    VECTOR_PRODUCT_WRONG_SIZES = "Vector product is defined only for vectors of size 3"

    @staticmethod
    def VECTOR_WRONG_SIZES(n1, n2):
        return f"Wrong sizes: {n1} and {n2}"


class PointException(EngineException):

    POINT_WRONG_INPUT = "Point with these parameters can't be created"

    POINT_UNKNOWN_OPERATION = "This operation isn’t defined for point"


class UNKNOWN_OPERATION(EngineException):

    @staticmethod
    def MESSAGE(operation, obj1, obj2=None):
        obj1 = str(obj1)
        obj2 = str(obj2)
        a = obj1.find('.')
        obj1 = obj1[a+1:-2]
        a = obj2.find('.')
        obj2 = obj2[a+1:-2]
        if obj2 is not None:
            return f"{operation} isn't defined for {obj1} and {obj2}"
        return f"{operation} isn't defined for {obj1}"


class WRONG_INPUT(EngineException):

    @staticmethod
    def MESSAGE(waiting, received):
        waiting = str(waiting)
        received = str(received)
        a = received.find('.')
        received = received[a + 1:-2]
        print(f"Wrong input. Waiting {waiting}, but received {received}.")
