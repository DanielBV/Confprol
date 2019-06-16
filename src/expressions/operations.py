from ..type import ValueType
from . import Expression
from src.exceptions import OperationNotSupported
from multimethods.multimethod import  typemultimethod,DISPATCH_ANY

class TypeOperations:

    @staticmethod
    @typemultimethod(ValueType.NUMBER,ValueType.NUMBER)
    @typemultimethod(ValueType.BOOLEAN, ValueType.NUMBER)
    @typemultimethod(ValueType.NUMBER, ValueType.BOOLEAN)#TODO Add 'or/union' to typemultimethod
    def plus(expr1:Expression, expr2:Expression):
        name = f"{expr1.name} + {expr2.name}"
        value = expr1.value + expr2.value
        return Expression(value, name,ValueType.NUMBER)

    @staticmethod
    @typemultimethod(ValueType.STRING,ValueType.STRING)
    @typemultimethod(ValueType.NUMBER, ValueType.STRING)  #TODO add any except
    @typemultimethod(ValueType.BOOLEAN, ValueType.STRING) 
    @typemultimethod(ValueType.STRING, ValueType.NUMBER)
    @typemultimethod(ValueType.STRING, ValueType.BOOLEAN)
    def plus(expr1: Expression, expr2: Expression):
        value = str(expr1.value) + str(expr2.value)
        return  Expression(value, value,ValueType.STRING)

    @staticmethod
    @typemultimethod(DISPATCH_ANY, DISPATCH_ANY)
    def plus(expr1: Expression, expr2: Expression):
        raise OperationNotSupported("+", expr1, expr2)



    @staticmethod
    @typemultimethod(ValueType.NUMBER, ValueType.NUMBER)
    @typemultimethod(ValueType.BOOLEAN, ValueType.NUMBER)
    @typemultimethod(ValueType.NUMBER, ValueType.BOOLEAN)
    def mult(expr1:Expression, expr2:Expression):
        print("ASdsds")
        name = f"{expr1.name} * {expr2.name}"
        value = expr1.value * expr2.value
        return Expression(value, name,ValueType.NUMBER)


    @staticmethod
    @typemultimethod(DISPATCH_ANY,DISPATCH_ANY)
    def mult(expr1:Expression, expr2:Expression):
        print(expr1.type,expr2.type)
        raise OperationNotSupported("*", expr1, expr2)

    @staticmethod
    @typemultimethod(ValueType.NUMBER, ValueType.NUMBER)
    @typemultimethod(ValueType.BOOLEAN, ValueType.NUMBER)
    @typemultimethod(ValueType.NUMBER, ValueType.BOOLEAN)
    def div(expr1:Expression, expr2:Expression):
        name = f"{expr1.name} / {expr2.name}"
        value = expr1.value / expr2.value
        return  Expression(value, name,ValueType.NUMBER)

    @staticmethod
    @typemultimethod(DISPATCH_ANY, DISPATCH_ANY)
    def div(expr1: Expression, expr2: Expression):
        raise OperationNotSupported("/", expr1, expr2)

    @staticmethod
    @typemultimethod(ValueType.NUMBER, ValueType.NUMBER)
    @typemultimethod(ValueType.BOOLEAN, ValueType.NUMBER)
    @typemultimethod(ValueType.NUMBER, ValueType.BOOLEAN)
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
    @typemultimethod(DISPATCH_ANY,DISPATCH_ANY)
    def equals(expr1:Expression, expr2:Expression):
        name = f"{expr1.name} == {expr2.name}"
        value = expr1.value == expr2.value
        return  Expression(value, name,ValueType.BOOLEAN)

