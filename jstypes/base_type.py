from .types import Boolean, NaN, Number


#
# Base class for all types
#
class BaseType:
    def toPrimitive(self):
        return self

    def isCallable(self):
        return Boolean('false')

    def toInteger(self):
        convert = Number(self.value())
        if not isinstance(convert.value(), NaN):
            return Number(int(convert.value()))

        return convert
