
from .confprol_exception import  ConfprolException

class EvaluateQuanticBooleanError(ConfprolException):

    def __init__(self):
        super(EvaluateQuanticBooleanError, self).__init__("EvaluateQuanticBooleanException")

    def get_message(self):
        return f"Quantic booleans can't be evaluated or operated as regular booleans. Use evalX() or evalY() to " \
            f"evaluate them first."

