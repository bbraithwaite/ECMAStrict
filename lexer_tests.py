import unittest
from lexer import lexer

class LexerTests(unittest.TestCase):
    
    def _validate_identifier_char(self, input):
        lexer.input(input)
        token = lexer.token()
        self.assertEqual(token.value, input)
        self.assertEqual(token.type, 'IDENTIFIER')

    def _invalid_first_identifier_char(self, input):
        lexer.input(input)
        token = lexer.token()
        self.assertEqual(token, None)

    def _validate_keyword(self, keyword):
        lexer.input(keyword)
        token = lexer.token()
        self.assertEqual(token.value, keyword)
        self.assertEqual(token.type, keyword.upper())

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


if __name__ == '__main__':
    unittest.main()
