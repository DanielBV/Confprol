

from generated_antlr4.confprolVisitor import confprolVisitor
from src.callable import Callable
from generated_antlr4.confprolParser import confprolParser
from src.exceptions import ReturnException, NotCallable,DuplicatedParameter,FunctionNotDefined, VariableNotDefined, ArgumentsMissing, TooManyArguments
from src.context import Context
from src.expressions import Expression,Function
from src.type import ValueType
from .expressions.operations import TypeOperations


class MyVisitor(confprolVisitor):


    def visitFinalIDS(self, ctx: confprolParser.FinalIDSContext):
        self.temp_context = self.context
        super().visitFinalIDS(ctx)
        return self.temp_context

    def visitAttribute(self, ctx:confprolParser.AttributeContext):
        name = ctx.ID().getText()
        if self.temp_context.has_attribute(name):
            self.temp_context = self.temp_context.get_attribute(name)
        else:
            raise VariableNotDefined(name, ctx.start.line)

        return super(MyVisitor, self).visitAttribute(ctx)

    def visitIntermediateIDs(self, ctx:confprolParser.IntermediateIDsContext):
        name = ctx.ID().getText()
        if self.temp_context.has_attribute(name):
            self.temp_context = self.temp_context.get_attribute(name)
        else:
            raise VariableNotDefined(name, ctx.start.line)
        #TODO refactor
        return super().visitIntermediateIDs(ctx)

    def visitCall(self, ctx:confprolParser.CallContext):
        name = ctx.ID().getText()
        if self.temp_context.has_attribute(name):
            self.temp_context = self.temp_context.get_attribute(name)
        else:
            raise VariableNotDefined(name, ctx.start.line)

        try:
            function =  self.temp_context.get_attribute("CALL")
        except ValueError:
            raise NotCallable()

        arg_node = ctx.arguments()
        if arg_node is None:
            arguments = []
        else:
            arguments = self.visitArguments(arg_node)

        parameters = function.get_parameters()
        if len(arguments) < len(parameters):
            missing_arguments = parameters[len(arguments):]
            raise ArgumentsMissing("Argument number mismatch", ctx.start.line, function.get_name(), missing_arguments)
        if len(arguments) > len(parameters):
            extra_arguments = list(map(lambda arg: arg.name, arguments))

            raise TooManyArguments("Too many arguments", ctx.start.line, function.get_name(), extra_arguments)

        self.temp_context = function.run(arguments)
        return 3

    def visitFinalFloat(self, ctx: confprolParser.FinalFloatContext):
        value = float(ctx.FLOAT().getText())
        return Expression(value, value, ValueType.BOOLEAN)

    def visitFinalBoolean(self, ctx: confprolParser.FinalBooleanContext):
        value = 'True' == ctx.getText()
        return Expression(value,value,ValueType.BOOLEAN)


    def visitReturn_value(self, ctx: confprolParser.Return_valueContext):
        value =  super().visit(ctx.expr())
        raise ReturnException(value)

    def visitExprEqual(self, ctx: confprolParser.ExprEqualContext):
        value1 = self.visit(ctx.expr2(0))
        value2 = self.visit(ctx.expr2(1))
        return  TypeOperations.equals(value1,value2)

    def __init__(self, context):
        self.context = Context()
        self.temp_context = None


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



    def visitFinalFunctionCall(self, ctx: confprolParser.FinalFunctionCallContext):
        return super().visitFinalFunctionCall(ctx)

    def visitFunction_declaration(self, ctx: confprolParser.Function_declarationContext):
        name = ctx.ID().getText()
        params_ctx = ctx.parameters()
        if params_ctx is not None:
            params = self.visitParameters(ctx.parameters())
            duplicated_params = set([x for x in params if params.count(x) > 1])

            if len(duplicated_params) != 0:
                raise DuplicatedParameter(name, duplicated_params, ctx.start.line)
        else:
            params = []

        expression = Function(Callable(params,ctx.statement(),name,self))
        self.context.set_variable(name,expression)


    def visitFinalSTRING(self, ctx: confprolParser.FinalSTRINGContext):
        text = ctx.STRING().getText()
        text = text[1:len(text)-1]
        return Expression(text,text,ValueType.STRING)

    def visitExprMINUS(self, ctx: confprolParser.ExprMINUSContext):
        value = super().visit(ctx.expr2())
        return  TypeOperations.minus(value,super().visit(ctx.term()))


    def visitExprSUM(self, ctx: confprolParser.ExprSUMContext):
        value = super().visit(ctx.expr2())
        return TypeOperations.plus(value,super().visit(ctx.term()))

    def visitExprTERM(self, ctx: confprolParser.ExprTERMContext):
        return self.visit(ctx.term())

    def visitTermDIV(self, ctx: confprolParser.TermDIVContext):
        value = super().visit(ctx.term())
        return  TypeOperations.div(value,super().visit(ctx.final()))

    def visitTermFINAL(self, ctx: confprolParser.TermFINALContext):
        value = super().visit(ctx.final())
        return value

    def visitTermMULT(self, ctx: confprolParser.TermMULTContext):
        value = super().visit(ctx.term())
        return  TypeOperations.mult(value,super().visit(ctx.final()))

    def visitFinalPAR(self, ctx: confprolParser.FinalPARContext):
        value = super().visit(ctx.expr())

        return value

    def visitFinalNUMBER(self, ctx: confprolParser.FinalNUMBERContext):
        value =  int(ctx.NUMBER().getText())
        name = str(value)

        return Expression(value,name,ValueType.NUMBER)

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
        self.context.set_variable(variable,value)

        return super().visitAssign(ctx)

    def visitPrint(self, ctx: confprolParser.PrintContext):
        value = self.visit(ctx.expr()).value

        print(value)

