import unittest
from jstypes import types


class ToBooleanTests(unittest.TestCase):
    def test_undefined_toboolean(self):
        self.assertFalse(types.Undefined().toBoolean().value())

    def test_null_toboolean(self):
        self.assertFalse(types.Null().toBoolean().value())

    def test_boolean_true_toboolean(self):
        self.assertTrue(types.Boolean('true').toBoolean().value())
        self.assertFalse(types.Boolean('false').toBoolean().value())

    def test_number_toboolean(self):
        self.assertFalse(types.Number(0).toBoolean().value())
        self.assertFalse(types.Number(-0).toBoolean().value())
        self.assertFalse(types.Number(+0).toBoolean().value())
        self.assertFalse(types.Number(types.NaN()).toBoolean().value())
        self.assertTrue(types.Number(1).toBoolean().value())
        self.assertTrue(types.Number(1.0).toBoolean().value())

    def test_string_toboolean(self):
        self.assertFalse(types.String('').toBoolean().value())
        self.assertTrue(types.String('foo').toBoolean().value())
        self.assertTrue(types.String('true').toBoolean().value())
        self.assertTrue(types.String('false').toBoolean().value())
