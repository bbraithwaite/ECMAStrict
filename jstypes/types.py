class Null:
    def toString(self):
        return 'null'

class Undefined:
    def toString(self):
        return 'undefined'

class Boolean:
    def __init__(self, value):
        self.__value = value

    def value(self):
        if self.__value == 'true':
            return True
        
        return False
            
    def toString(self):
        return self.__value

class String:
    def __init__(self, value):
        self.__value = value

    def value(self):
        return self.__value
            
    def toString(self):
        return self.__value

class Number:
    def __init__(self, value):
        self.__value = value

    def value(self):
        return self.__value
            
    def toString(self):
        return str(self.__value)
