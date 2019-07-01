from src.expressions.confprol_object import ConfprolObject
from src.type import ValueType
from .expression import Expression



class ObjectExpression(Expression):
    """
    Expression that represents an object
    """

    def __init__(self,name):
        
        super(ObjectExpression, self).__init__(ConfprolObject(object()),name,ValueType.OBJECT)


    def copy(self):
        expr = ObjectExpression(self.name)
        expr.object = self.object
        return expr

    def get_deep_value(self):
        return self.value

    def __str__(self):
        return f"[Object {id(self.value)}]"