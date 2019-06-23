
from .confprol_exception import ConfprolException

class DivisionByZero(ConfprolException):

    def __init__(self):
        super(DivisionByZero, self).__init__("DivisionByZeroException")

    def get_message(self):
        return "Division by 0"
