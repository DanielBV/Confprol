

from generated_antlr4.confprolVisitor import confprolVisitor
from src.expressions.callable.callable import Callable
from generated_antlr4.confprolParser import confprolParser
from src.exceptions import ReturnException, NotCallable,MethodNotDefined,FunctionNotDefined,\
    VariableNotDefined, DivisionByZero, RuntimeException, ConfProlSyntaxError, ConfprolException, OperationNotSupported

from src.expressions import CallableFunction
from .expressions.operations import TypeOperations
from .confprol_handler import ConfprolHandler


class MyVisitor(confprolVisitor):





    def visitList_creation(self, ctx: confprolParser.List_creationContext):
        arg_node = ctx.arguments()
        if arg_node is None:
            values = []
        else:
            values = self.visitArguments(arg_node)

        return self.handler.load_list(values)


    def visitFinalID(self, ctx: confprolParser.FinalIDContext):
        name = ctx.getText()
        return self.handler.get_attribute(name,ctx.start.line)

    def visitAttributeBeginning(self, ctx: confprolParser.AttributeBeginningContext):
        if ctx.STRING() is not None:
            expr = self.handler.load_string(ctx.STRING().getText())
        else:
            expr = self.handler.get_attribute(ctx.ID().getText(),ctx.start.line)


        ctx.subattributes().before = expr
        return super().visitAttributeBeginning(ctx)


    def visitAttribute(self, ctx:confprolParser.AttributeContext):
        name = ctx.ID().getText()

        if ctx.before.has_attribute(name):
            return ctx.before.get_attribute(name)
        else:
            raise VariableNotDefined(name, ctx.start.line) #TODO differenciate between attribute not defined and variable not defined



    def visitIntermediateIDs(self, ctx:confprolParser.IntermediateIDsContext):
        ctx.subattributes(0).before = ctx.before
        before = super(MyVisitor, self).visit(ctx.subattributes(0))
        ctx.subattributes(1).before = before
        return super(MyVisitor, self).visit(ctx.subattributes(1))





    def visitCall(self, ctx:confprolParser.CallContext):
        name = ctx.ID().getText()
        if ctx.before.has_attribute(name):
            expression = ctx.before.get_attribute(name)
        else:
            raise RuntimeException(ctx.start.line,MethodNotDefined(ctx.before.name,name))

        if not isinstance(expression,Callable):
            raise NotCallable()

        arg_node = ctx.arguments()
        if arg_node is None:
            arguments = []
        else:
            arguments = self.visitArguments(arg_node)


        try:
            return self.handler.runFunction(expression,arguments,ctx.start.line)
        except ConfprolException as e:
            raise RuntimeException(ctx.start.line,e)

    def visitFinalFloat(self, ctx: confprolParser.FinalFloatContext):
        value = float(ctx.FLOAT().getText())
        return self.handler.load_float(value)

    def visitFinalBoolean(self, ctx: confprolParser.FinalBooleanContext):
        value = 'True' == ctx.getText()
        return self.handler.load_boolean(value)


    def visitReturn_value(self, ctx: confprolParser.Return_valueContext):
        value =  super().visit(ctx.expr())
        raise ReturnException(value)

    def visitExprEqual(self, ctx: confprolParser.ExprEqualContext):
        value1 = self.visit(ctx.expr2(0))
        value2 = self.visit(ctx.expr2(1))
        return  TypeOperations.equals(value1,value2)

    def __init__(self,handler:ConfprolHandler):
        self.handler = handler

    def visitArguments(self, ctx: confprolParser.ArgumentsContext):
        args = ctx.arguments()

        if args is None:
            return [self.visit(ctx.expr())]
        else:
            other_args = self.visitArguments(args)
            other_args.insert(0,self.visit(ctx.expr()))
            return other_args

    def visitParameters(self, ctx:confprolParser.ParametersContext):
       args = ctx.parameters()

       if args is None:
           return [ctx.ID().getText()]
       else:
           other_args = self.visitParameters(args)
           other_args.insert(0,ctx.ID().getText())
           return other_args


    def visitFunctionCall(self, ctx: confprolParser.FunctionCallContext):
        function = ctx.ID().getText()

        arg_node = ctx.arguments()
        if arg_node is None:
            arguments = []
        else:
            arguments = self.visitArguments(arg_node)

        if self.handler.has_attribute(function): #TODO refactor
            function = self.handler.get_attribute(function,ctx.start.line)
            return self.handler.runFunction(function,arguments,ctx.start.line)
        else:
            raise RuntimeException(ctx.start.line,FunctionNotDefined(function))


    def visitFunction_declaration(self, ctx: confprolParser.Function_declarationContext):
        name = ctx.ID().getText()
        params_ctx = ctx.parameters()
        if params_ctx is not None:
            params = self.visitParameters(ctx.parameters())
            duplicated_params = set([x for x in params if params.count(x) > 1])

            if len(duplicated_params) != 0:
                raise ConfProlSyntaxError(f"Duplicated parameter {duplicated_params} in function {name}",ctx.start.line,ctx.start.column) #TODO refactor
        else:
            params = []

        expression = CallableFunction(params,ctx.statement(),name,self)
        self.handler.assign_variable(name,expression)


    def visitFinalSTRING(self, ctx: confprolParser.FinalSTRINGContext):
        return self.handler.load_string(ctx.getText())


    def visitExprMINUS(self, ctx: confprolParser.ExprMINUSContext):
        value = super().visit(ctx.expr2())
        try:
            return  TypeOperations.minus(value,super().visit(ctx.term()))
        except OperationNotSupported as e:
            raise RuntimeException(ctx.start.line, e)

    def visitExprSUM(self, ctx: confprolParser.ExprSUMContext):
        value = super().visit(ctx.expr2())
        try:
            return TypeOperations.plus(value,super().visit(ctx.term()))
        except OperationNotSupported as e:
            raise RuntimeException(ctx.start.line, e)

    def visitExprTERM(self, ctx: confprolParser.ExprTERMContext):
        return self.visit(ctx.term())

    def visitTermDIV(self, ctx: confprolParser.TermDIVContext):
        value = super().visit(ctx.term())
        #TODO Keep moving methods to handler
        try:
            return TypeOperations.div(value,super().visit(ctx.final()))
        except (DivisionByZero,OperationNotSupported) as e:
            raise RuntimeException(ctx.start.line,e)


    def visitTermFINAL(self, ctx: confprolParser.TermFINALContext):
        value = super().visit(ctx.final())
        return value

    def visitTermMULT(self, ctx: confprolParser.TermMULTContext):
        value = super().visit(ctx.term())
        #TODO Move operations to handler
        try:
            return  TypeOperations.mult(value,super().visit(ctx.final()))
        except OperationNotSupported as e:
            raise RuntimeException(ctx.start.line, e)

    def visitFinalPAR(self, ctx: confprolParser.FinalPARContext):
        value = super().visit(ctx.expr())

        return value

    def visitFinalNUMBER(self, ctx: confprolParser.FinalNUMBERContext):
        value =  int(ctx.NUMBER().getText())

        return self.handler.load_number(value)

    def visitCondition(self, ctx:confprolParser.ConditionContext):
        value = super().visit(ctx.expr()).value
        if value:
            statements = ctx.statement()
            for s in statements:
                super().visit(s)
        else:
            if ctx.elsecondition() is not None:
                return super().visitElsecondition(ctx.elsecondition())

    def visitProgram(self, ctx: confprolParser.ProgramContext):
        return super().visitProgram(ctx)

    def visitStatement(self, ctx: confprolParser.StatementContext):
        return super().visitStatement(ctx)

    def visitAssign(self, ctx: confprolParser.AssignContext):

        variable = ctx.ID().getText()
        value =  super().visit(ctx.expr())

        self.handler.assign_variable(variable,value)

        return super().visitAssign(ctx)

    def visitPrint(self, ctx: confprolParser.PrintContext):
        value = self.visit(ctx.expr())

        self.handler.print_expression(value)

    def get_context(self):
        return self.handler.context

    def set_context(self,context):
        self.handler.set_context(context)
