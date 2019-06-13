



class StringOperations:

    @staticmethod
    def concatenation(string1,string2):
        from src.expressions import StringExpression
        value =  str(string1) + str(string2)
        return StringExpression(value,value)