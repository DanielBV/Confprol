
from .expression import FinalExpression
from src.exceptions import OperationNotSupported
from src.type import ValueType
from .operations import StringOperations

class StringExpression(FinalExpression):


    def minus(self, other: 'FinalExpression'):
        raise OperationNotSupported("-",self,other)

    def plus(self, other: 'FinalExpression'):
       return StringOperations.concatenation(self.value,other.value)



    def div(self, other: 'FinalExpression'):
        raise OperationNotSupported("/", self, other)

    def mult(self, other: 'FinalExpression'):
        raise OperationNotSupported("*", self, other)

    def get_type(self):
        return ValueType.STRING