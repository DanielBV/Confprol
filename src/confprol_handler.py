



from src.expressions.callable.callable import Callable
from src.exceptions import  NotCallable,ArgumentsMissing, TooManyArguments
from src.expressions import Expression,StringExpression
from src.type import ValueType


#TODO Find better name
class ConfprolHandler:
    def loadString(self, text: str):
        # TODO Refactor with an abstract factory
        text = text[1:len(text) - 1]
        return StringExpression(text, text)

    def runFunction(self, callable: Callable, arguments, line):
        if callable.type != ValueType.FUNCTION:
            raise NotCallable()

        parameters = callable.get_parameters()
        if len(arguments) < len(parameters):
            missing_arguments = parameters[len(arguments):]
            raise ArgumentsMissing("Argument number mismatch", line, callable.get_name(),
                                   missing_arguments)
        if len(arguments) > len(parameters):
            extra_arguments = list(map(lambda arg: arg.name, arguments))

            raise TooManyArguments("Too many arguments", line, callable.get_name(), extra_arguments)

        return callable.run(arguments)