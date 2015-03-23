import unittest
import utils
import ply.lex as lex
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

class HexLiteralTest(unittest.TestCase):
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
            ('0x10a', 'NUMBER', 266),
            ('0xDEADBEEF', 'NUMBER', 3735928559)
        ]

        utils.assertTokenList(self, lexer, tokens)
