import unittest
import jstypes.types as types

class ToStringTests(unittest.TestCase):
    def test_undefined_tostring(self):
        self.assertEquals(types.Undefined().toString().value(), 'undefined')

    def test_null_tostring(self):
        self.assertEquals(types.Null().toString().value(), 'null')

    def test_nan_tostring(self):
        self.assertEquals(types.NaN().toString().value(), 'NaN')

    def test_boolean_true_tostring(self):
        self.assertEquals(types.Boolean('true').toString().value(), 'true')

    def test_boolean_false_tostring(self):
        self.assertEquals(types.Boolean('false').toString().value(), 'false')

    def test_string_tostring(self):
        self.assertEquals(types.String('hello world').toString().value(), 'hello world')

    def test_number_tostring(self):
        self.assertEquals(types.Number(1.0).toString().value(), '1.0')
        self.assertEquals(types.Number(-2.0).toString().value(), '-2.0')
        self.assertEquals(types.Number('Infinity').toString().value(), 'Infinity')
        self.assertEquals(types.Number('-Infinity').toString().value(), '-Infinity')
