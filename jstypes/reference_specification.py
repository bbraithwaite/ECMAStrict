
class ReferenceSpecification:
    """
    8.7 The Reference Specification Type

    A Reference is a resolved name binding. A Reference consists of three components:

        1. the base value
        2. the referenced name
        3. the Boolean valued strict reference flag. (will always be true!)

    The base value is either undefined, an Object, a Boolean, a String, a Number, or an environment record (10.2.1).
    A base value of undefined indicates that the reference could not be resolved to a binding. The referenced name is a String.

    """
    def __init__(self, base, name):
        self.__base = base
        self.__name = name

    # Returns the base value component of the reference V.
    def getBase(self, v):
        return self.__base

    # Returns the referenced name component of the reference V.
    def getReferencedName(self, v):
        return None

    # Returns the strict reference component of the reference V.
    def isStrictReference(self, v):
        return None

    # Returns true if the base value is a Boolean, String, or Number.
    def hasPrimitiveBase(self, v):
        return False

    # Returns true if either the base value is an object or HasPrimitiveBase(V) is true; otherwise returns false.
    def isPropertyReference(self, v):
        return False

    # Returns true if the base value is undefined and false otherwise.
    def isUnresolvableReference(self, v):
        return False
