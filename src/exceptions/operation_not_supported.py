
from .confprol_exception import ConfprolException


class OperationNotSupported(ConfprolException):

    def __init__(self,operation:str, expr1:'FinalExpression', expr2: 'FinalExpresion'):
        self.operation = operation
        self.expr1 = expr1
        self.expr2 = expr2
        
        super(OperationNotSupported, self).__init__("OperationNotSupportedException")

    def get_message(self):
        return f"Operation {self.operation} can't be applied to {self.expr1.type} and {self.expr2.type}"
        