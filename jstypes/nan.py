from .types import String


#
# Represents NaN (not a number) for use with Number type
#
class NaN:
    def toString(self):
        return String('NaN')
