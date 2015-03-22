import unittest
import interpreter.jsinterpreter as interpreter

class AssignmentTest(unittest.TestCase):
    def test_number_assignment(self):
        parse_tree = [('var', 'foo', ('number', 1.0))]
        env = interpreter.interpret(parse_tree)
        self.assertEquals(env, { 'foo' : 1.0 })
