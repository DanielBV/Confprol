
from src.type import ValueType

class Expression:



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
            return None

    def has_attribute(self,attribute):
        return attribute in self.attributes

    def __str__(self):
        return str(self.value)

    def get_deep_value(self):
        """
        Returns the value of the expression. If the expression contains subexpressions, it will replace the subexpressions
        with their correspondent'get_deep_value'
        :return:
        """

        return self.value