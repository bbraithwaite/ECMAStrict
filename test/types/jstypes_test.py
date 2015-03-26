import unittest
import jstypes.types as types

class JsTypeTests(unittest.TestCase):
    def test_undefined_tostring(self):
        t = types.Undefined()       
        self.assertEquals(t.toString(), 'undefined')

    def test_null_tostring(self):
        t = types.Null()        
        self.assertEquals(t.toString(), 'null')

    def test_boolean_true_tostring(self):
        t = types.Boolean('true')       
        self.assertEquals(t.toString(), 'true')

    def test_boolean_false_tostring(self):
        t = types.Boolean('false')      
        self.assertEquals(t.toString(), 'false')

    def test_boolean_true_value(self):
        t = types.Boolean('true')       
        self.assertEquals(t.value(), True)

    def test_boolean_false_value(self):
        t = types.Boolean('false')
        self.assertEquals(t.value(), False)

    def test_string_value(self):
        t = types.String('hello world')
        self.assertEquals(t.value(), 'hello world')

    def test_string_tostring(self):
        t = types.String('hello world')
        self.assertEquals(t.toString(), 'hello world')

    def test_number_value(self):
        t = types.Number(1.0)
        self.assertEquals(t.value(), 1.0)

    def test_number_tostring(self):
        t = types.Number(1.0)
        self.assertEquals(t.toString(), '1.0')
