import unittest
from jstypes import types


class ToPrimitiveTests(unittest.TestCase):
    def test_undefined_toprimitive(self):
        self.assertIsInstance(types.Undefined().toPrimitive(), types.Undefined)

    def test_null_toprimitive(self):
        self.assertIsInstance(types.Null().toPrimitive(), types.Null)

    def test_boolean_true_toprimitive(self):
        t = types.Boolean('true')
        conversion = t.toPrimitive()
        self.assertIsInstance(conversion, types.Boolean)
        self.assertEquals(conversion.value(), True)

    def test_number_toprimitive(self):
        t = types.Number(1.0)
        conversion = t.toPrimitive()
        self.assertIsInstance(conversion, types.Number)
        self.assertEquals(conversion.value(), 1.0)

    def test_string_toprimitive(self):
        t = types.String('foo')
        conversion = t.toPrimitive()
        self.assertIsInstance(conversion, types.String)
        self.assertEquals(conversion.value(), 'foo')
