"""
Tests for 7.8.5 Regular Expression Literals
"""

import unittest
import utils
import ply.lex as lex
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

class RegExLiteralsTest(unittest.TestCase):
    def test_string_literal(self):      
        tokens = [
            # (input, expectedType, expectedValue)
            ('/a/', 'REGEX_LITERAL', '/a/'),
            ('/\a/', 'REGEX_LITERAL', '/\a/'),
            ('/[]/', 'REGEX_LITERAL', '/[]/'),
            ('/[a]/', 'REGEX_LITERAL', '/[a]/'),
            ('/[a-z]/', 'REGEX_LITERAL', '/[a-z]/'),
            ('/[\*]/', 'REGEX_LITERAL', '/[\*]/'),
            ('/a/g', 'REGEX_LITERAL', '/a/g'),
            ('/abc/', 'REGEX_LITERAL', '/abc/'),
            ('/abc\*/', 'REGEX_LITERAL', '/abc\*/'),
            ('/a\*/', 'REGEX_LITERAL', '/a\*/'),
            ('/[a-z][0-9]/g', 'REGEX_LITERAL', '/[a-z][0-9]/g'),
        ]

        utils.assertTokenList(self, lexer, tokens)       
