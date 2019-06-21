
from .expression import Expression
from src.type import ValueType
from src.expressions.callable.python_callable import  PythonCallabe
from typing import List


def length_function(expr:List[Expression]):
    expr = expr[0]
    value = len(expr.value)
    return Expression(value,f"length({expr.name})",ValueType.NUMBER)

class StringExpression(Expression):

    def __init__(self,value,name):
        super(StringExpression, self).__init__(value,name,ValueType.STRING)

        self.attributes["length"] = PythonCallabe(["this"],"length",length_function)

    def __str__(self):
        return self.value