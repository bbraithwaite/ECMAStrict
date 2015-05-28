from .types import BaseType, Boolean, Number, String


#
# Null Type (8.2)
#
class Null(BaseType):
    def toBoolean(self):
        return Boolean('false')

    def toNumber(self):
        return Number(0)

    def toString(self):
        return String('null')
