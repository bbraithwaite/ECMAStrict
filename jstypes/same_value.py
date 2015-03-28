import types

def _isNaN(type):
    return isinstance(type.value(), types.NaN)

def _isZero(type):
    return type.value() == 0

#
# The SameValue Algorithm (9.12)
#
def equal(x, y):
    
    if isinstance(x, types.Undefined):
        return True
    elif isinstance(x, types.Null):
        return True
    elif isinstance(x, types.Number):
        if _isNaN(x) and _isNaN(y):
            return True
        elif x.value() == y.value():
            return True
        else:
            return False
    elif isinstance(x, types.String):
        return x.value() == y.value()
    elif isinstance(x, types.Boolean):
        return x.value() == y.value()

    return False
