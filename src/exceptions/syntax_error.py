
from .confprol_exception import ConfprolException

class ConfProlSyntaxError(ConfprolException):

    def __init__(self,message,line, column):
        self.message = message
        self.line = line
        self.column = column

        super(ConfProlSyntaxError, self).__init__("SyntaxException")

    def get_message(self):
        return f"{self.name} in line {self.line}:{self.column} {self.message}"