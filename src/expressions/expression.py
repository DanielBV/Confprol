
from src.type import ValueType


class Expression():



    def __init__(self, value, name,type_:ValueType):
        self.value = value
        self.name  = name
        self.attributes = {}
        self.__type = type_




    @property
    def type(self):
        return self.__type


    def get_attribute(self, attribute):

        if attribute in self.attributes:
            return self.attributes[attribute]
        else:
            raise ValueError(f"Expressions of type {self.type} don't have an attribute {attribute} ")
        #TODO return none instead of exception?
    def has_attribute(self,attribute):
        return attribute in self.attributes
