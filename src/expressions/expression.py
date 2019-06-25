
from src.type import ValueType
from .confprol_object import ConfprolObject

class Expression:



    def __init__(self, value:ConfprolObject, name,type_:ValueType):
        self.object = value
        self.name  = name
        self.__type = type_


    @property
    def value(self):
        return self.object.value

    @property
    def type(self):
        return self.__type

    def __str__(self):
        return str(self.value)

    def get_attribute(self,attribute):
        return self.object.get_attribute(attribute)

    def set_attribute(self, name, value: 'Expression'):
        self.object.set_attribute(name,value)

    def set_attributes(self, attr):
        self.object.set_attributes(attr)

    def has_attribute(self, attribute):
        return self.object.has_attribute(attribute)

    def get_deep_value(self):
        """
        Returns the value of the expression. If the expression contains subexpressions, it will replace the subexpressions
        with their correspondent'get_deep_value'
        :return:
        """

        return self.value

    def __repr__(self):
        return self.__str__()

    def copy(self):
         return Expression(self.object,self.name,self.type)