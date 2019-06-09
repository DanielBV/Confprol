import sys
from generated_antlr4 import *
from antlr4 import *
from generated_antlr4.confprolLexer import confprolLexer
from generated_antlr4.confprolParser import confprolParser
from generated_antlr4.confprolVisitor import confprolVisitor

state = {}


class MyVisitor(confprolVisitor):


    def visitFinalSTRING(self, ctx: confprolParser.FinalSTRINGContext):
        text = ctx.STRING().getText()
        text = text[1:len(text)-1]
        return text

    def visitExprMINUS(self, ctx: confprolParser.ExprMINUSContext):
        value = super().visit(ctx.expr())
        return value - super().visit(ctx.term())


    def visitExprSUM(self, ctx: confprolParser.ExprSUMContext):
        value = super().visit(ctx.expr())
        return value + super().visit(ctx.term())

    def visitExprTERM(self, ctx: confprolParser.ExprTERMContext):
        return self.visit(ctx.term())

    def visitTermDIV(self, ctx: confprolParser.TermDIVContext):
        value = super().visit(ctx.term())
        return value / super().visit(ctx.final())

    def visitTermFINAL(self, ctx: confprolParser.TermFINALContext):
        value = super().visit(ctx.final())
        return value

    def visitTermMULT(self, ctx: confprolParser.TermMULTContext):
        value = super().visit(ctx.term())
        return value * super().visit(ctx.final())

    def visitFinalPAR(self, ctx: confprolParser.FinalPARContext):
        value = super().visit(ctx.expr())

        return value

    def visitFinalNUMBER(self, ctx: confprolParser.FinalNUMBERContext):
        return int(ctx.NUMBER().getText())

    def visitFinalID(self, ctx: confprolParser.FinalIDContext):
        return state[ctx.getText()]

    def visitCondition(self, ctx:confprolParser.ConditionContext):
        value = super().visit(ctx.expr())
        if value:
            statements = ctx.statement()
            for s in statements:
                super().visit(s)
        else:
            return super().visitElsecondition(ctx.elsecondition())

    def visitProgram(self, ctx: confprolParser.ProgramContext):
        return super().visitProgram(ctx)

    def visitStatement(self, ctx: confprolParser.StatementContext):
        return super().visitStatement(ctx)

    def visitAssign(self, ctx: confprolParser.AssignContext):

        variable = ctx.ID().getText()
        state[variable] =  super().visit(ctx.expr())


        return super().visitAssign(ctx)

    def visitPrint(self, ctx: confprolParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)


def main():
    input_stream = FileStream("randomprogram.txt")
    lexer = confprolLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = confprolParser(stream)
    tree = parser.program()

    visitor = MyVisitor()
    result = visitor.visit(tree)

    print(state)


if __name__ == '__main__':
    main()
