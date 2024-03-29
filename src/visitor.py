

from generated_antlr4.confprolVisitor import confprolVisitor
from exceptions import ReturnException,AttributeNotDefined,FunctionNotDefined,\
     RuntimeException, ConfProlSyntaxError, ConfprolException
from expressions.runnable_expression import RunnableExpression
from expressions.callable.callable_function import CallableFunction

from confprol_handler import ConfprolHandler
from expressions.booleans.quantic_axis import QuanticAxis

from generated_antlr4.confprolParser import confprolParser

class MyVisitor(confprolVisitor):


    def visitNegatedExpr(self, ctx: confprolParser.NegatedExprContext):
        expr = self.visit(ctx.expr())

        return self.handler.negated_expr(expr,ctx.start.line)

    def visitWhile_not_loop(self, ctx: confprolParser.While_not_loopContext):
        try:
            value = super().visit(ctx.expr()).to_boolean()
        except ConfprolException as e:
            raise RuntimeException(ctx.start.line, e)

        while not value:
            statements = ctx.statement()
            for s in statements:
                super().visit(s)

            try:
                value = super().visit(ctx.expr()).to_boolean()
            except ConfprolException as e:
                raise RuntimeException(ctx.start.line, e)



    def visitBooleanMillionToOne(self, ctx:confprolParser.BooleanMillionToOneContext):
        return self.handler.load_boolean_million_to_one()

    def visitBooleanTrueFridays(self, ctx:confprolParser.BooleanTrueFridaysContext):
        return self.handler.load_boolean_true_except_fridays()

    def visitBooleanTrue(self, ctx: confprolParser.BooleanTrueContext):
        return self.handler.load_boolean(True)

    def visitBooleanFalse(self, ctx: confprolParser.BooleanFalseContext):
        return self.handler.load_boolean(False)

    def visitBooleanXTrue(self, ctx: confprolParser.BooleanXTrueContext):
        return self.handler.load_qubit(True,QuanticAxis.X)

    def visitBooleanXFalse(self, ctx: confprolParser.BooleanXFalseContext):
        return self.handler.load_qubit(False, QuanticAxis.X)

    def visitBooleanYTrue(self, ctx: confprolParser.BooleanYTrueContext):
        return self.handler.load_qubit(True, QuanticAxis.Y)

    def visitBooleanYFalse(self, ctx: confprolParser.BooleanYFalseContext):
        return self.handler.load_qubit(False, QuanticAxis.Y)

    def visitInOperationsSum(self, ctx: confprolParser.InOperationsSumContext):
        if ctx.ID():
            base = self.handler.get_attribute(ctx.ID().getText(),ctx.start.line)
        else:
            base = super(MyVisitor, self).visit(ctx.attributes())

        other = super(MyVisitor, self).visit(ctx.expr())
        self.handler.in_sum(base,other, ctx.start.line)

    def visitInOperationsMinus(self, ctx: confprolParser.InOperationsMinusContext):
        if ctx.ID():
            base = self.handler.get_attribute(ctx.ID().getText(), ctx.start.line)
        else:
            base = super(MyVisitor, self).visit(ctx.attributes())

        other = super(MyVisitor, self).visit(ctx.expr())
        self.handler.in_minus(base, other,ctx.start.line)


    def visitInOperationsMult(self, ctx: confprolParser.InOperationsMultContext):
        if ctx.ID():
            base = self.handler.get_attribute(ctx.ID().getText(), ctx.start.line)
        else:
            base = super(MyVisitor, self).visit(ctx.attributes())

        other = super(MyVisitor, self).visit(ctx.expr())
        self.handler.in_mult(base, other,ctx.start.line)

    def visitInOperationsDivision(self, ctx: confprolParser.InOperationsDivisionContext):
        if ctx.ID():
            base = self.handler.get_attribute(ctx.ID().getText(), ctx.start.line)
        else:
            base = super(MyVisitor, self).visit(ctx.attributes())

        other = super(MyVisitor, self).visit(ctx.expr())
        self.handler.in_div(base, other,ctx.start.line)



    def visitImport_(self, ctx: confprolParser.Import_Context):
        path = ctx.STRING().getText()
        path = path[1:len(path)-1]

        import_id = ctx.ID().getText()

        self.handler.import_path(path,import_id,ctx.start.line,self.base_path)

    def visitFinalNone(self, ctx: confprolParser.FinalNoneContext):
        return self.handler.load_none()

    def visitFinalNegativeNumber(self, ctx: confprolParser.FinalNegativeNumberContext):
        value = int(ctx.getText())
        return self.handler.load_number(value)

    def visitExprNE(self, ctx: confprolParser.ExprNEContext):
        return super().visitExprNE(ctx)

    def visitAttribute_assign(self, ctx: confprolParser.Attribute_assignContext):
        base_expr = self.visit(ctx.expr(0))
        value = self.visit(ctx.expr(1))

        if ctx.subattributes() is not None:
            ctx.subattributes().before = base_expr
            base_expr = super(MyVisitor, self).visit(ctx.subattributes())

        value = value.copy()
        attr_name = ctx.ID().getText()
        value.name = f"{base_expr.name}.{attr_name}"
        base_expr.set_attribute(attr_name,value)

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
            expr = ctx.before.get_attribute(name)
            expr = expr.copy()
            expr.name = f"{ctx.before.name}.{name}"
            return expr
        else:
            raise RuntimeException(ctx.start.line, AttributeNotDefined(ctx.before.name,ctx.before.type, name))



    def visitIntermediateIDs(self, ctx:confprolParser.IntermediateIDsContext):
        ctx.subattributes(0).before = ctx.before
        before = super(MyVisitor, self).visit(ctx.subattributes(0))

        ctx.subattributes(1).before = before
        return super(MyVisitor, self).visit(ctx.subattributes(1))





    def visitMethodCall(self, ctx:confprolParser.MethodCallContext):
        name = ctx.ID().getText()
        if ctx.before.has_attribute(name):
            expression = ctx.before.get_attribute(name)
        else:

            raise RuntimeException(ctx.start.line, AttributeNotDefined(ctx.before.name,ctx.before.type, name))


        arg_node = ctx.arguments()
        if arg_node is None:
            arguments = []
        else:
            arguments = self.visitArguments(arg_node)


        try:
            expr =  self.handler.run_function(expression, arguments, ctx.start.line)
            expr = expr.copy()
            arguments_name = list(map(lambda a:a.name,arguments))
            expr.name = f"{expression.name}(" + ",".join(arguments_name) + ")"
            return expr
        except ConfprolException as e:
            raise RuntimeException(ctx.start.line,e)


    def visitFinalFloat(self, ctx: confprolParser.FinalFloatContext):
        value = float(ctx.FLOAT().getText())
        return self.handler.load_float(value)


    def visitReturn_value(self, ctx: confprolParser.Return_valueContext):
        value =  super().visit(ctx.expr())
        raise ReturnException(value)

    def visitExprEqual(self, ctx: confprolParser.ExprEqualContext):
        value1 = self.visit(ctx.expr(0))
        value2 = self.visit(ctx.expr(1))
        try:
            return self.handler.equal(value1,value2)
        except ConfprolException as e:
            raise RuntimeException(ctx.start.line, e)


    def __init__(self,handler:ConfprolHandler,file_path):
        self.handler = handler
        self.base_path = file_path

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

        if self.handler.has_attribute(function):
            try:
                function = self.handler.get_attribute(function,ctx.start.line)
                return self.handler.run_function(function, arguments, ctx.start.line)
            except ConfprolException as e:
                raise RuntimeException(ctx.start.line, e)
        else:
            raise RuntimeException(ctx.start.line,FunctionNotDefined(function))


    def visitFunction_declaration(self, ctx: confprolParser.Function_declarationContext):
        name = ctx.ID().getText()
        params_ctx = ctx.parameters()
        if params_ctx is not None:
            params = self.visitParameters(ctx.parameters())
            duplicated_params = set([x for x in params if params.count(x) > 1])

            if len(duplicated_params) != 0:
                raise ConfProlSyntaxError(f"Duplicated parameter {duplicated_params} in function {name}.",ctx.start.line,ctx.start.column)
        else:
            params = []

        expression = RunnableExpression(CallableFunction(params,ctx.statement(),self),name)
        self.handler.assign_variable(name,expression)


    def visitFinalSTRING(self, ctx: confprolParser.FinalSTRINGContext):
        return self.handler.load_string(ctx.getText())


    def visitExprMINUS(self, ctx: confprolParser.ExprMINUSContext):
        expr1 = super().visit(ctx.expr2())
        expr2 = super().visit(ctx.term())

        return self.handler.minus(expr1,expr2,ctx.start.line)

    def visitExprSUM(self, ctx: confprolParser.ExprSUMContext):
        expr1 = super().visit(ctx.expr2())
        expr2 = super().visit(ctx.term())

        return self.handler.sum(expr1,expr2,ctx.start.line)

    def visitExprTERM(self, ctx: confprolParser.ExprTERMContext):
        return self.visit(ctx.term())

    def visitTermDIV(self, ctx: confprolParser.TermDIVContext):
        expr1 = super().visit(ctx.term())
        expr2 = super().visit(ctx.final())

        return self.handler.division(expr1, expr2,ctx.start.line)

    def visitTermFINAL(self, ctx: confprolParser.TermFINALContext):
        value = super().visit(ctx.final())
        return value

    def visitTermMULT(self, ctx: confprolParser.TermMULTContext):
        expr1 = super().visit(ctx.term())
        expr2 = super().visit(ctx.final())

        return self.handler.multiplication(expr1,expr2, ctx.start.line)

    def visitFinalPAR(self, ctx: confprolParser.FinalPARContext):
        value = super().visit(ctx.expr())

        return value

    def visitFinalNUMBER(self, ctx: confprolParser.FinalNUMBERContext):
        value =  int(ctx.NUMBER().getText())

        return self.handler.load_number(value)

    def visitCondition(self, ctx:confprolParser.ConditionContext):
        try:
            value = super().visit(ctx.expr()).to_boolean()
        except ConfprolException as e:
            raise RuntimeException(ctx.start.line, e)

        if not value:
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



    def visitPrint_(self, ctx: confprolParser.Print_Context):
        value = self.visit(ctx.expr())

        self.handler.print_expression(value)

    def get_context(self):
        return self.handler.context

    def set_context(self,context):
        self.handler.set_context(context)
