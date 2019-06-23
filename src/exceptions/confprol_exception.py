


class ConfprolException(Exception):

    def __init__(self,name):
        self.name = name


    def get_name(self):
        return self.name

    def get_message(self):
        return self.name