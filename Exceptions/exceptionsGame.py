class EngineException(Exception):
    pass


class WRONG_INPUT(EngineException):

    @staticmethod
    def MESSAGE(waiting, received):
        waiting = str(waiting)
        received = str(received)
        a = received.find('.')
        received = received[a + 1:-2]
        print(f"Wrong input. Waiting {waiting}, but received {received}.")