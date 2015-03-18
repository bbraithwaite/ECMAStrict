# TODO: temp place for shared assertion methods
def validate_token(self, lexer, value, typeName):
    lexer.input(value)
    token = lexer.token()
    self.assertEqual(token.value, value)
    self.assertEqual(token.type, typeName)

def validate_identifier_char(self, lexer, value):
    validate_token(self, lexer, value, 'IDENTIFIER')

def invalid_first_identifier_char(self, lexer, input):
    lexer.input(input)
    token = lexer.token()
    self.assertIsNone(token)

def validate_keyword(self, lexer, keyword):
    validate_token(self, lexer, keyword, keyword.upper())