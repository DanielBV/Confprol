from expressions.objects.confprol_object import ConfprolObject
from type import ValueType
from . import BasicExpression,StringExpression
from exceptions import OperationNotSupported, DivisionByZero
from multimethods.multimethod import  typemultimethod

class TypeOperations:

    @staticmethod
    @typemultimethod((ValueType.NUMBER,ValueType.BOOLEAN),(ValueType.NUMBER,ValueType.BOOLEAN))
    def plus(expr1:BasicExpression, expr2:BasicExpression):
        name = f"{expr1.name} + {expr2.name}"
        value = expr1.value + expr2.value
        return BasicExpression(ConfprolObject(value), name, ValueType.NUMBER)

    @staticmethod
    @typemultimethod(ValueType.STRING,object)
    @typemultimethod(object, ValueType.STRING)
    def plus(expr1: BasicExpression, expr2: BasicExpression):
        name = f"{expr1.name} + {expr2.name}"
        value = str(expr1.value) + str(expr2.value)
        return  StringExpression(ConfprolObject(value),name)

    @staticmethod
    @typemultimethod(object, object)
    def plus(expr1: BasicExpression, expr2: BasicExpression):
        raise OperationNotSupported("+", expr1, expr2)



    @staticmethod
    @typemultimethod((ValueType.NUMBER,ValueType.BOOLEAN), (ValueType.NUMBER,ValueType.BOOLEAN))
    def mult(expr1:BasicExpression, expr2:BasicExpression):
        name = f"{expr1.name} * {expr2.name}"
        value = expr1.value * expr2.value
        return BasicExpression(ConfprolObject(value), name, ValueType.NUMBER)


    @staticmethod
    @typemultimethod(object,object)
    def mult(expr1:BasicExpression, expr2:BasicExpression):
        raise OperationNotSupported("*", expr1, expr2)

    @staticmethod
    @typemultimethod((ValueType.NUMBER, ValueType.BOOLEAN), (ValueType.NUMBER, ValueType.BOOLEAN))
    def div(expr1:BasicExpression, expr2:BasicExpression):
        name = f"{expr1.name} / {expr2.name}"

        if expr2.value == 0:
            raise DivisionByZero()
        value = expr1.value / expr2.value
        return  BasicExpression(ConfprolObject(value), name, ValueType.NUMBER)

    @staticmethod
    @typemultimethod(object, object)
    def div(expr1: BasicExpression, expr2: BasicExpression):
        raise OperationNotSupported("/", expr1, expr2)

    @staticmethod
    @typemultimethod((ValueType.NUMBER, ValueType.BOOLEAN), (ValueType.NUMBER, ValueType.BOOLEAN))
    def minus(expr1:BasicExpression, expr2:BasicExpression):
        name = f"{expr1.name} - {expr2.name}"
        value = expr1.value - expr2.value
        return  BasicExpression(ConfprolObject(value), name, ValueType.NUMBER)

    @staticmethod
    @typemultimethod(object, object)
    def minus(expr1: BasicExpression, expr2: BasicExpression):
        raise OperationNotSupported("-", expr1, expr2)

    @staticmethod
    def equals(expr1:BasicExpression, expr2:BasicExpression):
        name = f"{expr1.name} := {expr2.name}"
        value = expr1.value == expr2.value
        return  BasicExpression(ConfprolObject(value), name, ValueType.BOOLEAN)

