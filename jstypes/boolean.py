from .types import BaseType, Number, String


#
# Boolean Type (8.3)
#
class Boolean(BaseType):
    def __init__(self, value):
        self.__value = value

    def toBoolean(self):
        return self

    def toNumber(self):
        if (self.value()):
            return Number(1)

        return Number(0)

    def value(self):
        if self.__value == 'true':
            return True

        return False

    def toString(self):
        return String(self.__value)
