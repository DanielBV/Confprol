
from src.type import ValueType

class Expression():



    def __init__(self, value, name,type_:ValueType):
        self.value = value
        self.name  = name
        self.__type = type_

    @property
    def type(self):
        return self.__type
