from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener

from generated_antlr4.confprolLexer import confprolLexer
from generated_antlr4.confprolParser import confprolParser
from visitor import MyVisitor
from exceptions import *
from error_listener import  MyErrorListener
import sys
import os
from confprol_handler import ConfprolHandler
from utilities.constants import ENCODING
from default_functions import default_functions


def execute(input_stream,raise_exception=False,base_path="."):
    lexer = confprolLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = confprolParser(stream)
    parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
    parser.addErrorListener(MyErrorListener())


    try:
        tree = parser.program()

        visitor = MyVisitor(ConfprolHandler(),base_path)
        visitor.get_context().set_variables(default_functions) #TODO refactor
        visitor.visit(tree)
    except ReturnException as e:
        return e.return_value.get_exit_value()
    except (RuntimeException,ConfProlSyntaxError) as e:
        if raise_exception:
            raise e
        else:
            print(e.get_message())


def execute_file(file_path:str,raise_exception=False):
    base_path = os.path.dirname(os.path.realpath(file_path))
    input_stream = FileStream(file_path,ENCODING)
    return execute(input_stream,raise_exception,base_path)



def main():

    if len(sys.argv)!=2:
        script_name = os.path.basename(__file__)
        print(f"Usage: python {script_name} <file_path>")
        exit(-1)

    try:
        return execute_file(sys.argv[1],False)
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")


if __name__ == '__main__':
    main()
