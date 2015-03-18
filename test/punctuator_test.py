import unittest
import utils
from lexer import lexer

class PunctuatorTests(unittest.TestCase):
    def test_punctuators_are_tokenised(self):  
        tokens = [
            ('{', 'LBRACE'),
            ('}', 'RBRACE'),
            ('(', 'LPAREN'),
            (')', 'RPAREN'),
            ('[', 'LBRACKET'),
            (']', 'RBRACKET'),
            ('.', 'DOT'),
            (';', 'SEMICOLON'),
            (',', 'COMMA')
        ]

        for t in tokens:
            utils.validate_token(self, lexer, t[0], t[1])
       
    def test_comparison_punctuators_are_tokenised(self):
        tokens = [
            ('<', 'LT'),
            ('>', 'GT'),
            ('<=', 'LTE'),
            ('>=', 'GTE'),
            ('==', 'EQUALV'),
            ('!=', 'NOTEQUALV'),
            ('===', 'EQUALVT'),
            ('!==', 'NOTEQUALVT')
        ]

        for t in tokens:
            utils.validate_token(self, lexer, t[0], t[1])
    
    def test_arithmetic_punctuators_are_tokenised(self):
        tokens = [
            ('+', 'PLUS'),
            ('-', 'MINUS'),
            ('*', 'MULTIPLY'),
            ('%', 'MODULO'),
            ('++', 'PLUSPLUS'),
            ('--', 'MINUSMINUS')
        ]

        for t in tokens:
            utils.validate_token(self, lexer, t[0], t[1])

    def test_bitwise_punctuators_are_tokenised(self):
        tokens = [
            ('<<', 'LSHIFT'),
            ('>>', 'RSHIFT'),
            ('>>>', 'LOGRSHIFT'),
            ('&', 'AND'),
            ('|', 'OR'),
            ('^', 'XOR'),
            ('~', 'BWNOT')
        ]

        for t in tokens:
            utils.validate_token(self, lexer, t[0], t[1])

    def test_logical_punctuators_are_tokenised(self):
        tokens = [
            ('!', 'NOT'),
            ('&&', 'ANDAND'),
            ('||', 'OROR'),
            ('?', 'TERNARY'),
            (':', 'COLON')
        ]

        for t in tokens:
            utils.validate_token(self, lexer, t[0], t[1])

    def test_assignment_punctuators_are_tokenised(self):
        tokens = [
            ('=', 'EQUAL'),
            ('+=', 'PLUSEQUAL'),
            ('-=', 'MINUSEQUAL'),
            ('*=', 'MULTIPLYEQUAL'),
            ('%=', 'MODULOEQUAL'),
            ('<<=', 'LSHIFTEQUAL'),
            ('>>=', 'RSHIFTEQUAL'),
            ('>>>=', 'LOGRSHIFTEQUAL'),
            ('&=', 'ANDEQUAL'),
            ('|=', 'OREQUAL'),
            ('^=', 'XOREQUAL')
        ]

        for t in tokens:
            utils.validate_token(self, lexer, t[0], t[1])

    def test_div_punctuators_are_tokenised(self):
        tokens = [
            ('/', 'FSLASH'),
            ('/=', 'FSLASHEQUAL')
        ]
        
        for t in tokens:
            utils.validate_token(self, lexer, t[0], t[1])