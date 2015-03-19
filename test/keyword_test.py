import unittest
import utils
from lexer.jslexer import lexer

class KeywordTests(unittest.TestCase):

    # Comments
    def test_single_line_comment_is_ignored(self):
        lexer.input('// this is a comment')
        token = lexer.token()
        self.assertEqual(lexer.lineno, 1)
        self.assertIsNone(token)

    # Identifier names and identifiers
    def test_identifier_first_chars_are_tokenised(self):
        chars = [
            'x',
            'X',
            '$',
            '_'
        ]

        for c in chars:
            utils.validate_identifier_char(self, lexer, c)

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
            utils.validate_keyword(self, lexer, k)

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
            utils.validate_keyword(self, lexer, k)

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
            utils.validate_keyword(self, lexer, k)

if __name__ == '__main__':
    unittest.main()