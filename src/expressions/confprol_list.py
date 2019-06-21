from src.type import ValueType
from .expression import Expression
from typing import  List
from .callable.python_callable import PythonCallabe


def get_position(arguments):
    list_ = arguments[0].value
    pos = arguments[1].value

    return list_[pos]



class ListExpression(Expression):


    def __init__(self,values:List[Expression],name):
        super(ListExpression, self).__init__(values,name,ValueType.LIST)

        self.attributes["get"] = PythonCallabe(["self","position"],"get",get_position)

    def __str__(self):
        values = map(lambda expr:str(expr),self.value)
        return "[" + ",".join(values) + "]"