from .callable import Callable
from src.expressions import BasicExpression

class PythonMethod(Callable):

    def __init__(self, arguments, name, run_function, called_on:BasicExpression):
        super(PythonMethod, self).__init__(arguments,name)
        self._run = run_function
        self.called_on =called_on

    def run(self, values):
        """
        :param values:  Arguments of the method except the instance.
        :return:
        """
        values.insert(0, self.called_on)

        return super(PythonMethod, self).run(values)

    def copy(self):
        return PythonMethod(self.value,self.name,self._run, self.called_on)