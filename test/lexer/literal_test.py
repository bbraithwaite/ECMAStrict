import unittest
import utils
import ply.lex as lex
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

class LiteralTest(unittest.TestCase):
    def test_null_literal(self):
        utils.validate_token(self, lexer, 'null', 'NULL')

    def test_true_boolean_literal(self):
        utils.validate_token(self, lexer, 'true', 'TRUE')

    def test_false_boolean_literal(self):
        utils.validate_token(self, lexer, 'false', 'FALSE')

    def test_integer_numeric_literal(self):
        tokens = [
            ('0', 'NUMBER', 0),
            ('1', 'NUMBER', 1),
            ('90', 'NUMBER', 90),
            ('-0', 'NUMBER', 0),
            ('-1', 'NUMBER', -1),
            ('+1', 'NUMBER', 1)
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_integer_sequnce_cannot_start_with_zero_numeric_literal(self):
        lexer.input('01')
        self.assertIsNone(lexer.token())

    def test_decimal_numeric_literal(self):
        tokens = [
            ('0.0', 'NUMBER', 0),
            ('-0.1', 'NUMBER', -0.1),
            ('+0.123', 'NUMBER', 0.123)
            #('.0', 'NUMBER'), add support for optional int literal
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_hex_numeric_literal(self):
        tokens = [
            ('0x1', 'NUMBER', 1.0),
            ('0X2', 'NUMBER', 2.0),
            ('0xa', 'NUMBER', 10),
            ('0xa', 'NUMBER', 10),
            ('0xb', 'NUMBER', 11),
            ('0xc', 'NUMBER', 12),
            ('0xd', 'NUMBER', 13),
            ('0xe', 'NUMBER', 14),
            ('0xf', 'NUMBER', 15),
            ('0x10', 'NUMBER', 16),
            ('0x10a', 'NUMBER', 266)
        ]

        utils.assertTokenList(self, lexer, tokens)


    def test_empty_string_literal(self):    
        utils.validate_token_and_value(self, lexer, "''", 'STRING', '')

    def test_simple_string_literal(self):
        utils.validate_token_and_value(self, lexer, "'foo bar'", 'STRING', 'foo bar')
