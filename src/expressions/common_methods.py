from .basic_expression import BasicExpression
from typing import List
from src.expressions.objects.confprol_object import ConfprolObject
from src.type import ValueType

def length_function(expr:List[BasicExpression]):
    expr = expr[0]
    value = len(expr.value)
    return BasicExpression(ConfprolObject(value), f"length({expr.name})", ValueType.NUMBER)