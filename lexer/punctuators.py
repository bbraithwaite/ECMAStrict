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