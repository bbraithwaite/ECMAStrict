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
