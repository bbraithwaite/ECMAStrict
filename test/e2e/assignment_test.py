"""
End-to-end tests using lexer, parser and interpreter.
"""

import unittest
import lexer.jslexer as jslexer
import parser.jsparser as jsparser
import interpreter.jsinterpreter as jsinterpreter

import ply.yacc as yacc
import ply.lex as lex

lexer = lex.lex(module=jslexer)
parser = yacc.yacc(module=jsparser)

class AssignmentTest(unittest.TestCase):
    def test_number_assignment(self):
        with open ("test/e2e/assignment-fixture.js", "r") as jsFile:
            parse_tree = parser.parse(jsFile.read(), lexer=lexer)
            env = jsinterpreter.interpret(parse_tree)
            expected = {'bar': 'baz', 'foo': 'bar', 'one': 2.0, 'two': 2.0}
            self.assertEquals(env, expected)
