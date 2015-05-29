from .types import Undefined, Null, Number, String, Boolean, NaN


def _isNaN(type):
    return isinstance(type.value(), NaN)


#
# The SameValue Algorithm (9.12)
#
def equal(x, y):
    if isinstance(x, Undefined):
        return True
    elif isinstance(x, Null):
        return True
    elif isinstance(x, Number):
        if _isNaN(x) and _isNaN(y):
            return True
        elif x.value() == y.value():
            return True
        else:
            return False
    elif isinstance(x, String):
        return x.value() == y.value()
    elif isinstance(x, Boolean):
        return x.value() == y.value()

    return False
