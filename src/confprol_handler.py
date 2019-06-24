



from src.expressions.callable.callable import Callable
from src.exceptions import  NotCallable, VariableNotDefined, RuntimeException, TooManyArguments, ArgumentsMissing, \
OperationNotSupported,DivisionByZero
from src.expressions import Expression,StringExpression, ListExpression
from src.expressions.operations import TypeOperations
from src.type import ValueType
from src.context import Context



class ConfprolHandler:

    def __init__(self):
        self.context = Context()

    def load_string(self, text: str):
        text = text[1:len(text) - 1]
        return StringExpression(text, text)

    def run_function(self, callable: Callable, arguments, line):
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
        a =  Expression(number, str(number), ValueType.NUMBER)
        return a

    def assign_variable(self, variable, value):
        self.context.set_variable(variable,value)
        value.name = variable


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

    def division(self, expr1:Expression, expr2:Expression, line):
        try:
            return TypeOperations.div(expr1,expr2)
        except (DivisionByZero, OperationNotSupported) as e:
            raise RuntimeException(line, e)

    def multiplication(self,expr1:Expression,expr2:Expression,line):
        try:
            return  TypeOperations.mult(expr1,expr2)
        except OperationNotSupported as e:
            raise RuntimeException(line, e)

    def equal(self, expr1:Expression, expr2:Expression):
        return TypeOperations.equals(expr1,expr2)

    def minus(self, expr1:Expression, expr2:Expression, line):
        try:
            return TypeOperations.minus(expr1,expr2)
        except OperationNotSupported as e:
            raise RuntimeException(line, e)

    def sum(self, expr1, expr2, line):
        try:
            return TypeOperations.plus(expr1,expr2)
        except OperationNotSupported as e:
            raise RuntimeException(line, e)
