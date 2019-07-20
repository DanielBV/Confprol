from .expressions.object_expression import ObjectExpression
from .expressions import RunnableExpression
from .expressions.callable import  PythonCallabe
from src.exceptions.confprol_value_error import ConfprolValueError
from .expressions import BasicExpression, StringExpression
from .type import ValueType
from .expressions.confprol_object import ConfprolObject
from .multimethods.multimethod import typemultimethod, multimethod
from src.expressions.booleans.quantic_axis import QuanticAxis
from src.expressions.booleans.quantic_boolean import QuanticBoolean

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


def get_input(message):
    value = input(message)
    return StringExpression(ConfprolObject(value),value)


@multimethod(QuanticBoolean)
def evaluate_quantic_x(expression):
    return expression.evaluate(QuanticAxis.X)

@multimethod(object)
def evaluate_quantic_x(expression):
    raise ConfprolValueError(f"Cannot evaluate a non quantic value.")


@multimethod(QuanticBoolean)
def evaluate_quantic_y(expression):
    return expression.evaluate(QuanticAxis.Y)


@multimethod(object)
def evaluate_quantic_y(expression):
    raise ConfprolValueError(f"Cannot evaluate a non quantic value.")


object_constructor = RunnableExpression(PythonCallabe([],new_object),"object")
function_has_attribute = RunnableExpression(PythonCallabe(["object","attribute"],has_attribute),"has_attribute")
function_to_integer = RunnableExpression(PythonCallabe(["element"],lambda args: to_integer(args[0]) ),"int")
function_to_float = RunnableExpression(PythonCallabe(["element"],lambda args: to_float(args[0]) ),"float")
function_to_string = RunnableExpression(PythonCallabe(["element"],lambda args: to_string(args[0]) ),"string")
function_input = RunnableExpression(PythonCallabe(["prompt"],lambda args: get_input(args[0])),"ask_user_to_type_words_to_use_them_for_something")
function_evaluate_x = RunnableExpression(PythonCallabe(["quantic_boolean"],lambda args: evaluate_quantic_x(args[0])),"evalX")
function_evaluate_y = RunnableExpression(PythonCallabe(["quantic_boolean"],lambda args: evaluate_quantic_y(args[0])),"evalY")


default_functions = {"object":object_constructor, "has_attribute":function_has_attribute, "int":function_to_integer,
                     "float":function_to_float, "string":function_to_string, "ask_user_to_type_words_to_use_them_for_something":function_input,
                     "evalX":function_evaluate_x,"evalY":function_evaluate_y}

