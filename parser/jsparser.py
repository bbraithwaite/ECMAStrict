from lexer.jslexer import tokens

start = 'exp'

def p_exp_indentifier(p):
    'exp : IDENTIFIER'
    p[0] = ("identifier",p[1]) 

def p_error(p):
    print("Syntax error at '%s'" % p.value)
