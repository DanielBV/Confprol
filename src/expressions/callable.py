from typing import  List

from src.exceptions import ReturnException


class Callable:

    def __init__(self, arguments:List[str],name):
        self.__arguments = arguments # argument name
        self.name = name

    def get_parameters(self):
        return self.__arguments

    def get_name(self):
        return self.name

    def run(self,values):
        if len(values) != len(self.__arguments):
            missing_arguments = self.__arguments[len(values):]
            raise ValueError(f"Argument number mismatch in {self.name}. Missing {missing_arguments} ")

        return self._run(values)

    def _run(self, values):
        raise NotImplementedError("Callable 'run' not implemented")

