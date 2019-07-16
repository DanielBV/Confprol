



from src.exceptions import  NotCallable, VariableNotDefined, RuntimeException, TooManyArguments, ArgumentsMissing, \
OperationNotSupported,DivisionByZero, FileNotFound, CannotOpenDirectory
from src.expressions import BasicExpression,StringExpression, ListExpression,RunnableExpression
from src.expressions.operations import TypeOperations
from src.type import ValueType
from src.context import Context
from src.expressions.confprol_object import ConfprolObject
from src.expressions.none import confprol_none
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
from generated_antlr4.confprolParser import confprolParser

from src.error_listener import  MyErrorListener
from generated_antlr4.confprolLexer import confprolLexer
from src.expressions.object_expression import ObjectExpression
from src.utilities.constants import ENCODING
import os

class ConfprolHandler:

    def __init__(self):
        self.context = Context()

    def load_string(self, text: str):
        text = text[1:len(text) - 1]
        return StringExpression(ConfprolObject(text), text)

    def run_function(self, callable: RunnableExpression, arguments, line):
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
        return BasicExpression(ConfprolObject(float), str(float), ValueType.NUMBER)

    def load_boolean(self, boolean:bool):
        return BasicExpression(ConfprolObject(boolean), str(boolean), ValueType.BOOLEAN)

    def load_number(self, number:int):
        a =  BasicExpression(ConfprolObject(number), str(number), ValueType.NUMBER)
        return a

    def assign_variable(self, variable, value):
        new_value = value.copy()
        self.context.set_variable(variable,new_value)
        new_value.name = variable


    def has_attribute(self,attribute):
        return self.context.has_attribute(attribute)

    def set_context(self, context):
        self.context = context

    def load_list(self, values):
        expression_names = list(map(lambda expr: expr.name,values))
        name = "[" + ",".join(expression_names) + "]"
        return ListExpression(ConfprolObject(values),name)

    def print_expression(self, value):
        print(value)

    def division(self, expr1:BasicExpression, expr2:BasicExpression, line):
        try:
            return TypeOperations.div(expr1,expr2)
        except (DivisionByZero, OperationNotSupported) as e:
            raise RuntimeException(line, e)

    def multiplication(self, expr1:BasicExpression, expr2:BasicExpression, line):
        try:
            return  TypeOperations.mult(expr1,expr2)
        except OperationNotSupported as e:
            raise RuntimeException(line, e)

    def equal(self, expr1:BasicExpression, expr2:BasicExpression):
        return TypeOperations.equals(expr1,expr2)

    def minus(self, expr1:BasicExpression, expr2:BasicExpression, line):
        try:
            return TypeOperations.minus(expr1,expr2)
        except OperationNotSupported as e:
            raise RuntimeException(line, e)

    def sum(self, expr1, expr2, line):
        try:
            return TypeOperations.plus(expr1,expr2)
        except OperationNotSupported as e:
            raise RuntimeException(line, e)

    def load_none(self):
        return confprol_none

    def import_path(self, path,import_id,line):
        from src.visitor import MyVisitor
        try:
            lexer = confprolLexer(FileStream(path,ENCODING))
            stream = CommonTokenStream(lexer)
            parser = confprolParser(stream)
            parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
            parser.addErrorListener(MyErrorListener())


            tree = parser.program()
            visitor = MyVisitor(ConfprolHandler())
            visitor.visit(tree)

            expr = ObjectExpression(import_id)

            imported_variables = visitor.get_context().variables

            expr.set_attributes(imported_variables)
            self.assign_variable(import_id,expr)
        except FileNotFoundError:
            raise RuntimeException(line,FileNotFound(path))
        except (PermissionError,IsADirectoryError):
            raise RuntimeException(line, CannotOpenDirectory(path))

    def in_sum(self, base, other, line):
            new_value = self.sum(base,other,line)
            base.object.value = new_value.object.value

    def in_minus(self, base, other, line):
        new_value = self.minus(base, other, line)
        base.object.value = new_value.object.value

    def in_mult(self, base, other,line):
        new_value = self.multiplication(base, other, line)
        base.object.value = new_value.object.value

    def in_div(self, base, other,line):

        new_value = self.division(base, other, line)
        base.object.value = new_value.object.value


