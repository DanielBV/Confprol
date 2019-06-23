

class RuntimeException(Exception):

    def __init__(self,line, base_exception):
        self.line = line
        self.base_exception = base_exception



    def get_message(self):
        return f"{self.base_exception.get_name()} line {self.line}: {self.base_exception.get_message()}"