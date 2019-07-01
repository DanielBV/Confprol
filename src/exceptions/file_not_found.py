from .confprol_exception import ConfprolException


class FileNotFound(ConfprolException):

    def __init__(self,file):
        self.file = file
        super(FileNotFound, self).__init__("FileNotFoundException")


    def get_message(self):
        return f"File {self.file} not found."


class CannotOpenDirectory(ConfprolException):

    def __init__(self, dir):
        self.dir = dir
        super(CannotOpenDirectory, self).__init__("CannotOpenDirectoryException")

    def get_message(self):
        return f"The directory {self.dir} can't be opened or imported."

