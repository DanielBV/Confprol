

class MethodNotDefined(Exception):

    def __init__(self,object_name,method_name,line):
        self.object_name = object_name
        self.method_name = method_name
        self.line = line