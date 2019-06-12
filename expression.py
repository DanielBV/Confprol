

class FinalExpression:


    def __init__(self, value, name):
        self.value = value
        self.name  = name


    def plus(self, other:'FinalExpression'):
        name = f"{self.name} + {other.name}"
        value = self.value + other.value
        return FinalExpression(value,name)

    def minus(self,other:'FinalExpression'):
        name = f"{self.name} - {other.name}"
        value = self.value - other.value
        return FinalExpression(value, name)

    def div(self, other:'FinalExpression'):
        name = f"{self.name} / {other.name}"
        value = self.value / other.value
        return FinalExpression(value, name)

    def mult(self, other:'FinalExpression'):
        name = f"{self.name} * {other.name}"
        value = self.value * other.value
        return FinalExpression(value, name)

