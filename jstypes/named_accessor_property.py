from .types import Undefined, Boolean


class NamedAccessorProperty():
    def __init__(self):
        """Sets the default values for the type."""
        self.__get = Undefined()
        self.__set = Undefined()
        self.__enumerable = Boolean('false')
        self.__configurable = Boolean('false')

    def get(self):
        return self.__get

    def set(self):
        return self.__set

    def enumerable(self):
        return self.__enumerable

    def configurable(self):
        return self.__configurable
