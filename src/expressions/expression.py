
from type import ValueType
from expressions.objects.confprol_object import ConfprolObject

class Expression:
    """
    Expressions are encapsulations of ConfprolObjects. They are used in order to:
        - Allow multiple alias for the same object.
        - Interpret the object's value depending on its type.
            -  For example, the value of a ConfprolObject can be a String, boolean, integer, float, etc. But the
            expression defines how to print it (__str__)
        - In some expressions, like QuanticExpression, the expression hides the object from the outside, so
        when you try to evaluate a quantic boolean without using evalX or evalY, an exception is raised.
    """


    def __init__(self, value:ConfprolObject, name,type_:ValueType):
        self.object = value
        self.name  = name
        self.__type = type_


    @property
    def value(self):
        return self.object.value

    @property
    def type(self):
        return self.__type

    def __str__(self):
        return str(self.value)

    def get_attribute(self,attribute):
        return self.object.get_attribute(attribute)

    def set_attribute(self, name, value: 'BasicExpression'):
        self.object.set_attribute(name,value)

    def set_attributes(self, attr):
        self.object.set_attributes(attr)

    def has_attribute(self, attribute):
        return self.object.has_attribute(attribute)

    def get_deep_value(self):
        """
        Returns the value of the expression. If the expression contains subexpressions, it will replace the subexpressions
        with their correspondent'get_deep_value'
        :return:
        """

        raise NotImplementedError("get_deep_value not implemented")

    def __repr__(self):
        return self.__str__()

    def copy(self):
        raise NotImplementedError("copy not implemented")

    def to_boolean(self):
        return bool(self.value)


    def get_exit_value(self):
        """
        Value that is returned by the python program when you return outside a function.
            - Required to avoid conflicts with objects that don't have a Python equivalent, like QuanticBoolean
        :return:
        """
        return self.get_deep_value()