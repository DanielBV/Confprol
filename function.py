from typing import  List

class Function:

    def __init__(self, arguments:List[str], function_tree, visitor:'MyVisitor'):
        self.__arguments = arguments # argument name
        self.__function_content = function_tree
        print(self.__arguments)
        print(self.__function_content)
        self.visitor = visitor


    def run(self, values):
        if len(values) != len(self.__arguments):
            raise ValueError("Argument number mismatch") #TODO Improve

        args = dict(zip(self.__arguments, values))

        old_state = self.visitor.context
        self.visitor.context = args #TODO Make context an object

        for statement in self.__function_content:
            self.visitor.visitStatement(statement)

        self.visitor.context = old_state
