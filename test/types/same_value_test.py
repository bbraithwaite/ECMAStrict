import unittest
from jstypes import types
from jstypes import same_value


class same_valueTests(unittest.TestCase):
    def test_type_x_is_different_from_type_y_returns_false(self):
        x = types.Number(1)
        y = types.String('foo')
        self.assertFalse(same_value.equal(x, y))

    def test_type_x_is_undefined_returns_true(self):
        x = types.Undefined()
        y = types.String('foo')
        self.assertTrue(same_value.equal(x, y))

    def test_type_x_is_null_returns_true(self):
        x = types.Null()
        y = types.String('foo')
        self.assertTrue(same_value.equal(x, y))

    def test_type_x_is_number_and_x_y_is_nan_returns_true(self):
        x = types.Number('foo')
        y = types.Number('bar')
        self.assertTrue(same_value.equal(x, y))

    def test_type_x_is_number_and_x_y_are_zero_returns_true(self):
        x = types.Number(+0)
        y = types.Number(-0)
        self.assertTrue(same_value.equal(x, y))
        x = types.Number(-0)
        y = types.Number(+0)
        self.assertTrue(same_value.equal(x, y))

    def test_type_x_is_number_and_x_y_are_equal_returns_true(self):
        self.assertTrue(same_value.equal(types.Number(1), types.Number(1)))

    def test_type_x_is_number_and_x_y_are_not_equal_returns_false(self):
        self.assertFalse(same_value.equal(types.Number(1), types.Number(2)))

    def test_type_x_is_string_and_x_y_are_equal_returns_true(self):
        self.assertTrue(same_value.equal(types.String('foo'), types.String('foo')))

    def test_type_x_is_string_and_x_y_are_not_equal_returns_false(self):
        self.assertFalse(same_value.equal(types.String('foo'), types.String('foo ')))

    def test_type_x_is_boolean_and_x_y_are_equal_returns_true(self):
        self.assertTrue(same_value.equal(types.Boolean('true'), types.Boolean('true')))
        self.assertTrue(same_value.equal(types.Boolean('false'), types.Boolean('false')))

    def test_type_x_is_boolean_and_x_y_are_not_equal_returns_false(self):
        self.assertFalse(same_value.equal(types.Boolean('true'), types.Boolean('false')))
        self.assertFalse(same_value.equal(types.Boolean('false'), types.Boolean('true')))

    # TODO: Return true if x and y refer to the same object. Otherwise, return false.
