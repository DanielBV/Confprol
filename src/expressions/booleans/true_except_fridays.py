from src.expressions.basic_expression import BasicExpression
from src.type import ValueType
from src.expressions.objects.confprol_object import ConfprolObject
from datetime import  datetime

class TrueExceptFridays(BasicExpression):

    def __init__(self,object=None):
        if object is None:
            object = ConfprolObject(None)
        super(TrueExceptFridays, self).__init__(object, "TrueExceptFridays", ValueType.BOOLEAN)

    def get_deep_value(self):
        return self.value

    @property
    def value(self):
       return self.to_boolean()

    def copy(self):
        return TrueExceptFridays(self.object)

    def __str__(self):
        return f"[TrueExceptFridays]"

    def to_boolean(self):

        return self.get_todays_weekday() != 5

    def get_todays_weekday(self):
        return datetime.today().isoweekday()