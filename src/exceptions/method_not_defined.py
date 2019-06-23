
from .confprol_exception import  ConfprolException

class MethodNotDefined(ConfprolException):

    def __init__(self,object_name,method_name):
        self.object_name = object_name
        self.method_name = method_name
        super(MethodNotDefined, self).__init__("MethodNotDefinedException")

    def get_message(self):
        return f"Object {self.object_name} has no method {self.method_name}."

