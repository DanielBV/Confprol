from typing import  List

from src.exceptions import ReturnException
from ..none import confprol_none
from .callable import Callable


class CallableFunction(Callable):

    def __init__(self, arguments:List[str], function_tree, visitor: 'MyVisitor'):
        self.__arguments = arguments
        self.__function_content = function_tree
        self.visitor = visitor

        self.context = self.visitor.get_context()


        super(CallableFunction, self).__init__(arguments)

    def get_parameters(self):
        return self.__arguments

    def _run(self, values):

        args = dict(zip(self.__arguments, values))
        old_state = self.context
        new_state = old_state.create_subcontext()
        new_state.set_variables(args)
        self.visitor.set_context(new_state)

        try:
            for statement in self.__function_content:
                self.visitor.visitStatement(statement)
        except ReturnException as e:
            self.visitor.set_context(old_state)
            return e.return_value


        self.visitor.set_context(old_state)
        return confprol_none

