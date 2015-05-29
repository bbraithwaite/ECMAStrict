import unittest
from jstypes import named_data_property, types


class NamedDataPropertyTest(unittest.TestCase):
    def test_value_default_is_undefined(self):
        prop = named_data_property.NamedDataProperty()
        self.assertIsInstance(prop.value(), types.Undefined)

    def test_writable_default_is_false(self):
        prop = named_data_property.NamedDataProperty()
        self.assertIsInstance(prop.writable(), types.Boolean)
        self.assertEquals(prop.writable().value(), types.Boolean('False').value())

    def test_enumerable_default_is_false(self):
        prop = named_data_property.NamedDataProperty()
        self.assertIsInstance(prop.enumerable(), types.Boolean)
        self.assertEquals(prop.enumerable().value(), types.Boolean('False').value())

    def test_configurable_default_is_false(self):
        prop = named_data_property.NamedDataProperty()
        self.assertIsInstance(prop.configurable(), types.Boolean)
        self.assertEquals(prop.configurable().value(), types.Boolean('False').value())
