"""
Tests for 7.8.3 Numeric Literals.
"""

import unittest
import utils
import ply.lex as lex
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

class DecimalIntegerLiteralTest(unittest.TestCase):
    def test_with_decimal_integer_literal(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('0', 'NUMBER', 0),
            ('1', 'NUMBER', 1),
            ('123', 'NUMBER', 123)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_integer_literal_exponent(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('0e0', 'NUMBER', 0),
            ('1E1', 'NUMBER', 10),
            ('12E2', 'NUMBER', 1200)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_and_digits(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('0.0', 'NUMBER', 0),
            ('1.0', 'NUMBER', 1),
            ('123.0', 'NUMBER', 123), 
            ('123.456', 'NUMBER', 123.456),
            ('123.', 'NUMBER', 123),
            ('123.', 'NUMBER', 123),
            ('.0', 'NUMBER', 0),
            ('.12', 'NUMBER', 0.12)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_and_digits_and_exponent(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('1.0e1', 'NUMBER', 10),
            ('1.0E1', 'NUMBER', 10),
            ('1.0e+1', 'NUMBER', 10),
            ('1.0e-1', 'NUMBER', 0.1)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_and_exponent(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('.0e1', 'NUMBER', 0),
            ('.0E1', 'NUMBER', 0),
            ('.1e+1', 'NUMBER', 1.0),
            ('.1e-1', 'NUMBER', 0.01)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_and_exponent_matches_tokens(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('2.e1', 'NUMBER', 20),
            ('12.E1', 'NUMBER', 120),
            ('2.e-1', 'NUMBER', 0.2)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_integer_and_exponent_matches_tokens(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('2e1', 'NUMBER', 20),
            ('12E1', 'NUMBER', 120),
            ('2e-1', 'NUMBER', 0.2)
        ]

        utils.assertTokenList(self, lexer, tokens)
