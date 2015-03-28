from lexer.jslexer import tokens

start = 'js'

def p_js(p):
    'js : statement js'
    p[0] = [p[1]] + p[2]

def p_js_empty(p):
    'js : '
    p[0] = [ ]

def p_statement(p):
    '''statement : block
        | variable_statement
        | empty_statement
        | if_statement
        | iteration_statement
        | expression_statement
        | break_statement
        | continue_statement
        | return_statement
        | with_statement
        | labelled_statement
        | throw_statement
        | try_statement
        | debugger_statement'''
    p[0] = p[1]

def p_statement_list(p):
    'statement_list : statement statement_list'
    p[0] = [p[1]] + p[2]

def p_statement_list_single(p):
    'statement_list : statement'
    p[0] = p[1]

def p_statement_block(p):
    'block : LBRACE statement_list RBRACE'
    p[0] = ('block', p[2])

def p_statement_block_empty(p):
    'block : LBRACE RBRACE'
    p[0] = [ ]

def p_statement_variable_statement(p):
    'variable_statement : VAR variable_declaration_list SEMICOLON'
    p[0] = p[2]

def p_statement_variable_declaration_list(p):
    'variable_declaration_list : variable_declaration COMMA variable_declaration_list'
    p[0] = [p[1]] + p[3]

def p_statement_variable_declaration_list_single(p):
    'variable_declaration_list : variable_declaration'
    p[0] = [p[1]]

def p_statement_variable_declaration(p):
    'variable_declaration : identifier'
    p[0] = p[1]

def p_statement_variable_declaration_initialiser(p):
    'variable_declaration : IDENTIFIER EQUAL exp'
    p[0] = ('identifier', p[1], p[3])

def p_statement_empty_statement(p):
    'empty_statement : SEMICOLON'
    p[0] = [ ]

def p_statement_expression_statement(p):
    'expression_statement : exp'
    p[0] = p[1]

def p_statement_if_statement(p):
    'if_statement : IF LPAREN exp RPAREN statement'
    p[0] = ('if', p[3], p[5])

def p_statement_if_else_statement(p):
    'if_statement : IF LPAREN exp RPAREN statement ELSE statement'
    p[0] = ('if-else', p[3], p[5], p[7])

def p_statement_iteration_statement_do(p):
    'iteration_statement : DO statement WHILE LPAREN exp RPAREN'
    p[0] = ('do', p[2], p[5])

def p_statement_iteration_statement_while(p):
    'iteration_statement : WHILE LPAREN exp RPAREN statement'
    p[0] = ('while', p[3], p[5])

# TODO: add for iteration statements

def p_statement_continue_statement(p):
    'continue_statement : CONTINUE SEMICOLON'
    p[0] = ('continue', [])

def p_statement_continue_statement_identifier(p):
    'continue_statement : CONTINUE identifier SEMICOLON'
    p[0] = ('continue', p[2])

def p_statement_break_statement(p):
    'break_statement : BREAK SEMICOLON'
    p[0] = ('break', [])

def p_statement_break_statement_identifier(p):
    'break_statement : BREAK identifier SEMICOLON'
    p[0] = ('break', p[2])

def p_statement_return_statement(p):
    'return_statement : RETURN SEMICOLON'
    p[0] = ('return', [])

def p_statement_return_statement_identifier(p):
    'return_statement : RETURN exp SEMICOLON'
    p[0] = ('return', p[2])

def p_statement_with_statement(p):
    'with_statement : WITH LPAREN exp RPAREN statement'
    p[0] = ('with', p[3], p[5])

# TODO: Add switch statement production

def p_statement_labelled_statement(p):
    'labelled_statement : identifier COLON statement'
    p[0] = ('labelled', p[1], p[3])

def p_statement_throw_statement(p):
    'throw_statement : THROW exp'
    p[0] = ('throw', p[2])

def p_statement_try_catch_statement(p):
    'try_statement : TRY block catch_statement'
    p[0] = ('try-catch', p[2], p[3])

def p_statement_try_finally_statement(p):
    'try_statement : TRY block finally_statement'
    p[0] = ('try-finally', p[2], p[3])

def p_statement_try_catch_finally_statement(p):
    'try_statement : TRY block catch_statement finally_statement'
    p[0] = ('try-catch-finally', p[2], p[3], p[4])

def p_statement_catch_statement(p):
    'catch_statement : CATCH LPAREN identifier RPAREN block'
    p[0] = ('catch', p[3], p[5])

def p_statement_finally_statement(p):
    'finally_statement : FINALLY block'
    p[0] = ('finally', p[2])

def p_statement_debugger_statement(p):
    'debugger_statement : DEBUGGER SEMICOLON'
    p[0] = ('debugger', [])

def p_exp_number(p): 
    'exp : NUMBER_LITERAL'
    p[0] = ("number", p[1])  

def p_exp_identifier(p): 
    'exp : identifier'
    p[0] = p[1]

def p_identifier(p):
    'identifier : IDENTIFIER'
    p[0] = ("identifier", p[1])  

def p_error(p):
    print("Syntax error at '%s'" % p.value)
