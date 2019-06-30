from enum import Enum


class ValueType(Enum):
    STRING = 0
    NUMBER = 1
    BOOLEAN = 2
    FUNCTION = 3
    LIST = 4
    NONE = 5
    OBJECT = 6


    def __str__(self):
        return str(self.name)