from ..type import ValueType
from . import Expression
from src.exceptions import OperationNotSupported, DivisionByZero
from src.multimethods.multimethod import  typemultimethod,DISPATCH_ANY

class TypeOperations:

    @staticmethod
    @typemultimethod((ValueType.NUMBER,ValueType.BOOLEAN),(ValueType.NUMBER,ValueType.BOOLEAN))
    def plus(expr1:Expression, expr2:Expression):
        name = f"{expr1.name} + {expr2.name}"
        value = expr1.value + expr2.value
        return Expression(value, name,ValueType.NUMBER)

    @staticmethod
    @typemultimethod(ValueType.STRING,DISPATCH_ANY)
    @typemultimethod(DISPATCH_ANY, ValueType.STRING)
    def plus(expr1: Expression, expr2: Expression):
        name = f"{expr1.name} + {expr2.name}"
        value = str(expr1.value) + str(expr2.value)
        return  Expression(value,name,ValueType.STRING)

    @staticmethod
    @typemultimethod(DISPATCH_ANY, DISPATCH_ANY)
    def plus(expr1: Expression, expr2: Expression):
        raise OperationNotSupported("+", expr1, expr2)



    @staticmethod
    @typemultimethod((ValueType.NUMBER,ValueType.BOOLEAN), (ValueType.NUMBER,ValueType.BOOLEAN))
    def mult(expr1:Expression, expr2:Expression):
        name = f"{expr1.name} * {expr2.name}"
        value = expr1.value * expr2.value
        return Expression(value, name,ValueType.NUMBER)


    @staticmethod
    @typemultimethod(DISPATCH_ANY,DISPATCH_ANY)
    def mult(expr1:Expression, expr2:Expression):
        raise OperationNotSupported("*", expr1, expr2)

    @staticmethod
    @typemultimethod((ValueType.NUMBER, ValueType.BOOLEAN), (ValueType.NUMBER, ValueType.BOOLEAN))
    def div(expr1:Expression, expr2:Expression):
        name = f"{expr1.name} / {expr2.name}"

        if expr2.value == 0:
            raise DivisionByZero()
        value = expr1.value / expr2.value
        return  Expression(value, name,ValueType.NUMBER)

    @staticmethod
    @typemultimethod(DISPATCH_ANY, DISPATCH_ANY)
    def div(expr1: Expression, expr2: Expression):
        raise OperationNotSupported("/", expr1, expr2)

    @staticmethod
    @typemultimethod((ValueType.NUMBER, ValueType.BOOLEAN), (ValueType.NUMBER, ValueType.BOOLEAN))
    def minus(expr1:Expression, expr2:Expression):
        if expr1.type == ValueType.STRING or expr2.type == ValueType.STRING:
            raise OperationNotSupported("-", expr1, expr2)

        name = f"{expr1.name} - {expr2.name}"
        value = expr1.value - expr2.value
        return  Expression(value, name,ValueType.NUMBER)

    @staticmethod
    @typemultimethod(DISPATCH_ANY, DISPATCH_ANY)
    def minus(expr1: Expression, expr2: Expression):
        raise OperationNotSupported("-", expr1, expr2)

    @staticmethod
    def equals(expr1:Expression, expr2:Expression):
        name = f"{expr1.name} == {expr2.name}"
        value = expr1.value == expr2.value
        return  Expression(value, name,ValueType.BOOLEAN)

