from .types import Boolean, NaN, String, BaseType


#
# Undefined Type (8.1)
#
class Undefined(BaseType):
    def toBoolean(self):
        return Boolean('false')

    def toNumber(self):
        return NaN()

    def toString(self):
        return String('undefined')
