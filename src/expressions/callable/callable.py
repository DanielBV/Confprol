from typing import  List
from src.expressions.expression import Expression
from src.type import ValueType
from src.exceptions import ArgumentsMissing, TooManyArguments

class Callable(Expression):

    def __init__(self, arguments:List[str],name):
        self.__arguments = arguments # argument name
        self.function_name = name
        
        super(Callable, self).__init__(None,name,ValueType.FUNCTION)

    def get_parameters(self):
        return self.__arguments

    def get_name(self):
        return self.name

    def run(self,values):
        parameters = self.get_parameters()

        if len(values) < len(parameters):
            missing_arguments = parameters[len(values):]
            raise ArgumentsMissing( self.get_name(), missing_arguments)
        if len(values) > len(parameters):
            extra_arguments = list(map(lambda arg: arg.name, values))

            raise TooManyArguments("Too many arguments",   self.get_name(), extra_arguments)


        return self._run(values)

    def _run(self, values):
        raise NotImplementedError("Callable 'run' not implemented")

    def copy(self):
        raise NotImplementedError("Callable 'copy' not implemented")

    def __str__(self):
        return f"[function {self.function_name}]"