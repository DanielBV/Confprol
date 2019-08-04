
from .basic_expression import BasicExpression
from type import ValueType
from expressions.objects.confprol_object import ConfprolObject



confprol_none = BasicExpression(ConfprolObject(None), None, ValueType.NONE)