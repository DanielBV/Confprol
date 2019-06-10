



class Context:

    def __init__(self):
        self.parent = None
        self.variables = {}
        self.functions = {}

    def create_subcontext(self):
        new_context = Context()
        new_context.parent = self

        return new_context

    def get_variable(self, id_):
        print("Buscando la variable ", id_)
        if id_ in self.variables:
            return self.variables[id_]
        if self.parent is not None:
            return self.parent.get_variable(id_)

        return None

    def set_variable(self, id_, value):
        self.variables[id_] = value

    def set_variables(self, dicts_):
        for key in dicts_.keys():
            self.set_variable(key,dicts_[key])

    def add_function(self, name, function):
        if  name in self.functions:
            raise ValueError("Function ", name, " already defined")

        self.functions[name] = function

    def get_function(self, id_):
        if id_ in self.functions:
            return self.functions[id_]
        if self.parent is not None:
            return self.parent.get_functions(id_)

        return None