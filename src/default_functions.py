from .expressions.object_expression import ObjectExpression
from .expressions import RunnableExpression
from .expressions.callable import  PythonCallabe
from src.exceptions.confprol_value_error import ConfprolValueError
from .expressions import BasicExpression, StringExpression
from .type import ValueType
from .expressions.confprol_object import ConfprolObject
from .multimethods.multimethod import typemultimethod

def new_object(args):
    return ObjectExpression("object")

def has_attribute(args):
    expr = args[0]
    attr = args[1].value

    if type(attr)!= str:
        raise ConfprolValueError("The second argument of the function 'has_attribute' must be a string")

    return BasicExpression(ConfprolObject(expr.has_attribute(attr)),f"has_attribute({expr}{attr})",ValueType.BOOLEAN)


@typemultimethod((ValueType.NUMBER,ValueType.BOOLEAN))
def to_integer(expression):
    int_value = int(expression.value)
    return BasicExpression(ConfprolObject(int_value), f"int({expression.value})", ValueType.NUMBER)

@typemultimethod(ValueType.STRING)
def to_integer(expression):
    try:
        int_value = int(float(expression.value))  # First to float to allow strings like "3.2"
        return BasicExpression(ConfprolObject(int_value), f"int({expression.value})", ValueType.NUMBER)
    except ValueError:
        raise ConfprolValueError(f"The string '{expression.value}' can't be transformed to integer.")


@typemultimethod(object)
def to_integer(expression):
    raise ConfprolValueError(f"Cannot transform an object of type {expression.type} to integer.")


@typemultimethod((ValueType.NUMBER,ValueType.BOOLEAN))
def to_float(expression):
    float_value = float(expression.value)
    return BasicExpression(ConfprolObject(float_value), f"float({expression.value})", ValueType.NUMBER)

@typemultimethod(ValueType.STRING)
def to_float(expression):
    try:
        float_value = float(expression.value)
        return BasicExpression(ConfprolObject(float_value), f"int({expression.value})", ValueType.NUMBER)
    except ValueError:
        raise ConfprolValueError(f"The string '{expression.value}' can't be transformed to float.")


@typemultimethod(object)
def to_float(expression):
    raise ConfprolValueError(f"Cannot transform an object of type {expression.type} to float.")


def to_string(expression):
    value = str(expression)
    return StringExpression(ConfprolObject(value),value)



object_constructor = RunnableExpression(PythonCallabe([],new_object),"object")
function_has_attribute = RunnableExpression(PythonCallabe(["object","attribute"],has_attribute),"has_attribute")
function_to_integer = RunnableExpression(PythonCallabe(["element"],lambda args: to_integer(args[0]) ),"int")
function_to_float = RunnableExpression(PythonCallabe(["element"],lambda args: to_float(args[0]) ),"float")
function_to_string = RunnableExpression(PythonCallabe(["element"],lambda args: to_string(args[0]) ),"string")


default_functions = {"object":object_constructor, "has_attribute":function_has_attribute, "int":function_to_integer,
                     "float":function_to_float, "string":function_to_string}

