import unittest
import utils
import ply.lex as lex
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

class HexLiteralTest(unittest.TestCase):
    def test_hex_numeric_literal(self):
        tokens = [
            ('0x1', 'NUMBER_LITERAL', 1.0),
            ('0X2', 'NUMBER_LITERAL', 2.0),
            ('0xa', 'NUMBER_LITERAL', 10),
            ('0xa', 'NUMBER_LITERAL', 10),
            ('0xb', 'NUMBER_LITERAL', 11),
            ('0xc', 'NUMBER_LITERAL', 12),
            ('0xd', 'NUMBER_LITERAL', 13),
            ('0xe', 'NUMBER_LITERAL', 14),
            ('0xf', 'NUMBER_LITERAL', 15),
            ('0x10', 'NUMBER_LITERAL', 16),
            ('0x10a', 'NUMBER_LITERAL', 266),
            ('0xDEADBEEF', 'NUMBER_LITERAL', 3735928559)
        ]

        utils.assertTokenList(self, lexer, tokens)
