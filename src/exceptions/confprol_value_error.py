from .confprol_exception import ConfprolException

class ConfprolValueError(ConfprolException):

    def __init__(self, msg):
        super(ConfprolValueError, self).__init__("ValueException")
        self.msg = msg

    def get_message(self):
        return self.msg