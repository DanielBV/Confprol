
from .expression import Expression
from src.type import ValueType

class Function(Expression):


    def __init__(self, callable):

        super(Function, self).__init__(callable,callable,ValueType.FUNCTION)
        self.attributes["CALL"] = callable
