# import types


class Object():
    
    def value(self):
        return self._value



# #
# # Object Type (8.6)
# #
# class Object():
#     def __init__(self):
#         self.__properties = []          #
#         self.__prototype = types.Null() # Object or Null. All objects have this.
#         self.__extensible = True        # If true, own properties may be added to the object.

#         # Reserved class names: "Arguments", "Array", "Boolean", "Date", "Error", "Function", "JSON", "Math", "Number", "Object", "RegExp", and "String"
#         self.__class = ''               # A String value indicating a specification defined classification of objects. Can be accessed via Object.prototype.toString.

#     # Returns the value of the named property.
#     def get(self, propertyName):
#         return self.__properties[propertyName].value()

#     # Returns the Property Descriptor of the named own property of this object, or undefined if absent.
#     def getOwnProperty(self, propertyName):
#         return self.__properties[propertyName].descriptor()

#     # Returns the fully populated Property Descriptor of the named property of this object, or undefined if absent.
#     def getProperty(self, propertyName):
#         # need to traverse to parent object if not found here?
#         return self.__properties[propertyName].descriptor()

#     # Sets the specified named property to the value of the second parameter. The flag controls failure handling.
#     def put(self, propertyName, any, Boolean):
#         return self.__properties[propertyName].set(any)

#     # Returns a Boolean value indicating whether a [[Put]] operation with PropertyName can be performed.
#     def canPut(self, propertyName):
#         return self.__properties[propertyName].writable()

#     # Returns a Boolean value indicating whether the object already has a property with the given name.
#     def hasProperty(self, propertyName):
#         return self.__properties[propertyName] != None

#     # Removes the specified named own property from the object. The flag controls failure handling.
#     def delete(self, propertyName):
#         return self.__properties[propertyName].remove()

#     # Hint is a String. Returns a default value for the object.
#     def defaultValue(self, hint):
#         return None # must be primitive OR can throw TypeError ex.

#     # Creates or alters the named own property to have the state described by a Property Descriptor. 
#     # The flag controls failure handling.
#     def defineOwnProperty(self, propertyName, propertyDescriptor, Boolean):
#         return False



# class NameAccessorProperty():
#     def __init__(self):
#         self.__value = types.Undefined()
#         self.__writable = types.Boolean('false')
#         self.__enumerable = types.Boolean('false')
#         self.__configurable = types.Boolean('false')

#     def get(self):
#         return self.__value

#     def set(self, v):
#         self.__value = v
    
#     def enumerable(self):
#         return self.__enumerable

#     def configurable(self):
#         return self.__configurable
