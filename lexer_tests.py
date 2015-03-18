import unittest
from lexer import lexer

class LexerTests(unittest.TestCase):

    def _validate_token(self, value, typeName):
        lexer.input(value)
        token = lexer.token()
        self.assertEqual(token.value, value)
        self.assertEqual(token.type, typeName)
    
    def _validate_identifier_char(self, value):
        self._validate_token(value, 'IDENTIFIER')

    def _invalid_first_identifier_char(self, input):
        lexer.input(input)
        token = lexer.token()
        self.assertEqual(token, None)

    def _validate_keyword(self, keyword):
        self._validate_token(keyword, keyword.upper())

    # Comments
    def test_single_line_comment_is_ignored(self):
        lexer.input('// this is a comment')
        token = lexer.token()
        self.assertEqual(lexer.lineno, 1)
        self.assertEqual(token, None)

    # Identifier names and identifiers
    def test_identifier_first_chars_are_tokenised(self):
        self._validate_identifier_char('x')
        self._validate_identifier_char('X')
        self._validate_identifier_char('$')
        self._validate_identifier_char('_')

    def test_invalid_first_char_identifier_is_not_tokenised(self):
        # identifiers can contain numbers, but not as the first char
        self._invalid_first_identifier_char('1');

    def test_non_reserved_word_identifiers(self):
        lexer.input('variable1')
        token = lexer.token()
        self.assertEqual(token.value, 'variable1')
        self.assertEqual(token.type, 'IDENTIFIER')

    def test_keywords_are_tokenised(self):

        keywords = [
            'break',
            'case',
            'catch',
            'continue',
            'debugger',
            'default',
            'delete',
            'do',
            'else',
            'finally',
            'for',
            'function',
            'if',
            'in',
            'instanceof', 
            'typeof', 
            'new', 
            'return',
            'var',
            'void', 
            'switch', 
            'while', 
            'this', 
            'with', 
            'throw',
            'try'
        ]

        for k in keywords:
            self._validate_keyword(k)

    def test_future_keywords_are_tokenised(self):

        future_keywords = [
            'class', 
            'enum', 
            'extends', 
            'super',
            'const',
            'export',
            'import'
        ]

        for k in future_keywords:
            self._validate_keyword(k)

    def test_future_strict_keywords_are_tokenised(self):

        future_strict_keywords = [
            'implements', 
            'let', 
            'private',
            'public',
            'yield',
            'interface',
            'package',
            'protected',
            'static'    
        ]

        for k in future_strict_keywords:
            self._validate_keyword(k)

    def test_punctuators_are_tokenised(self):
        self._validate_token('{', 'LBRACE')
        self._validate_token('}', 'RBRACE')
        self._validate_token('(', 'LPAREN')
        self._validate_token(')', 'RPAREN')
        self._validate_token('[', 'LBRACKET')
        self._validate_token(']', 'RBRACKET')
        self._validate_token('.', 'DOT')
        self._validate_token(';', 'SEMICOLON')
        self._validate_token(',', 'COMMA')

    def test_comparison_punctuators_are_tokenised(self):
        self._validate_token('<', 'LT')
        self._validate_token('>', 'GT')
        self._validate_token('<=', 'LTE')
        self._validate_token('>=', 'GTE')
        self._validate_token('==', 'EQUALV')
        self._validate_token('!=', 'NOTEQUALV')
        self._validate_token('===', 'EQUALVT')
        self._validate_token('!==', 'NOTEQUALVT')
    
    def test_arithmetic_punctuators_are_tokenised(self):
        self._validate_token('+', 'PLUS')
        self._validate_token('-', 'MINUS')
        self._validate_token('*', 'MULTIPLY')
        self._validate_token('%', 'MODULO')
        self._validate_token('++', 'PLUSPLUS')
        self._validate_token('--', 'MINUSMINUS')

    def test_bitwise_punctuators_are_tokenised(self):
        self._validate_token('<<', 'LSHIFT')
        self._validate_token('>>', 'RSHIFT')
        self._validate_token('>>>', 'LOGRSHIFT')
        self._validate_token('&', 'AND')
        self._validate_token('|', 'OR')
        self._validate_token('^', 'XOR')
        self._validate_token('~', 'BWNOT')

    def test_logical_punctuators_are_tokenised(self):
        self._validate_token('!', 'NOT')
        self._validate_token('&&', 'ANDAND')
        self._validate_token('||', 'OROR')
        self._validate_token('?', 'TERNARY')
        self._validate_token(':', 'COLON')

    def test_assignment_punctuators_are_tokenised(self):
        self._validate_token('=', 'EQUAL')
        self._validate_token('+=', 'PLUSEQUAL')
        self._validate_token('-=', 'MINUSEQUAL')
        self._validate_token('*=', 'MULTIPLYEQUAL')
        self._validate_token('%=', 'MODULOEQUAL')
        self._validate_token('<<=', 'LSHIFTEQUAL')
        self._validate_token('>>=', 'RSHIFTEQUAL')
        self._validate_token('>>>=', 'LOGRSHIFTEQUAL')
        self._validate_token('&=', 'ANDEQUAL')
        self._validate_token('|=', 'OREQUAL')
        self._validate_token('^=', 'XOREQUAL')

    def test_div_punctuators_are_tokenised(self):
        self._validate_token('/', 'FSLASH')
        self._validate_token('/=', 'FSLASHEQUAL')

if __name__ == '__main__':
    unittest.main()
