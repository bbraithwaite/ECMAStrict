import unittest
import utils
import ply.lex as lex
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

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

        utils.assertTokenList(self, lexer, tokens)
       
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

        utils.assertTokenList(self, lexer, tokens)
    
    def test_arithmetic_punctuators_are_tokenised(self):
        tokens = [
            ('+', 'PLUS'),
            ('-', 'MINUS'),
            ('*', 'MULTIPLY'),
            ('%', 'MODULO'),
            ('++', 'PLUSPLUS'),
            ('--', 'MINUSMINUS')
        ]

        utils.assertTokenList(self, lexer, tokens)

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

        utils.assertTokenList(self, lexer, tokens)

    def test_logical_punctuators_are_tokenised(self):
        tokens = [
            ('!', 'NOT'),
            ('&&', 'ANDAND'),
            ('||', 'OROR'),
            ('?', 'TERNARY'),
            (':', 'COLON')
        ]

        utils.assertTokenList(self, lexer, tokens)

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

        utils.assertTokenList(self, lexer, tokens)

    def test_div_punctuators_are_tokenised(self):
        tokens = [
            ('/', 'FSLASH'),
            ('/=', 'FSLASHEQUAL')
        ]
        
        utils.assertTokenList(self, lexer, tokens)
