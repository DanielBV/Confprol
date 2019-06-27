
from .confprol_exception import  ConfprolException

class AttributeNotDefined(ConfprolException):

    def __init__(self,object_name,type_,attribute_name):
        self.object_name = object_name
        self.attribute_name = attribute_name
        self.type = type_
        super(AttributeNotDefined, self).__init__("AttributeNotDefinedException")

    def get_message(self):
        return f"Object {self.object_name} of type {self.type} doesn't have an attribute {self.attribute_name}."

