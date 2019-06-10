

class ArgumentMismatch(Exception):

    def __init__(self, message, name):
        super(message)
        self.name = name