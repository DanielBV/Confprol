from expressions.basic_expression import BasicExpression
from type import ValueType
from .quantic_axis import QuanticAxis
from expressions.objects.quantic_object import QuanticObject
from exceptions  import EvaluateQuanticBooleanError
import random
from expressions.objects.confprol_object import ConfprolObject


class QuanticBoolean(BasicExpression):
    
    def __init__(self,axis:QuanticAxis,value):
        super(QuanticBoolean, self).__init__(QuanticObject(value,axis),"[Quantic boolean]",ValueType.BOOLEAN)

    def get_deep_value(self):
        return self.value
    
    @property
    def value(self):
        raise EvaluateQuanticBooleanError()

    def copy(self):
        copy =  QuanticBoolean(self.object.axis, self.object.value)
        copy.object = self.object
        return copy

    def __str__(self):
        return f"[Quantic Boolean {id(self.object)}]"

    def to_boolean(self):
        raise EvaluateQuanticBooleanError()

    def evaluate(self, axis:QuanticAxis):

        if axis != self.object.axis:
            self.object.axis = axis
            value = random.randint(0,9)
            if value>=5:
                self.object.value = True
            else:
                self.object.value = False

        return BasicExpression(ConfprolObject(self.object.value),f"evalX{self}",ValueType.BOOLEAN)

    def get_exit_value(self):
        return self.object