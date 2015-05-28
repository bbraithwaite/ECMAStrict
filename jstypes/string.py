from .types import BaseType, Boolean, Number


#
# String Type (8.4)
#
class String(BaseType):
    def __init__(self, value):
        self.__value = value

    def toBoolean(self):
        if len(self.value()) > 0:
            return Boolean('true')
        else:
            return Boolean('false')

    def toNumber(self):
        return Number(self)

    def value(self):
        return self.__value

    def toString(self):
        return self
