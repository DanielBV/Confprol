

from expressions.basic_expression import BasicExpression
from type import ValueType
from expressions.objects.confprol_object import ConfprolObject
import random

class MillionToOneChance(BasicExpression):

    def __init__(self,object=None):
        if object is None:
            object = ConfprolObject(None)
        super(MillionToOneChance, self).__init__(object, "MillionToOneChance", ValueType.BOOLEAN)


    @property
    def value(self):
       return self.to_boolean()

    def copy(self):
        return MillionToOneChance(self.object)

    def __str__(self):
        return f"[MillionToOnceChance]"

    def to_boolean(self):
        value = random.randint(0, 9)
        return value != 0
