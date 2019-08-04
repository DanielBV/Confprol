# Generated from confprol.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .confprolParser import confprolParser
else:
    from confprolParser import confprolParser

# This class defines a complete generic visitor for a parse tree produced by confprolParser.

class confprolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by confprolParser#program.
    def visitProgram(self, ctx:confprolParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#statement.
    def visitStatement(self, ctx:confprolParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#import_.
    def visitImport_(self, ctx:confprolParser.Import_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#while_not_loop.
    def visitWhile_not_loop(self, ctx:confprolParser.While_not_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#assign.
    def visitAssign(self, ctx:confprolParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#attribute_assign.
    def visitAttribute_assign(self, ctx:confprolParser.Attribute_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#print_.
    def visitPrint_(self, ctx:confprolParser.Print_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#condition.
    def visitCondition(self, ctx:confprolParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#elsecondition.
    def visitElsecondition(self, ctx:confprolParser.ElseconditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#return_value.
    def visitReturn_value(self, ctx:confprolParser.Return_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#inOperationsSum.
    def visitInOperationsSum(self, ctx:confprolParser.InOperationsSumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#inOperationsMinus.
    def visitInOperationsMinus(self, ctx:confprolParser.InOperationsMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#inOperationsMult.
    def visitInOperationsMult(self, ctx:confprolParser.InOperationsMultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#inOperationsDivision.
    def visitInOperationsDivision(self, ctx:confprolParser.InOperationsDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#negatedExpr.
    def visitNegatedExpr(self, ctx:confprolParser.NegatedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#exprNE.
    def visitExprNE(self, ctx:confprolParser.ExprNEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#exprEqual.
    def visitExprEqual(self, ctx:confprolParser.ExprEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#exprMINUS.
    def visitExprMINUS(self, ctx:confprolParser.ExprMINUSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#exprSUM.
    def visitExprSUM(self, ctx:confprolParser.ExprSUMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#exprTERM.
    def visitExprTERM(self, ctx:confprolParser.ExprTERMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#termDIV.
    def visitTermDIV(self, ctx:confprolParser.TermDIVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#termFINAL.
    def visitTermFINAL(self, ctx:confprolParser.TermFINALContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#termMULT.
    def visitTermMULT(self, ctx:confprolParser.TermMULTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalPAR.
    def visitFinalPAR(self, ctx:confprolParser.FinalPARContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalNUMBER.
    def visitFinalNUMBER(self, ctx:confprolParser.FinalNUMBERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalNone.
    def visitFinalNone(self, ctx:confprolParser.FinalNoneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalID.
    def visitFinalID(self, ctx:confprolParser.FinalIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalIDS.
    def visitFinalIDS(self, ctx:confprolParser.FinalIDSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalSTRING.
    def visitFinalSTRING(self, ctx:confprolParser.FinalSTRINGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalFunctionCall.
    def visitFinalFunctionCall(self, ctx:confprolParser.FinalFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalBoolean.
    def visitFinalBoolean(self, ctx:confprolParser.FinalBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalFloat.
    def visitFinalFloat(self, ctx:confprolParser.FinalFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalListCreation.
    def visitFinalListCreation(self, ctx:confprolParser.FinalListCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#finalNegativeNumber.
    def visitFinalNegativeNumber(self, ctx:confprolParser.FinalNegativeNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#attributeBeginning.
    def visitAttributeBeginning(self, ctx:confprolParser.AttributeBeginningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#intermediateIDs.
    def visitIntermediateIDs(self, ctx:confprolParser.IntermediateIDsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#attribute.
    def visitAttribute(self, ctx:confprolParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#methodCall.
    def visitMethodCall(self, ctx:confprolParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#list_creation.
    def visitList_creation(self, ctx:confprolParser.List_creationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#functionCall.
    def visitFunctionCall(self, ctx:confprolParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#arguments.
    def visitArguments(self, ctx:confprolParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#booleanTrue.
    def visitBooleanTrue(self, ctx:confprolParser.BooleanTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#booleanFalse.
    def visitBooleanFalse(self, ctx:confprolParser.BooleanFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#booleanXTrue.
    def visitBooleanXTrue(self, ctx:confprolParser.BooleanXTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#booleanXFalse.
    def visitBooleanXFalse(self, ctx:confprolParser.BooleanXFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#booleanYTrue.
    def visitBooleanYTrue(self, ctx:confprolParser.BooleanYTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#booleanYFalse.
    def visitBooleanYFalse(self, ctx:confprolParser.BooleanYFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#booleanTrueFridays.
    def visitBooleanTrueFridays(self, ctx:confprolParser.BooleanTrueFridaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#booleanMillionToOne.
    def visitBooleanMillionToOne(self, ctx:confprolParser.BooleanMillionToOneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#function_declaration.
    def visitFunction_declaration(self, ctx:confprolParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by confprolParser#parameters.
    def visitParameters(self, ctx:confprolParser.ParametersContext):
        return self.visitChildren(ctx)



del confprolParser