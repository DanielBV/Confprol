registry = {}




class MultiMethod(object):
    def __init__(self, name):
        self.name = name
        self.typemap = {}
        self.cache = {}

    def __call__(self, *args):

        args_types = self.get_types(args)

        if args_types in self.cache:
            return self.cache[args_types](*args)


        for key in self.typemap.keys():
            if len(key) != len(args_types):
                continue

            if self.check_key_matches(key, args_types):
                self.cache[args_types] = self.typemap.get(key)
                return self.typemap.get(key)(*args)

        raise TypeError("No match")

    def check_key_matches(self, key, args_types):

        for i, element in enumerate(key):

            if type(element) == tuple:
                found = False
                for type_ in element:

                    if self.compare(type_, args_types[i]):
                        found = True
                        break

                if not found:
                    return False


            elif not self.compare(element, args_types[i]):
                return False


        return True



    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate registration",function,self.typemap)
        self.typemap[types] = function

    def get_types(self,types):
        return tuple(arg.__class__ for arg in types)

    def compare(self, expected_type, found_type):
        return issubclass(found_type,expected_type)

class TypeMultiMethod(MultiMethod):

    def get_types(self,types):
        return tuple(arg.type for arg in types)

    def compare(self,expected_type,found_type):
        return found_type == expected_type or expected_type == object

def register(function,types,name_factory):
    function = getattr(function, "__lastreg__", function)
    name = function.__name__

    mm = registry.get(name)
    if mm is None:
        mm = registry[name] = name_factory(name)
    mm.register(types, function)
    mm.__lastreg__ = function
    return mm

def typemultimethod(*types):

    return lambda x: register(x,types,lambda name:TypeMultiMethod(name))


def multimethod(*types):
    return lambda x: register(x, types, lambda name: MultiMethod(name))

