
from .basic_expression import BasicExpression
from src.type import ValueType
from src.expressions.callable import  PythonMethod
from src.expressions.runnable_expression import RunnableExpression
from .common_methods import length_function



class StringExpression(BasicExpression):

    def __init__(self, object, name):
        super(StringExpression, self).__init__(object, name, ValueType.STRING)

        self.set_attribute("length",RunnableExpression(PythonMethod(["this"],length_function,self),"length"))

    def __str__(self):
        return self.value

    def copy(self):
        return StringExpression(self.object,self.name)