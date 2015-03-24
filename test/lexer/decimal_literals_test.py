"""
Tests for the numeric literals that start with a Decima Literal grammar section below:

DecimalLiteral ::
    DecimalIntegerLiteral . DecimalDigits (opt) ExponentPart (opt)
    DecimalIntegerLiteral ExponentPart (opt)

DecimalIntegerLiteral :: 
    0
    NonZeroDigit DecimalDigits (opt)

"""

import unittest
import utils
import ply.lex as lex
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

class DecimalIntegerLiteralTest(unittest.TestCase):
    """
    Tests combiation:
        DecimalIntegerLiteral
    """
    def test_with_decimal_integer_literal(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('0', 'NUMBER', 0),
            ('1', 'NUMBER', 1),
            ('123', 'NUMBER', 123)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_integer_literal_cannot_start_with_multiple_zeros(self):
        utils.assertTokensAreNone(self, lexer, ['00'])

    def test_with_decimal_integer_literal_exponent(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('0e0', 'NUMBER', 0),
            ('1E1', 'NUMBER', 10),
            ('12E2', 'NUMBER', 1200)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_integer_literal_exponent_cannot_start_with_multiple_zeros(self):
        utils.assertTokensAreNone(self, lexer, ['00e1'])

    """
    Tests combiation:
        DecimalIntegerLiteral . DecimalDigits
    """
    def test_with_decimal_and_digits_matches_tokens(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('0.0', 'NUMBER', 0),
            ('1.0', 'NUMBER', 1),
            ('123.0', 'NUMBER', 123), 
            ('123.456', 'NUMBER', 123.456),
            ('123.', 'NUMBER', 123),
            ('123.', 'NUMBER', 123)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_and_digits_cannot_start_with_multiple_zeros(self):
         utils.assertTokensAreNone(self, lexer, ['00.01'])

    """
    Tests combiation:
        DecimalIntegerLiteral . DecimalDigits ExponentPart
    """
    def test_with_decimal_and_digits_and_exponent_matches_tokens(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('1.0e1', 'NUMBER', 10),
            ('1.0E1', 'NUMBER', 10),
            ('1.0e+1', 'NUMBER', 10),
            ('1.0e-1', 'NUMBER', 0.1)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_and_digits_and_exponent_cannot_start_with_multiple_zeros(self):
        utils.assertTokensAreNone(self, lexer, ['00.0e1'])

    """
    Tests combiation:
        DecimalIntegerLiteral . ExponentPart
    """
    def test_with_decimal_and_exponent_matches_tokens(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('2.e1', 'NUMBER', 20),
            ('12.E1', 'NUMBER', 120),
            ('2.e-1', 'NUMBER', 0.2)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_decimal_and_exponent_cannot_start_with_multiple_zeros(self):
        utils.assertTokensAreNone(self, lexer, ['00.e1'])

    """
    Tests combiation:
        DecimalIntegerLiteral ExponentPart
    """
    def test_with_integer_and_exponent_matches_tokens(self):
        tokens = [
            # (input, expectedType, expectedValue)
            ('2e1', 'NUMBER', 20),
            ('12E1', 'NUMBER', 120),
            ('2e-1', 'NUMBER', 0.2)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_with_integer_and_exponent_cannot_start_with_multiple_zeros(self):
        utils.assertTokensAreNone(self, lexer, ['00e1'])
