import unittest
import jstypes.types as types
import jstypes.same_value as sameValue

class SameValueTests(unittest.TestCase):
    def test_type_x_is_different_from_type_y_returns_false(self):
        x = types.Number(1)
        y = types.String('foo')
        self.assertFalse(sameValue.equal(x, y))

    def test_type_x_is_undefined_returns_true(self):
        x = types.Undefined()
        y = types.String('foo')
        self.assertTrue(sameValue.equal(x, y))

    def test_type_x_is_null_returns_true(self):
        x = types.Null()
        y = types.String('foo')
        self.assertTrue(sameValue.equal(x, y))

    def test_type_x_is_number_and_x_y_is_nan_returns_true(self):
        x = types.Number('foo')
        y = types.Number('bar')
        self.assertTrue(sameValue.equal(x, y))

    def test_type_x_is_number_and_x_y_are_zero_returns_true(self):
        x = types.Number(+0)
        y = types.Number(-0)
        self.assertTrue(sameValue.equal(x, y))
        x = types.Number(-0)
        y = types.Number(+0)
        self.assertTrue(sameValue.equal(x, y))

    def test_type_x_is_number_and_x_y_are_equal_returns_true(self):
        self.assertTrue(sameValue.equal(types.Number(1), types.Number(1)))

    def test_type_x_is_number_and_x_y_are_not_equal_returns_false(self):
        self.assertFalse(sameValue.equal(types.Number(1), types.Number(2)))

    def test_type_x_is_string_and_x_y_are_equal_returns_true(self):
        self.assertTrue(sameValue.equal(types.String('foo'), types.String('foo')))

    def test_type_x_is_string_and_x_y_are_not_equal_returns_false(self):
        self.assertFalse(sameValue.equal(types.String('foo'), types.String('foo ')))
 
    def test_type_x_is_boolean_and_x_y_are_equal_returns_true(self):
        self.assertTrue(sameValue.equal(types.Boolean('true'), types.Boolean('true')))
        self.assertTrue(sameValue.equal(types.Boolean('false'), types.Boolean('false')))

    def test_type_x_is_boolean_and_x_y_are_not_equal_returns_false(self):
        self.assertFalse(sameValue.equal(types.Boolean('true'), types.Boolean('false')))
        self.assertFalse(sameValue.equal(types.Boolean('false'), types.Boolean('true')))

    # TODO: Return true if x and y refer to the same object. Otherwise, return false.
