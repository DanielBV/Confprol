import sys
from generated_antlr4 import *
from antlr4 import *
from generated_antlr4.confprolLexer import confprolLexer
from generated_antlr4.confprolParser import confprolParser
from visitor import MyVisitor





def main():
    input_stream = FileStream("randomprogram.txt")
    lexer = confprolLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = confprolParser(stream)
    tree = parser.program()

    state = {}
    visitor = MyVisitor(state)
    result = visitor.visit(tree)
    #TODO Add return exception try catch

    print(state)

if __name__ == '__main__':
    main()
