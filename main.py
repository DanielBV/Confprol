import sys
from generated_antlr4 import *
from antlr4 import *
from generated_antlr4.confprolLexer import confprolLexer
from generated_antlr4.confprolParser import confprolParser
from visitor import MyVisitor
from exceptions import *




def main():
    input_stream = FileStream("randomprogram.txt")
    lexer = confprolLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = confprolParser(stream)
    tree = parser.program()

    state = {}
    visitor = MyVisitor(state)
    try:
        result = visitor.visit(tree)
    except ArgumentsMissing as e:
        print(f"Line {e.line}: Missing arguments  {e.missing_arguments} in function {e.function}")
    except ReturnException as e:
        exit(e.return_value)
    except DuplicatedParameter as e:
        print(f"Line {e.line}: Method declaration '{e.function_name}' hycas duplicated parameters {e.duplicated_parameters}")
    except FunctionNotDefined as e:
        print(f"Line {e.line}: Method '{e.function}' isn't defined.")
    except VariableNotDefined as e:
        print(f"Line {e.line}: Variable'{e.variable_name}' isn't defined.")
    except TooManyArguments as e:
        print(f"Line {e.line}: Too many arguments  {e.extra_arguments} in function {e.function}")




if __name__ == '__main__':
    main()
