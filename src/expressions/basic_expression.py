
from src.type import ValueType
from src.expressions.objects.confprol_object import ConfprolObject
from .expression import Expression

class BasicExpression(Expression):



    def __init__(self, object:ConfprolObject, name, type_:ValueType):
        super(BasicExpression, self).__init__(object, name, type_)



    def get_deep_value(self):
        """
        Returns the value of the expression. If the expression contains subexpressions, it will replace the subexpressions
        with their correspondent'get_deep_value'
        :return:
        """

        return self.value

    def copy(self):
        """
        Copies the expression (not the object that it represents)
        Used to allow multiple alias for variables
        :return:
        """
        return BasicExpression(self.object, self.name, self.type)