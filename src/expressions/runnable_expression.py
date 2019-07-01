from src.type import ValueType
from .expression import Expression
from src.exceptions import  TooManyArguments, ArgumentsMissing


class RunnableExpression(Expression):
    
    def __init__(self,function,name):
        super(RunnableExpression, self).__init__(function,name,ValueType.FUNCTION)


    def run(self,values):
        try:
            expr = self.value.run(values)
            value_names = list(map(lambda a: a.name, values))
            expr.name = f"{self.name}(" + ",".join(value_names) + ")"
            return expr
        except (TooManyArguments,ArgumentsMissing) as e:
            e.function = self.name
            raise e

    def copy(self):
        return RunnableExpression(self.value,self.name)


    def __str__(self):
        return f"[function {self.name}]"