from .confprol_exception import ConfprolException

class ElementNotContained(ConfprolException):
    
    def __init__(self,list_name, expr_missing):
        self.list_name = list_name
        self.expr = expr_missing
        super(ElementNotContained, self).__init__("ElementNotContainedException")


    def get_message(self):
        return f"The list {self.list_name} doesn't contain {self.expr}"