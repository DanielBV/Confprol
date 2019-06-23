



from src.expressions.callable.callable import Callable
from src.exceptions import  NotCallable, VariableNotDefined, RuntimeException, TooManyArguments, ArgumentsMissing
from src.expressions import Expression,StringExpression, ListExpression
from src.type import ValueType
from src.context import Context



class ConfprolHandler:

    def __init__(self):
        self.context = Context()

    def load_string(self, text: str):
        text = text[1:len(text) - 1]
        return StringExpression(text, text)

    def runFunction(self, callable: Callable, arguments,line):
        if callable.type != ValueType.FUNCTION:
            raise RuntimeException(line,NotCallable(callable.name))

        try:
            return callable.run(arguments)
        except (ArgumentsMissing,TooManyArguments) as e:
            raise RuntimeException(line,e)

    def get_attribute(self,attribute,line):
        if self.context.has_attribute(attribute):
            return self.context.get_attribute(attribute)
        else:
            raise RuntimeException(line,VariableNotDefined(attribute))

    def load_float(self, float:float):
        return Expression(float, str(float), ValueType.NUMBER)

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

    def load_list(self, values):
        expression_names = list(map(lambda expr: expr.name,values))
        name = "[" + ",".join(expression_names) + "]"
        return ListExpression(values,name)

    def print_expression(self, value):
        print(value)