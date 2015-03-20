import unittest
import lexer.jslexer
import parser.jsparser

import ply.yacc as yacc
import ply.lex as lex

lexer = lex.lex(module=lexer.jslexer)
parser = yacc.yacc(module=parser.jsparser)

class FirstTest(unittest.TestCase):
    def test_instance_of_parser(self):
        parse_tree = parser.parse('foo', lexer=lexer)
        self.assertEquals(parse_tree, ('identifier', 'foo'))
