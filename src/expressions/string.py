from src.expressions.confprol_object import ConfprolObject
from .basic_expression import BasicExpression
from src.type import ValueType
from src.expressions.callable import  PythonMethod
from typing import List
from src.expressions.runnable_expression import RunnableExpression


def length_function(expr:List[BasicExpression]):
    expr = expr[0]
    value = len(expr.value)

    return BasicExpression(ConfprolObject(value), f"length({expr.name})", ValueType.NUMBER)

class StringExpression(BasicExpression):

    def __init__(self,value,name):
        super(StringExpression, self).__init__(value,name,ValueType.STRING)

        self.set_attribute("length",RunnableExpression(PythonMethod(["this"],length_function,self),"length"))

    def __str__(self):
        return self.value

    def copy(self):
        return StringExpression(self.object,self.name)