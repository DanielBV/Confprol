
from src.type import ValueType
from .operations import StringOperations

class FinalExpression:

    #TODO Make interface
    def __init__(self, value, name):
        self.value = value
        self.name  = name


    def plus(self, other:'FinalExpression'):
        if other.get_type()==ValueType.STRING:
            return StringOperations.concatenation(self.value, other.value)

        name = f"{self.name} + {other.name}"
        value = self.value + other.value
        return FinalExpression(value,name)

    def minus(self,other:'FinalExpression'):
        name = f"{self.name} - {other.name}"
        value = self.value - other.value
        return FinalExpression(value, name)

    def div(self, other:'FinalExpression'):
        name = f"{self.name} / {other.name}"
        value = self.value / other.value
        return FinalExpression(value, name)

    def mult(self, other:'FinalExpression'):
        name = f"{self.name} * {other.name}"
        value = self.value * other.value
        return FinalExpression(value, name)

    def equals(self, other:'FinalExpression'):
        value =  self.value == other.value
        name = f"{self.name} == {other.name}"
        return FinalExpression(value, name)

    def get_type(self)->ValueType:
        return ValueType.NUMBER