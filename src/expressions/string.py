
from .expression import Expression
from src.type import ValueType
from .python_callable import  PythonCallabe
from typing import List
#TODO make relative import

def length_function(expr:List[Expression]):
    expr = expr[0]
    value = len(expr.value)
    return Expression(value,value,ValueType.NUMBER)

class StringExpression(Expression):

    def __init__(self,string):
        super(StringExpression, self).__init__(string,string,ValueType.STRING)

        length = Expression(None,None,ValueType.FUNCTION)#TODO Refactor to make this cleaner

        self.attributes["length"] = PythonCallabe(["this"],"length",length_function)
