from .callable import Callable


class PythonCallabe(Callable):

    def __init__(self,arguments,name, run_function):
        super(PythonCallabe, self).__init__(arguments,name)
        self._run = run_function

    def copy(self):
        return PythonCallabe(self.value,self.name,self._run)