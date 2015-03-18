import ply.lex as lex 
from tokens import *

punctuators = (
    punctuators + 
    punctuators_assignment + 
    punctuators_arithmetic + 
    punctuators_bitwise + 
    punctuators_conditional + 
    punctuators_comparison + 
    punctuators_logical + 
    div_punctuators
)

tokens = (
    other + 
    keywords + 
    future_keywords + 
    future_strict_keywords + 
    punctuators
)

def t_single_line_comment(t):
    # Only single line comments are supported
    r'^//.*'
    pass

def t_IDENTIFIER(t):
    # identifiers must start with:
    #   UnicodeLetter (a-zA-Z in this example, for simplicity)
    #   $
    #   _ (underscore)
    #   \ UnicodeEscapeSequence (although supported in this project)
    # subsequent chars can be:
    #   Same as initial letter
    #   Unicode digit (0-9)
    #   (Other unicode chars are possible but not supported)
    r'[a-zA-Z$_][a-zA-Z$_0-9]*'
    v = t.value.upper() 
    if v in keywords:
        t.type = t.value.upper()

    if v in future_keywords:
        t.type = t.value.upper()
        
    if v in future_strict_keywords:
        t.type = t.value.upper()

    return t

# punctuators
t_LBRACE        = r'{'
t_RBRACE        = r'}'
t_LPAREN        = r'\('
t_RPAREN        = r'\)'
t_LBRACKET      = r'\['
t_RBRACKET      = r'\]'
t_DOT           = r'\.'
t_SEMICOLON     = r';'
t_COMMA         = r','

# comparison
t_LT            = r'<'
t_GT            = r'>'
t_LTE           = r'<='
t_GTE           = r'>='
t_EQUALVT       = r'==='
t_NOTEQUALVT    = r'!==' 
t_EQUALV        = r'==' 
t_NOTEQUALV     = r'!='

# arithmetic  
t_PLUSPLUS      = r'\+\+'
t_MINUSMINUS    = r'--'
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_MULTIPLY      = r'\*'
t_MODULO        = r'%'

# bitwise
t_LSHIFT        = r'<<'
t_RSHIFT        = r'>>'
t_LOGRSHIFT     = r'>>>'
t_AND           = r'&'
t_OR            = r'\|'
t_XOR           = r'\^'
t_BWNOT         = r'~'

# logical
t_NOT           = r'!'
t_ANDAND        = r'&&'
t_OROR          = r'\|\|'
t_TERNARY       = r'\?'
t_COLON         = r':'

# assignment
t_EQUAL         = r'='
t_PLUSEQUAL     = r'\+='
t_MINUSEQUAL    = r'-='
t_MULTIPLYEQUAL = r'\*='
t_MODULOEQUAL   = r'%='
t_LSHIFTEQUAL   = r'<<='
t_RSHIFTEQUAL   = r'>>='
t_LOGRSHIFTEQUAL = r'>>>='
t_ANDEQUAL      = r'&='
t_OREQUAL       = r'\|='
t_XOREQUAL      = r'\^='

# div punctuators
t_FSLASH        = r'/'
t_FSLASHEQUAL   = r'/='

t_ignore    = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)    

# Build the lexer
lexer = lex.lex()