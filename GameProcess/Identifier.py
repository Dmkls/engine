global identifiers
identifiers = [-1]

class Identifier:
    global identifiers

    def __init__(self):
        self.identifiers = identifiers
        self.value = None

    def get_value(self):
        return self.value

    @staticmethod
    def __generate__():
        ide = identifiers[-1]
        while ide in identifiers:
            ide += 1
        identifiers.append(ide)
        return ide