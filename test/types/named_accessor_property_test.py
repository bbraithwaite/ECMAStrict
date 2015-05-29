import unittest
from jstypes import named_accessor_property, types


class NamedAccessorPropertyTest(unittest.TestCase):
    def test_get_default_is_undefined(self):
        prop = named_accessor_property.NamedAccessorProperty()
        self.assertIsInstance(prop.get(), types.Undefined)

    def test_set_default_is_undefined(self):
        prop = named_accessor_property.NamedAccessorProperty()
        self.assertIsInstance(prop.set(), types.Undefined)

    def test_enumerable_default_is_false(self):
        prop = named_accessor_property.NamedAccessorProperty()
        self.assertIsInstance(prop.enumerable(), types.Boolean)
        self.assertEquals(prop.enumerable().value(), types.Boolean('False').value())

    def test_configurable_default_is_false(self):
        prop = named_accessor_property.NamedAccessorProperty()
        self.assertIsInstance(prop.configurable(), types.Boolean)
        self.assertEquals(prop.configurable().value(), types.Boolean('False').value())
