
from generated_antlr4.confprolVisitor import confprolVisitor
from function import Function
from generated_antlr4.confprolParser import confprolParser
from exceptions import ReturnException, DuplicatedParameter,FunctionNotDefined, VariableNotDefined, ArgumentsMissing, TooManyArguments
from context import Context



class MyVisitor(confprolVisitor):


    def visitReturn_value(self, ctx: confprolParser.Return_valueContext):
        value =  super().visit(ctx.expr())
        raise ReturnException(value)

    def __init__(self, context):
        self.context = Context()


    def visitArguments(self, ctx: confprolParser.ArgumentsContext):
        args = ctx.arguments()

        if args is None:
            return [self.visit(ctx.expr())]
        else:
            other_args = self.visitArguments(args)
            other_args.insert(0,self.visit(ctx.expr()))
            return other_args

    def visitParameters(self, ctx:confprolParser.ParametersContext):
       args = ctx.parameters() #TODO handle no parameters

       if args is None:
           return [ctx.ID().getText()]
       else:
           other_args = self.visitParameters(args)
           other_args.insert(0,ctx.ID().getText())
           return other_args

    def visitMethodCall(self, ctx: confprolParser.MethodCallContext):
        function = ctx.ID().getText()

        arg_node = ctx.arguments()
        if arg_node is None:
            arguments = []
        else:
            arguments = self.visitArguments(arg_node)

        if self.context.has_function(function): #TODO Refactor

            function =  self.context.get_function(function)
            parameters = function.get_parameters()
            if len(arguments) < len(parameters):
                missing_arguments = parameters[len(arguments):]
                raise ArgumentsMissing("Argument number mismatch", ctx.start.line, function.get_name(), missing_arguments)
            if len(arguments) > len(parameters):
                extra_arguments = ctx.arguments().getText().split(',')[len(parameters):]   #TODO Refactor expr to objects

                raise TooManyArguments("Too many arguments", ctx.start.line, function.get_name(),extra_arguments)

        else:
            raise FunctionNotDefined(function,ctx.start.line)

        return_value = function.run(arguments)

        return return_value


    def visitFinalMethodCall(self, ctx: confprolParser.FinalMethodCallContext):
        return super().visitFinalMethodCall(ctx)

    def visitFunction_declaration(self, ctx: confprolParser.Function_declarationContext):
        name = ctx.ID().getText()
        args = self.visitParameters(ctx.parameters())
        duplicated_args = set([x for x in args if args.count(x) > 1])

        if len(duplicated_args) == 0:
            self.context.add_function(name,Function(args,ctx.statement(),name,self))
        else:
             raise DuplicatedParameter(name,duplicated_args,ctx.start.line)

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
        name = ctx.getText()
        if self.context.has_variable(name):
            return self.context.get_variable(ctx.getText())
        else:
            raise VariableNotDefined(name, ctx.start.line)

    def visitCondition(self, ctx:confprolParser.ConditionContext):
        value = super().visit(ctx.expr())
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
        self.context.set_variable(variable,super().visit(ctx.expr()))


        return super().visitAssign(ctx)

    def visitPrint(self, ctx: confprolParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)
