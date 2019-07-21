
from .basic_expression import BasicExpression
from src.type import ValueType
from src.expressions.objects.confprol_object import ConfprolObject



confprol_none = BasicExpression(ConfprolObject(None), None, ValueType.NONE)