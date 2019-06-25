




class ConfprolObject:

    def __init__(self, value):
        self.value = value
        self.attributes = {}

    def set_attribute(self, name, value: 'Expression'):
        self.attributes[name] = value

    def set_attributes(self, attr):
        for attribute in attr.keys():
            self.set_attribute(attribute, attr[attribute])



    def get_attribute(self, attribute):

        if attribute in self.attributes:
            return self.attributes[attribute]
        else:
            return None

    def has_attribute(self, attribute):
        return attribute in self.attributes

