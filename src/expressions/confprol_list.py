from src.type import ValueType
from .basic_expression import BasicExpression
from .expression import Expression
from typing import  List
from .callable import  PythonMethod
from src.exceptions import ElementNotContained
from .confprol_object import ConfprolObject
from  .runnable_expression import RunnableExpression


def get_position(arguments):
    list_ = arguments[0].value
    pos = arguments[1].value

    return list_[pos]


def length_function(expr:List[BasicExpression]):
    expr = expr[0]
    value = len(expr.value)
    return BasicExpression(ConfprolObject(value), f"length({expr.name})", ValueType.NUMBER)

def append(arguments:List[BasicExpression]):
    list_ = arguments[0]
    expr = arguments[1]

    list_.append(expr)

def remove(arguments:List[BasicExpression]):
    list_ = arguments[0]
    expr = arguments[1]

    list_.remove(expr)

def insert(arguments:List[BasicExpression]):
    list_ = arguments[0]
    position = arguments[1].value
    expr = arguments[2]

    list_.insert(position,expr)

class ListExpression(Expression):


    def __init__(self, values:ConfprolObject, name): #TODO refactor
        super(ListExpression, self).__init__(values,name,ValueType.LIST)

        self.set_attribute("get",RunnableExpression(PythonMethod(["self","position"],get_position,self),"get"))
        self.set_attribute("length",RunnableExpression(PythonMethod(["self"], length_function,self),"length"))
        self.set_attribute("append",  RunnableExpression(PythonMethod(["self","value"], append, self),"append"))
        self.set_attribute("remove",RunnableExpression(PythonMethod(["self", "value"], remove,self),"remove"))
        self.set_attribute("insert", RunnableExpression(PythonMethod(["self", "position", "value"],  insert,self),"insert"))


    def __str__(self):
        values = map(lambda expr:str(expr),self.value)
        return "[" + ",".join(values) + "]"

    def append(self, expr):
        self.value.append(expr)

    def get_deep_value(self):
        return list(map(lambda expr:expr.get_deep_value(),self.value))

    def remove(self,expr):

        values = list(map(lambda expr:expr.get_deep_value(), self.value))
        deep_expr = expr.get_deep_value()
        if deep_expr in values:
            i = values.index(expr.get_deep_value())
            self.value.pop(i)
        else:
            raise ElementNotContained(self.name,expr) #

    def insert(self, position, expr):
        self.value.insert(position,expr)

    def copy(self):
        return ListExpression(self.object,self.name)