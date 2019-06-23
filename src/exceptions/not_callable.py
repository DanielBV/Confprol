from .confprol_exception import  ConfprolException


class NotCallable(ConfprolException):
    

    def __init__(self, variable_name):
        self.not_callable_name = variable_name
        super(NotCallable, self).__init__("NotCallableException")

    def get_message(self):
        return f"The variable {self.not_callable_name} is not callable."