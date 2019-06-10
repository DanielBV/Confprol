

class ReturnException(Exception):

    def __init__(self, return_value):
        super(ReturnException, self).__init__()
        self.return_value = return_value
