from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener

from generated_antlr4.confprolLexer import confprolLexer
from generated_antlr4.confprolParser import confprolParser
from src.visitor import MyVisitor
from src.exceptions import *
from src.error_listener import  MyErrorListener
import sys
import os
from src.confprol_handler import ConfprolHandler


def execute(input_stream,raise_exception=False):
    lexer = confprolLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = confprolParser(stream)
    parser.removeErrorListener(ConsoleErrorListener.INSTANCE)
    parser.addErrorListener(MyErrorListener())


    try:
        tree = parser.program()
        visitor = MyVisitor(ConfprolHandler())
        visitor.visit(tree)
    except ReturnException as e:
        return e.return_value.get_deep_value()
    except (RuntimeException,ConfProlSyntaxError) as e:
        if raise_exception:
            raise e
        else:
            print(e.get_message())


def execute_file(file_path:str,raise_exception=False):
    input_stream = FileStream(file_path,"utf-8")
    return execute(input_stream,raise_exception)



def main():

    if len(sys.argv)!=2:
        script_name = os.path.basename(__file__)
        print(f"Usage: python {script_name} <file_path>")
        exit(-1)

    return execute_file(sys.argv[1],False)



if __name__ == '__main__':
    main()
