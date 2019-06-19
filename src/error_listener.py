from antlr4.error.ErrorListener import ErrorListener
from .exceptions import  ConfProlSyntaxError
class MyErrorListener( ErrorListener ):


    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ConfProlSyntaxError(f"line {line}:{column} Syntax Error ({msg})")