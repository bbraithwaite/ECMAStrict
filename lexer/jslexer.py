from jsidentifiers import *
from jsnumbers import *
from jsstrings import *

#
#   Punctuators (7.7)
#
punctuators_symbols = (
    'LBRACE',           # {
    'RBRACE',           # }
    'LPAREN',           # (
    'RPAREN',           # )
    'LBRACKET',         # [
    'RBRACKET',         # ]
    'DOT',              # .
    'SEMICOLON',        # ;
    'COMMA'             # ,
)

punctuators_arithmetic = (
    'PLUS',             # +
    'MINUS',            # -
    'MULTIPLY',         # *
    'MODULO',           # %
    'PLUSPLUS',         # ++
    'MINUSMINUS'        # --
)
    
punctuators_assignment = (
    'EQUAL',            # =
    'PLUSEQUAL',        # +=
    'MINUSEQUAL',       # -=
    'MULTIPLYEQUAL',    # *=
    'MODULOEQUAL',      # %=
    'LSHIFTEQUAL',      # <<=
    'RSHIFTEQUAL',      # >>=
    'LOGRSHIFTEQUAL',   # >>>=
    'ANDEQUAL',          # &=
    'OREQUAL',          # |=
    'XOREQUAL'          # ^=
)

punctuators_bitwise = (
    'LSHIFT',           # <<
    'RSHIFT',           # >>
    'LOGRSHIFT',        # >>>
    'AND',              # &
    'OR',               # |
    'XOR',              # ^
    'BWNOT',            # ~
)

punctuators_comparison = (
    'LT',               # <
    'GT',               # >
    'LTE',              # <=
    'GTE',              # >=,
    'EQUALV',           # ==  (value, with type coercion)
    'NOTEQUALV',        # !=  (value, with type coercion)
    'EQUALVT',          # === (value and type)
    'NOTEQUALVT'        # !== (value and type)
)

punctuators_conditional = (
    'TERNARY',          # ?
    'COLON'             # :
)

punctuators_logical = (
    'ANDAND',           # &&,
    'NOT',              # !
    'OROR',             # ||
)

div_punctuators = (
    'FSLASH',           # /
    'FSLASHEQUAL'       # /=
)

tokens = (
    variable + 
    keywords + 
    future_keywords + 
    future_strict_keywords + 
    punctuators_symbols + 
    punctuators_assignment + 
    punctuators_arithmetic + 
    punctuators_bitwise + 
    punctuators_conditional + 
    punctuators_comparison + 
    punctuators_logical + 
    div_punctuators +
    literal_keywords
)

def t_single_line_comment(t):
    r'^//.*'
    pass

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
