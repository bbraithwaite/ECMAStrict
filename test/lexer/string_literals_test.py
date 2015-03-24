"""
Tests for string literals.
"""

import unittest
import utils
import ply.lex as lex
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

class StringLiteralsTest(unittest.TestCase):
    def test_string_literal(self):      
        tokens = [
            # (input, expectedType, expectedValue)
            ("''", 'STRING', ''),
            ("'foo bar'", 'STRING', 'foo bar')
        ]

        utils.assertTokenList(self, lexer, tokens)       

    def test_invalid_string_literal(self):
        tokens = [
            ("'"),
            ("'\\'"),
            ("\n"),
            ("\r")
        ]

        utils.assertTokensAreNone(self, lexer, tokens)

    def test_string_literal_with_line_continuation(self):      
        tokens = [
            # (input, expectedType, expectedValue)
            ("'foo\\\nbar\\\nbaz'", 'STRING', 'foo\\\nbar\\\nbaz')
        ]

        utils.assertTokenList(self, lexer, tokens)    
