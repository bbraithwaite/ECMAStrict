import unittest
from jstypes import types


class IsCallableTests(unittest.TestCase):
    def test_undefined_iscallable(self):
        self.assertFalse(types.Undefined().isCallable().value())

    def test_null_iscallable(self):
        self.assertFalse(types.Null().isCallable().value())

    def test_boolean_true_iscallable(self):
        self.assertFalse(types.Boolean('true').isCallable().value())

    def test_number_iscallable(self):
        self.assertFalse(types.Number(0).isCallable().value())

    def test_string_iscallable(self):
        self.assertFalse(types.String('').isCallable().value())
