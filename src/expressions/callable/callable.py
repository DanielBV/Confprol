from typing import  List
from src.exceptions import ArgumentsMissing, TooManyArguments
from ..none import confprol_none
from ..confprol_object import ConfprolObject

class Callable(ConfprolObject):

    def __init__(self, arguments:List[str]):
        self.__arguments = arguments # argument name
        
        super(Callable, self).__init__(self)

    def get_parameters(self):
        return self.__arguments


    def run(self,values):
        parameters = self.get_parameters()

        if len(values) < len(parameters):
            missing_arguments = parameters[len(values):]
            raise ArgumentsMissing( None, missing_arguments)
        if len(values) > len(parameters):
            extra_arguments = list(map(lambda arg: arg.name, values))

            raise TooManyArguments("Too many arguments",   None, extra_arguments)

        object = self._run(values)

        if object is None:
            return confprol_none
        else:
            return object

    def _run(self, values):
        raise NotImplementedError("Callable 'run' not implemented")


