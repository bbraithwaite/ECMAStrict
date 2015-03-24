from lexer.jslexer import tokens

start = 'js'

def p_js(p):
    'js : statement js'
    p[0] = [p[1]] + p[2]

def p_js_empty(p):
    'js : '
    p[0] = [ ]

def p_statement_var(p):
    'statement : VAR IDENTIFIER EQUAL exp SEMICOLON'
    p[0] = ('var', p[2], p[4])

def p_statement_assign(p):
    'statement : IDENTIFIER EQUAL exp SEMICOLON'
    p[0] = ('assign', p[1], p[3])

def p_exp_number(p): 
    'exp : NUMBER_LITERAL'
    p[0] = ("number", p[1])     

def p_exp_string(p): 
    'exp : STRING_LITERAL'
    p[0] = ("string", p[1])

def p_exp_identifier(p): 
    'exp : IDENTIFIER'
    p[0] = ("identifier", p[1])

def p_exp_boolean(p): 
    'exp : BOOLEAN_LITERAL'
    p[0] = ("boolean", p[1])

def p_error(p):
    print("Syntax error at '%s'" % p.value)
