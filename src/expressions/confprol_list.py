from src.type import ValueType
from .expression import Expression
from typing import  List
from .callable import  PythonMethod
from src.exceptions import ElementNotContained


def get_position(arguments):
    list_ = arguments[0].value
    pos = arguments[1].value

    return list_[pos]


def length_function(expr:List[Expression]): #TODO avoid duplication with string
    expr = expr[0]
    value = len(expr.value)
    return Expression(value,f"length({expr.name})",ValueType.NUMBER)

def append(arguments:List[Expression]):
    list_ = arguments[0]
    expr = arguments[1]

    list_.append(expr)

def remove(arguments:List[Expression]):
    list_ = arguments[0]
    expr = arguments[1]

    list_.remove(expr)

def insert(arguments:List[Expression]):
    #TODO check position is an integer (multimethods?)
    list_ = arguments[0]
    position = arguments[1].value
    expr = arguments[2]

    list_.insert(position,expr)

class ListExpression(Expression):


    def __init__(self,values:List[Expression],name):
        super(ListExpression, self).__init__(values,name,ValueType.LIST)

        self.attributes["get"] = PythonMethod(["self","position"],"get",get_position,self) #TODO refactor to avoid creating multiple times the same method object
        self.attributes["length"] = PythonMethod(["self"], "get", length_function,self)
        self.attributes["append"] = PythonMethod(["self","value"],"append", append, self)
        self.attributes["remove"] = PythonMethod(["self", "value"], "remove", remove,self)
        self.attributes["insert"] = PythonMethod(["self", "position", "value"], "insert", insert,self)

    def __str__(self):
        values = map(lambda expr:str(expr),self.value)
        return "[" + ",".join(values) + "]"

    def append(self, expr):
        self.value.append(expr)

    def get_deep_value(self):
        return list(map(lambda expr:expr.get_deep_value(),self.value))

    def remove(self,expr):
        #TODO Be careful with 'get_deep_value' if I add objects, a=Object(1), b=Object(1) [a,b].remove(Object(1))
        # should throw ValueError
        values = list(map(lambda expr:expr.get_deep_value(), self.value))
        deep_expr = expr.get_deep_value()
        if deep_expr in values:
            i = values.index(expr.get_deep_value())
            self.value.pop(i)
        else:
            raise ElementNotContained(self.name,expr) #TODO Make a better exception system to add line easier

    def insert(self, position, expr):
        self.value.insert(position,expr)