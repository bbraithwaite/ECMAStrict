import unittest
import interpreter.jsinterpreter as interpreter

class AssignmentTest(unittest.TestCase):
    def test_number_assignment(self):
        parse_tree = [('var', 'foo', ('number', 1.0))]
        env = interpreter.interpret(parse_tree)
        self.assertEquals(env, { 'foo' : 1.0 })

    def test_mutli_var_assignment(self):
        parse_tree = [
            ('var', 'foo', ('string', 'bar')),
            ('var', 'bar', ('string', 'baz'))
        ]
        env = interpreter.interpret(parse_tree)
        self.assertEquals(env, { 'foo' : 'bar' , 'bar' : 'baz'})

    def test_reassignment_to_value(self):
        parse_tree = [
            ('var', 'foo', ('string', 'bar')),
            ('assign', 'foo', ('string', 'baz'))
        ]
        env = interpreter.interpret(parse_tree)
        self.assertEquals(env, { 'foo' : 'baz'})    

    def test_reassignment_to_identifier(self):
        parse_tree = [
            ('var', 'foo', ('number', 1)),
            ('var', 'bar', ('number', 2)),
            ('assign', 'foo', ('identifier', 'bar'))
        ]
        env = interpreter.interpret(parse_tree)
        self.assertEquals(env, { 'foo' : 2, 'bar' : 2})
