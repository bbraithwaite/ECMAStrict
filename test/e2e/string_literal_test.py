# """
# End-to-end tests using lexer, parser and interpreter for String literals.
# """

# import unittest
# import lexer.jslexer as jslexer
# import parser.jsparser as jsparser
# import interpreter.jsinterpreter as jsinterpreter

# import ply.yacc as yacc
# import ply.lex as lex

# lexer = lex.lex(module=jslexer)
# parser = yacc.yacc(module=jsparser)

# class StringLiteralTest(unittest.TestCase):
#     def test_number_assignment(self):
#         with open ("test/e2e/string-literal-fixture.js", "r") as jsFile:
#             parse_tree = parser.parse(jsFile.read(), lexer=lexer)
#             env = jsinterpreter.interpret(parse_tree)
#             expected = {
#             	'unicodeEscape': 'I love JavaScript to \u221e and beyond', 
#             	'lineContinuation': 'hello\\\nworld'
#             }
#             self.assertEquals(env, expected)
