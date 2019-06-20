



from src.expressions.callable.callable import Callable
from src.exceptions import  NotCallable,ArgumentsMissing, TooManyArguments, VariableNotDefined
from src.expressions import Expression,StringExpression
from src.type import ValueType
from src.context import Context



class ConfprolHandler:

    def __init__(self):
        self.context = Context()

    def load_string(self, text: str):
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

    def get_attribute(self,attribute,line):
        if self.context.has_attribute(attribute):
            return self.context.get_attribute(attribute)
        else:
            raise VariableNotDefined(attribute, line)

    def load_float(self, float:float):
        return Expression(float, str(float), ValueType.FLOAT)

    def load_boolean(self, boolean:bool):
        return Expression(boolean, str(boolean), ValueType.BOOLEAN)

    def load_number(self, number:int):
        return Expression(number, str(number), ValueType.NUMBER)

    def assign_variable(self, variable, value):
        self.context.set_variable(variable,value)
        value.name = variable # TODO Might need a deep copy if a=b


    def has_attribute(self,attribute):
        return self.context.has_attribute(attribute)

    def set_context(self, context):
        self.context = context