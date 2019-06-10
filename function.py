from typing import  List
from return_exception import ReturnException

class Function:

    def __init__(self, arguments:List[str], function_tree, visitor: 'MyVisitor'):
        self.__arguments = arguments # argument name
        self.__function_content = function_tree
        self.visitor = visitor


    def run(self, values):
        if len(values) != len(self.__arguments):
            raise ValueError("Argument number mismatch") #TODO Improve

        args = dict(zip(self.__arguments, values))

        old_state = self.visitor.context
        self.visitor.context = args #TODO Make context an object


        try:
            for statement in self.__function_content:
                self.visitor.visitStatement(statement)
        except ReturnException as e:
            self.visitor.context = old_state
            return e.return_value

        self.visitor.context = old_state


