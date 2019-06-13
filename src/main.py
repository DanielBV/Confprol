from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener

from generated_antlr4.confprolLexer import confprolLexer
from generated_antlr4.confprolParser import confprolParser
from src.visitor import MyVisitor
from src.exceptions import *
from src.error_listener import  MyErrorListener



def execute(input_stream):
    lexer = confprolLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = confprolParser(stream)
    parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
    parser.addErrorListener(MyErrorListener())
    tree = parser.program()

    state = {}
    visitor = MyVisitor(state)

    try:
        visitor.visit(tree)
    except ReturnException as e:
        return e.return_value

def execute_file(file_path:str):
    input_stream = FileStream(file_path)
    return execute(input_stream)



def main():

    try:
       return execute_file("../randomprogram.txt")
    except ArgumentsMissing as e:
        print(f"Line {e.line}: Missing arguments  {e.missing_arguments} in function {e.function}")
    except DuplicatedParameter as e:
        print(f"Line {e.line}: Method declaration '{e.function_name}' hycas duplicated parameters {e.duplicated_parameters}")
    except FunctionNotDefined as e:
        print(f"Line {e.line}: Method '{e.function}' isn't defined.")
    except VariableNotDefined as e:
        print(f"Line {e.line}: Variable'{e.variable_name}' isn't defined.")
    except TooManyArguments as e:
        print(f"Line {e.line}: Too many arguments  {e.extra_arguments} in function {e.function}")
    except ConfProlSyntaxError as e:
        print(e)



if __name__ == '__main__':
    main()
