from enum import Enum

class FloorType(Enum):

    @classmethod
    def get_all(cls):
        return [e.value for e in FloorType]

    BASEMENT = 0
    GROUND = 1
    UPPER = 2