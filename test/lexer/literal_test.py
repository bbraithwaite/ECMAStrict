import unittest
import utils
import ply.lex as lex
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

class LiteralTest(unittest.TestCase):
    def test_null_literal(self):
        utils.validate_token(self, lexer, 'null', 'NULL_LITERAL')

    def test_true_boolean_literal(self):
        utils.validate_token(self, lexer, 'true', 'BOOLEAN_LITERAL')

    def test_false_boolean_literal(self):
        utils.validate_token(self, lexer, 'false', 'BOOLEAN_LITERAL')
