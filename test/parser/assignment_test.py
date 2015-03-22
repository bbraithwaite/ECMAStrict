import unittest
import lexer.jslexer
import parser.jsparser

import ply.yacc as yacc
import ply.lex as lex

lexer = lex.lex(module=lexer.jslexer)
parser = yacc.yacc(module=parser.jsparser)

class AssigmentTest(unittest.TestCase):
    def test_variable_number(self):
        parse_tree = parser.parse("var foo = 1;", lexer=lexer)
        self.assertEquals(parse_tree, [('var', 'foo', ('number', 1.0))])

    def test_variable_string(self):
        parse_tree = parser.parse("var foo = 'bar';", lexer=lexer)
        self.assertEquals(parse_tree, [('var', 'foo', ('string', 'bar'))])

    def test_variable_identifier(self):
        parse_tree = parser.parse("var foo = bar;", lexer=lexer)
        self.assertEquals(parse_tree, [('var', 'foo', ('identifier', 'bar'))])     

    def test_variable_boolean_true(self):
        parse_tree = parser.parse("var foo = true;", lexer=lexer)
        self.assertEquals(parse_tree, [('var', 'foo', ('true', 'true'))])

    def test_variable_boolean_false(self):
        parse_tree = parser.parse("var foo = false;", lexer=lexer)
        self.assertEquals(parse_tree, [('var', 'foo', ('false', 'false'))])

    def test_variable_assignment(self):
        parse_tree = parser.parse("var foo = 1;foo = 3;", lexer=lexer)
        self.assertEquals(parse_tree, [
            ('var', 'foo', ('number', 1.0)),
            ('assign', 'foo', ('number', 3.0))
        ])
