from .types import Undefined, Boolean


class NamedDataProperty():
    def __init__(self):
        """Sets the default values for the type."""
        self.__value = Undefined()
        self.__writable = Boolean('false')
        self.__enumerable = Boolean('false')
        self.__configurable = Boolean('false')

    def value(self):
        return self.__value

    def writable(self):
        return self.__writable

    def enumerable(self):
        return self.__enumerable

    def configurable(self):
        return self.__configurable
