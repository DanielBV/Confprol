
from expressions.objects.confprol_object import ConfprolObject


class QuanticObject(ConfprolObject):


    def __init__(self, value, axis):
        self.axis = axis
        super(QuanticObject, self).__init__(value)