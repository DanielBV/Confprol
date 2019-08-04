from expressions.object_expression import ObjectExpression
from expressions import RunnableExpression
from expressions.callable import  PythonCallabe
from exceptions.confprol_value_error import ConfprolValueError
from expressions import BasicExpression, StringExpression
from type import ValueType
from expressions.objects.confprol_object import ConfprolObject
from multimethods.multimethod import typemultimethod, multimethod
from expressions.booleans.quantic_axis import QuanticAxis
from expressions.booleans.quantic_boolean import QuanticBoolean
from expressions.confprol_list import ListExpression
from utilities.string_algorithm import string_algorithm
from expressions.none import confprol_none
from expressions.booleans.million_to_one import MillionToOneChance
from expressions.booleans.true_except_fridays import TrueExceptFridays
import  string

import random

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
        raise ConfprolValueError(f"The string/variable '{expression.name}' can't be transformed to integer.")


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
        raise ConfprolValueError(f"The string/variable '{expression.name}' can't be transformed to float.")


@typemultimethod(object)
def to_float(expression):
    raise ConfprolValueError(f"Cannot transform an object of type {expression.type} to float.")


def to_string(expression):
    value = str(expression)
    return StringExpression(ConfprolObject(value),value)


def get_input(message):
    value = input(message)
    input_ = string_algorithm(value)
    return StringExpression(ConfprolObject(input_),input_)


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

@typemultimethod(ValueType.NUMBER, ValueType.NUMBER)
def confprol_range(start_expr,end_expr):
    start = start_expr.value
    end = end_expr.value

    if not type(start)==int:
        raise ConfprolValueError(f"The start value in range() must be an integer.")

    if not type(end)==int:
        raise ConfprolValueError(f"The end value in range() must be an integer.")

    range_ = range(start,end)
    list_ = map(lambda x: BasicExpression(ConfprolObject(x),x,ValueType.NUMBER),range_)
    return ListExpression(ConfprolObject(list_),f"range({start},{end})")

@typemultimethod(object,object)
def confprol_range(start,end):
    raise ConfprolValueError(f"The start and end in range() must be integers.")

def confprol_random():
    element = random.randint(0,21)

    if element in [0,1]:
        return BasicExpression(ConfprolObject(bool(element)),"random()",ValueType.BOOLEAN)
    elif element in range(2,6):
        value = random.randint(-10000000000000,10000000000000)
        return BasicExpression(ConfprolObject(value),"random()",ValueType.NUMBER)
    elif element in range(6,10):
        value = random.uniform(-10000000000000, 10000000000000)
        return BasicExpression(ConfprolObject(value), "random()", ValueType.NUMBER)
    elif element == 10:
        return confprol_none
    elif element == 1:
        return TrueExceptFridays()
    elif element == 12:
        return MillionToOneChance()
    elif element in range(13,17):
        axis = random.randint(0,1)
        value = random.randint(0,1)

        return QuanticBoolean(QuanticAxis(axis),bool(value))
    elif element in range(17,19):
        list_ = ListExpression(ConfprolObject([]),"random()")
        element = random.randint(0, 4)
        while element !=0:
            list_.append(confprol_random())
            element = random.randint(0, 4)
        return list_

    else:
        length = random.randint(0, 100)
        value = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase,k=length))
        return StringExpression(ConfprolObject(value),"random()")




object_constructor = RunnableExpression(PythonCallabe([],new_object),"object")
function_has_attribute = RunnableExpression(PythonCallabe(["object","attribute"],has_attribute),"has_attribute")
function_to_integer = RunnableExpression(PythonCallabe(["element"],lambda args: to_integer(args[0]) ),"int")
function_to_float = RunnableExpression(PythonCallabe(["element"],lambda args: to_float(args[0]) ),"float")
function_to_string = RunnableExpression(PythonCallabe(["element"],lambda args: to_string(args[0]) ),"string")
function_input = RunnableExpression(PythonCallabe(["prompt"],lambda args: get_input(args[0])),"ask_user_to_type_words_to_use_them_for_something")
function_evaluate_x = RunnableExpression(PythonCallabe(["quantic_boolean"],lambda args: evaluate_quantic_x(args[0])),"evalX")
function_evaluate_y = RunnableExpression(PythonCallabe(["quantic_boolean"],lambda args: evaluate_quantic_y(args[0])),"evalY")
function_range = RunnableExpression(PythonCallabe(["start","end"],lambda args: confprol_range(args[0],args[1])),"range")
function_random = RunnableExpression(PythonCallabe([],lambda args: confprol_random()),"random")

default_functions = {"object":object_constructor, "has_attribute":function_has_attribute, "int":function_to_integer,
                     "float":function_to_float, "string":function_to_string, "ask_user_to_type_words_to_use_them_for_something":function_input,
                     "evalX":function_evaluate_x,"evalY":function_evaluate_y, "range":function_range ,"random":function_random}

