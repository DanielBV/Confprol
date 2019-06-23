from typing import  List

from src.exceptions import ReturnException
from .callable import Callable



class CallableFunction(Callable):

    def __init__(self, arguments:List[str], function_tree,name, visitor: 'MyVisitor'):
        self.__arguments = arguments
        self.__function_content = function_tree
        self.visitor = visitor


        super(CallableFunction, self).__init__(arguments,name)

    def get_parameters(self):
        return self.__arguments

    def get_name(self):
        return self.name

    def _run(self, values):


        args = dict(zip(self.__arguments, values))
        old_state = self.visitor.get_context()
        new_state = old_state.create_subcontext()
        new_state.set_variables(args)

        self.visitor.set_context(new_state)

        try:
            for statement in self.__function_content:
                self.visitor.visitStatement(statement)
        except ReturnException as e:
            self.visitor.context = old_state
            value_names = list(map(lambda a:a.name,values))
            e.return_value.name = f"{self.name}(" + ",".join(value_names)+")"
            #TODO The name doesn't match methods
            return e.return_value


        self.visitor.set_context(old_state)


