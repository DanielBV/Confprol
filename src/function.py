from typing import  List

from src.exceptions import ReturnException
from src.expressions.expression import FinalExpression

class Function:

    def __init__(self, arguments:List[str], function_tree,name, visitor: 'MyVisitor'):
        self.__arguments = arguments # argument name
        self.__function_content = function_tree
        self.visitor = visitor
        self.name = name

    def get_parameters(self):
        return self.__arguments

    def get_name(self):
        return self.name

    def run(self, values):
        if len(values) != len(self.__arguments):
            missing_arguments = self.__arguments[len(values):]
            raise ValueError(f"Argument number mismatch in {self.name}. Missing {missing_arguments} ")

        args = dict(zip(self.__arguments, values))
        old_state = self.visitor.context
        self.visitor.context = self.visitor.context.create_subcontext()
        self.visitor.context.set_variables(args)


        try:
            for statement in self.__function_content:
                self.visitor.visitStatement(statement)
        except ReturnException as e:
            self.visitor.context = old_state
            return FinalExpression(e.return_value,f"{self.name}({values})")

        self.visitor.context = old_state


