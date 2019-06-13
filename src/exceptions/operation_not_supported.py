



class OperationNotSupported(Exception):

    def __init__(self,operation:str, expr1:'FinalExpression', expr2: 'FinalExpresion'):
        self.operation = operation
        self.expr1 = expr1
        self.expr2 = expr2