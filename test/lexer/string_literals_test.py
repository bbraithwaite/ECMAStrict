"""
Tests for 7.8.4 String Literals
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
            ("''", 'STRING_LITERAL', ''),
            ("'foo bar'", 'STRING_LITERAL', 'foo bar'),
            ('""', 'STRING_LITERAL', ''),
            ('"foo bar"', 'STRING_LITERAL', 'foo bar')
        ]

        utils.assertTokenList(self, lexer, tokens)       

    def test_invalid_string_literal(self):
        tokens = [
            ("'"),
            ("'\\'"),
            ("\n"),
            ("\r"),
            ('"'),
            ('"\\"'),
            ('"\n"'),
            ('"\r"')
        ]

        utils.assertTokensAreNone(self, lexer, tokens)

    def test_string_literal_with_line_continuation(self):      
        tokens = [
            # (input, expectedType, expectedValue)
            ("'foo\\\nbar\\\nbaz'", 'STRING_LITERAL', 'foo\\\nbar\\\nbaz'),
            ('"foo\\\nbar\\\nbaz"', 'STRING_LITERAL', 'foo\\\nbar\\\nbaz')
        ]

        utils.assertTokenList(self, lexer, tokens)    

    def test_string_literal_escape_sequences(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ("'\u221e'", 'STRING_LITERAL', '\u221e'),
            ('"To \u221e and beyond"', 'STRING_LITERAL', 'To \u221e and beyond'),
            ("'Show me the \xA3'", 'STRING_LITERAL', 'Show me the \xA3'),
            ("'\b'", 'STRING_LITERAL', '\b'),
            ("'\hello'", 'STRING_LITERAL', '\hello'),
            ("'hello \" world'", 'STRING_LITERAL', 'hello \" world')
        ]

        utils.assertTokenList(self, lexer, tokens)
