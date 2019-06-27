



class Context:

    def __init__(self):
        self.parent = None
        self.variables = {}

    def create_subcontext(self):
        new_context = Context()
        new_context.parent = self

        return new_context


    def has_attribute(self, id_):
        return self.get_attribute(id_) is not None


    def get_attribute(self, id_):
        if id_ in self.variables:
            return self.variables[id_]
        if self.parent is not None:
            return self.parent.get_attribute(id_)

        return None

    def set_variable(self, id_, value):
        self.variables[id_] = value

    def set_variables(self, dicts_):
        for key in dicts_.keys():
            self.set_variable(key,dicts_[key])

    def shallow_copy(self):
        if self.parent is not None:
            base = self.parent.create_subcontext()
        else:
            base = Context()

        base.set_variables(self.variables)
        print(self.variables)
        return base


    def __str__(self):
        if self.parent is None:
            parent_str = ""
        else:
            parent_str = str(self.parent)

        return str({"context":self.variables, "parent":parent_str})




