# import unittest
# import lexer.jslexer
# import parser.jsparser

# import ply.yacc as yacc
# import ply.lex as lex

# lexer = lex.lex(module=lexer.jslexer)
# parser = yacc.yacc(module=parser.jsparser)

# class AssigmentTest(unittest.TestCase):
#     def test_variable_number(self):
#         parse_tree = parser.parse("var foo = 1;", lexer=lexer)
#         self.assertEquals(parse_tree, [('var', 'foo', ('number', 1.0))])

#     def test_variable_string(self):
#         parse_tree = parser.parse("var foo = 'bar';", lexer=lexer)
#         self.assertEquals(parse_tree, [('var', 'foo', ('string', 'bar'))])

#     def test_variable_identifier(self):
#         parse_tree = parser.parse("var foo = bar;", lexer=lexer)
#         self.assertEquals(parse_tree, [('var', 'foo', ('identifier', 'bar'))])     

#     def test_variable_boolean_true(self):
#         parse_tree = parser.parse("var foo = true;", lexer=lexer)
#         self.assertEquals(parse_tree, [('var', 'foo', ('boolean', 'true'))])

#     def test_variable_boolean_false(self):
#         parse_tree = parser.parse("var foo = false;", lexer=lexer)
#         self.assertEquals(parse_tree, [('var', 'foo', ('boolean', 'false'))])

#     def test_variable_assignment(self):
#         parse_tree = parser.parse("var foo = 1;foo = 3;", lexer=lexer)
#         self.assertEquals(parse_tree, [
#             ('var', 'foo', ('number', 1.0)),
#             ('assign', 'foo', ('number', 3.0))
#         ])


# # TODO: these should be parser tests

# # def test_with_decimal_and_digits_cannot_start_with_multiple_zeros(self):
# #      utils.assertTokensAreNone(self, lexer, ['00.01'])

# # def test_with_decimal_and_digits_and_exponent_cannot_start_with_multiple_zeros(self):
# #     utils.assertTokensAreNone(self, lexer, ['00.0e1'])

# # def test_with_decimal_and_exponent_cannot_start_with_multiple_zeros(self):
# #     utils.assertTokensAreNone(self, lexer, ['00.e1'])

# # def test_with_integer_and_exponent_cannot_start_with_multiple_zeros(self):
# #     utils.assertTokensAreNone(self, lexer, ['00e1'])

# # def test_with_decimal_integer_literal_cannot_start_with_multiple_zeros(self):
# #     utils.assertTokensAreNone(self, lexer, ['00'])

# # def test_with_decimal_integer_literal_exponent_cannot_start_with_multiple_zeros(self):
# #     utils.assertTokensAreNone(self, lexer, ['00e1'])
