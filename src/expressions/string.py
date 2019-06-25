from src.expressions.confprol_object import ConfprolObject
from .expression import Expression
from src.type import ValueType
from src.expressions.callable import  PythonMethod
from typing import List


def length_function(expr:List[Expression]):
    expr = expr[0]
    value = len(expr.value)

    return Expression(ConfprolObject(value),f"length({expr.name})",ValueType.NUMBER)

class StringExpression(Expression):

    def __init__(self,value,name):
        super(StringExpression, self).__init__(value,name,ValueType.STRING)

        self.set_attribute("length",PythonMethod(["this"],"length",length_function,self))

    def __str__(self):
        return self.value

    def copy(self):
        return StringExpression(self.object,self.name)