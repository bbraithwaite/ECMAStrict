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
            ('0', 'NUMBER'),
            ('1', 'NUMBER'),
            ('90', 'NUMBER'),
            ('-0', 'NUMBER'),
            ('-1', 'NUMBER'),
            ('+1', 'NUMBER')
        ]

        for t in tokens:
            utils.validate_number(self, lexer, t[0], t[1])

    def test_integer_sequnce_cannot_start_with_zero_numeric_literal(self):
        lexer.input('01')
        self.assertIsNone(lexer.token())

    def test_decimal_numeric_literal(self):
        tokens = [
            ('0.0', 'NUMBER'),
            ('-0.1', 'NUMBER'),
            ('+0.123', 'NUMBER')
            #('.0', 'NUMBER'), add support for optional int literal
        ]

        for t in tokens:
            utils.validate_number(self, lexer, t[0], t[1])

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

        for t in tokens:
            lexer.input(t[0])
            token = lexer.token()
            self.assertEqual(token.value, t[2])
            self.assertEqual(token.type, 'NUMBER')


    def test_empty_string_literal(self):
        lexer.input("''")
        token = lexer.token()
        self.assertEqual(token.value, '')
        self.assertEqual(token.type, 'STRING')

    def test_simple_string_literal(self):
        lexer.input("'foo bar'")
        token = lexer.token()
        self.assertEqual(token.value, 'foo bar')
        self.assertEqual(token.type, 'STRING')
