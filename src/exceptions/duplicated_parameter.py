from .confprol_exception import ConfprolException

class DuplicatedParameter(ConfprolException):

    def __init__(self, function_name, duplicated_parameters):
        self.function_name = function_name
        self.duplicated_parameters = duplicated_parameters

        super(DuplicatedParameter, self).__init__("DuplicatedParameterException")


    def get_message(self):
        return f"Duplicated parameter {self.duplicated_parameters} in function {self.function_name}"

