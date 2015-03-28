import unittest
import jstypes.types as types

class ToNumberTests(unittest.TestCase):
    def test_undefined_tonumber(self):
        self.assertIsInstance(types.Undefined().toNumber(), types.NaN)

    def test_null_tonumber(self):
        self.assertIsInstance(types.Null().toNumber(), types.Number)
        self.assertEquals(types.Null().toNumber().value(), 0)

    def test_boolean_true_tonumber(self):
        self.assertIsInstance(types.Boolean('true').toNumber(), types.Number)
        self.assertEquals(types.Boolean('true').toNumber().value(), 1)
        self.assertIsInstance(types.Boolean('false').toNumber(), types.Number)
        self.assertEquals(types.Boolean('false').toNumber().value(), 0)

    def test_number_tonumber(self):
        self.assertIsInstance(types.Number(1).toNumber(), types.Number)
        self.assertEquals(types.Number(1).toNumber().value(), 1)

    def test_string_tonumber(self):
        self.assertIsInstance(types.String('').toNumber(), types.Number)
        self.assertEquals(types.String('').toNumber().value(), 0)
        self.assertEquals(types.String(' ').toNumber().value(), 0)
        self.assertEquals(types.String('1').toNumber().value(), 1.0)
        self.assertEquals(types.String('  1  ').toNumber().value(), 1.0)
        self.assertEquals(types.String('2.0').toNumber().value(), 2)
        self.assertEquals(types.String('.1').toNumber().value(), 0.1)
        self.assertEquals(types.String('+1').toNumber().value(), 1.0)
        self.assertEquals(types.String('-1').toNumber().value(), -1.0)
        self.assertEquals(types.String('Infinity').toNumber().value(), float('inf'))
        self.assertEquals(types.String('-Infinity').toNumber().value(), -float('inf'))
        self.assertEquals(types.String('2e1').toNumber().value(), 20)
        self.assertEquals(types.String('2E2').toNumber().value(), 200)
        self.assertEquals(types.String('0x1').toNumber().value(), 1)
        self.assertEquals(types.String('0X1').toNumber().value(), 1)
        self.assertEquals(types.String('0xa').toNumber().value(), 10)
        self.assertIsInstance(types.String('foo').toNumber(), types.Number)
        self.assertIsInstance(types.String('foo').toNumber().value(), types.NaN)

    def test_number_tointeger(self):
        self.assertEquals(types.Number(1.23).toInteger().value(), 1)
        self.assertEquals(types.Number(0.23).toInteger().value(), 0)
        self.assertIsInstance(types.Number(types.String('foo')).toInteger().value(), types.NaN)
