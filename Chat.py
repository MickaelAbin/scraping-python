AWAKE="awake"
SLEEP="sleep"

class Chat:
    def __init__(self, name):
        if name:
            self._name = name
        else:
            raise ValueError("Name cannot be empty")
        self._state = AWAKE

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def sleep(self):
        self._state = SLEEP

        
