from .callable import Callable
from src.expressions.basic_expression import Expression

class PythonMethod(Callable):

    def __init__(self, arguments, run_function, called_on:Expression):
        super(PythonMethod, self).__init__(arguments)
        self._run = run_function
        self.called_on =called_on

    def run(self, values):
        """
        :param values:  Arguments of the method except the instance.
        :return:
        """
        values.insert(0, self.called_on)

        return super(PythonMethod, self).run(values)

