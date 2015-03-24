import ply.lex as lex
import unittest
import utils
import lexer.jslexer

lexer = lex.lex(module=lexer.jslexer)

class KeywordTests(unittest.TestCase):

    def test_single_line_comment_is_ignored(self):
        lexer.input('// this is a comment')
        token = lexer.token()
        self.assertEqual(lexer.lineno, 1)
        self.assertIsNone(token)

    def test_identifier_first_chars_are_tokenised(self):
        tokens = [
            ('x', 'IDENTIFIER'),
            ('X', 'IDENTIFIER'),
            ('$', 'IDENTIFIER'),
            ('_', 'IDENTIFIER'),
            ('\u0000', 'IDENTIFIER'),
            ('x\u0000', 'IDENTIFIER'),
            ('x0', 'IDENTIFIER'),
            ('x-', 'IDENTIFIER'),
            ('x_', 'IDENTIFIER'),
            ('x_-0a\u0000', 'IDENTIFIER'),
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_non_reserved_word_identifiers(self):
        utils.validate_token(self, lexer, 'variable1', 'IDENTIFIER')

    def test_keywords_are_tokenised(self):
        tokens = [
            ('break', 'BREAK'),
            ('case', 'CASE'),
            ('catch', 'CATCH'),
            ('continue', 'CONTINUE'),
            ('debugger', 'DEBUGGER'),
            ('default', 'DEFAULT'),
            ('delete', 'DELETE'),
            ('do', 'DO'),
            ('else', 'ELSE'),
            ('finally', 'FINALLY'),
            ('for', 'FOR'),
            ('function', 'FUNCTION'),
            ('if', 'IF'),
            ('in', 'IN'),
            ('instanceof', 'INSTANCEOF'), 
            ('typeof', 'TYPEOF'),
            ('new', 'NEW'),
            ('return', 'RETURN'),
            ('var', 'VAR'),
            ('void', 'VOID'),
            ('switch', 'SWITCH'),
            ('while', 'WHILE'),
            ('this', 'THIS'),
            ('with', 'WITH'),
            ('throw', 'THROW'),
            ('try', 'TRY')
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_future_keywords_are_tokenised(self):
        tokens = [
            ('class', 'CLASS'),
            ('enum',  'ENUM'),
            ('extends', 'EXTENDS'),
            ('super', 'SUPER'),
            ('const', 'CONST'),
            ('export', 'EXPORT'),
            ('import', 'IMPORT')
        ]

        utils.assertTokenList(self, lexer, tokens)

    def test_future_strict_keywords_are_tokenised(self):
        tokens = [
            ('implements', 'IMPLEMENTS'),
            ('let', 'LET'),
            ('private', 'PRIVATE'),
            ('public', 'PUBLIC'),
            ('yield', 'YIELD'),
            ('interface', 'INTERFACE'),
            ('package', 'PACKAGE'),
            ('protected', 'PROTECTED'),
            ('static', 'STATIC')
        ]

        utils.assertTokenList(self, lexer, tokens)
