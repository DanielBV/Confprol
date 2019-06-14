from ..type import ValueType
from . import Expression
from src.exceptions import OperationNotSupported

class TypeOperations:

    @staticmethod
    def plus(expr1:Expression, expr2:Expression):
        if expr1.type == ValueType.STRING or expr2.type == ValueType.STRING:
            return TypeOperations.concatenation(expr1,expr2)

        name = f"{expr1.name} + {expr2.name}"
        value = expr1.value + expr2.value
        return Expression(value, name,ValueType.NUMBER)

    @staticmethod
    def mult(expr1:Expression, expr2:Expression):
        if expr1.type == ValueType.STRING or expr2.type == ValueType.STRING:
            raise OperationNotSupported("*", expr1, expr2)

        name = f"{expr1.name} * {expr2.name}"
        value = expr1.value * expr2.value
        return Expression(value, name,ValueType.NUMBER)

    @staticmethod
    def div(expr1:Expression, expr2:Expression):
        if expr1.type == ValueType.STRING or expr2.type == ValueType.STRING:
            raise OperationNotSupported("/", expr1, expr2)

        name = f"{expr1.name} / {expr2.name}"
        value = expr1.value / expr2.value
        return  Expression(value, name,ValueType.NUMBER)

    @staticmethod
    def minus(expr1:Expression, expr2:Expression):
        if expr1.type == ValueType.STRING or expr2.type == ValueType.STRING:
            raise OperationNotSupported("-", expr1, expr2)

        name = f"{expr1.name} - {expr2.name}"
        value = expr1.value - expr2.value
        return  Expression(value, name,ValueType.NUMBER)

    @staticmethod
    def equals(expr1:Expression, expr2:Expression):
        if expr1.type == ValueType.STRING or expr2.type == ValueType.STRING:
            raise OperationNotSupported("==", expr1, expr2)

        name = f"{expr1.name} == {expr2.name}"
        value = expr1.value == expr2.value
        return  Expression(value, name,ValueType.NUMBER)

    @staticmethod
    def concatenation(expr1:Expression, expr2:Expression):
        value = str(expr1.value) + str(expr2.value)
        return  Expression(value, value,ValueType.STRING)