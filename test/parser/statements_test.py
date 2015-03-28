import unittest
import lexer.jslexer
import parser.jsparser

import ply.yacc as yacc
import ply.lex as lex

lexer = lex.lex(module=lexer.jslexer)
parser = yacc.yacc(module=parser.jsparser)

class StatementsTest(unittest.TestCase):
    def test_block_statement_empty(self):
        parse_tree = parser.parse("{}", lexer=lexer)
        self.assertEquals(parse_tree, [[]])

    def test_block_statement_with_list(self):
        parse_tree = parser.parse("{ var foo = 1; }", lexer=lexer)
        self.assertEquals(parse_tree[0], ('block', [('identifier', 'foo', ('number', 1.0))]))

    def test_variable_statement_single(self):
        parse_tree = parser.parse("var foo;", lexer=lexer)
        self.assertEquals(parse_tree[0], [('identifier', 'foo')])

    def test_variable_statement_multiple(self):
        parse_tree = parser.parse("var foo,bar,baz;", lexer=lexer)
        self.assertEquals(parse_tree[0], [('identifier', 'foo'), ('identifier', 'bar'), ('identifier', 'baz')])

    def test_variable_statement_initialiser(self):
        parse_tree = parser.parse("var foo = 1;", lexer=lexer)
        self.assertEquals(parse_tree[0], [('identifier', 'foo', ('number', 1.0))])

    def test_empty_statement_initialiser(self):
        parse_tree = parser.parse(";", lexer=lexer)
        self.assertEquals(parse_tree[0], [])

    def test_expression_statement(self):
        parse_tree = parser.parse("foo;", lexer=lexer)
        self.assertEquals(parse_tree[0], ('identifier', 'foo'))

    def test_if_statement(self):
        parse_tree = parser.parse("if (foo) bar", lexer=lexer)
        self.assertEquals(parse_tree[0], ('if', ('identifier', 'foo'), ('identifier', 'bar')))

    def test_if_else_statement(self):
        parse_tree = parser.parse("if (foo) bar else baz", lexer=lexer)
        self.assertEquals(parse_tree[0], ('if-else', ('identifier', 'foo'), ('identifier', 'bar'), ('identifier', 'baz')))

    def test_iteration_statement_do(self):
        parse_tree = parser.parse("do foo while (bar)", lexer=lexer)
        self.assertEquals(parse_tree[0], ('do', ('identifier', 'foo'), ('identifier', 'bar')))

    def test_continue_statement(self):
        parse_tree = parser.parse("continue;", lexer=lexer)
        self.assertEquals(parse_tree[0], ('continue', []))

    def test_continue_statement_identifier(self):
        parse_tree = parser.parse("continue foo;", lexer=lexer)
        self.assertEquals(parse_tree[0], ('continue', ('identifier', 'foo')))

    def test_break_statement(self):
        parse_tree = parser.parse("break;", lexer=lexer)
        self.assertEquals(parse_tree[0], ('break', []))

    def test_break_statement_identifier(self):
        parse_tree = parser.parse("break foo;", lexer=lexer)
        self.assertEquals(parse_tree[0], ('break', ('identifier', 'foo')))

    def test_return_statement(self):
        parse_tree = parser.parse("return;", lexer=lexer)
        self.assertEquals(parse_tree[0], ('return', []))

    def test_return_statement_identifier(self):
        parse_tree = parser.parse("return foo;", lexer=lexer)
        self.assertEquals(parse_tree[0], ('return', ('identifier', 'foo')))

    def test_with_statement(self):
        parse_tree = parser.parse("with (foo) bar", lexer=lexer)
        self.assertEquals(parse_tree[0], ('with', ('identifier', 'foo'), ('identifier', 'bar')))

    def test_labelled_statement(self):
        parse_tree = parser.parse("foo : bar", lexer=lexer)
        self.assertEquals(parse_tree[0], ('labelled', ('identifier', 'foo'), ('identifier', 'bar')))

    def test_throw_statement(self):
        parse_tree = parser.parse("throw foo;", lexer=lexer)
        self.assertEquals(parse_tree[0], ('throw', ('identifier', 'foo')))

    def test_try_catch_statement(self):
        parse_tree = parser.parse("try { foo } catch (bar) { baz }", lexer=lexer)
        self.assertEquals(parse_tree[0], ('try-catch', ('block', ('identifier', 'foo')), ('catch', ('identifier', 'bar'), ('block', ('identifier', 'baz')))))

    def test_try_finally_statement(self):
        parse_tree = parser.parse("try { foo } finally { bar }", lexer=lexer)
        self.assertEquals(parse_tree[0], ('try-finally', ('block', ('identifier', 'foo')), ('finally', ('block', ('identifier', 'bar')))))

    def test_try_catch_finally_statement(self):
        parse_tree = parser.parse("try { foo } catch (bar) { baz } finally { qux }", lexer=lexer)
        self.assertEquals(parse_tree[0], ('try-catch-finally', ('block', ('identifier', 'foo')), ('catch', ('identifier', 'bar'), ('block', ('identifier', 'baz'))), ('finally', ('block', ('identifier', 'qux')))))

    def test_debugger_statement(self):
        parse_tree = parser.parse("debugger;", lexer=lexer)
        self.assertEquals(parse_tree[0], ('debugger', []))

