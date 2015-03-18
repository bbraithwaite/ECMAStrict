#
# OTHER TODO: choose better name, as design evolves
#
other = (
    'IDENTIFIER',
)


#
# The following tokens are ECMAScript keywords and may not be used as Identifiers in ECMAScript programs.
#
keywords = (
    'BREAK',            # break
    'CASE',             # case
    'CATCH',            # catch
    'CONTINUE',         # continue
    'DEBUGGER',         # debugger
    'DEFAULT',          # default
    'DELETE',           # delete
    'DO',               # do
    'ELSE',             # else
    'FINALLY',          # finally
    'FOR',              # for
    'FUNCTION',         # function
    'IF',               # if
    'IN',               # in
    'INSTANCEOF',       # instanceof
    'TYPEOF',           # typeof
    'NEW',              # new
    'RETURN',           # return
    'VAR',              # var
    'VOID',             # void
    'SWITCH',           # switch
    'WHILE',            # while
    'THIS',             # this
    'WITH',             # with
    'THROW',            # throw
    'TRY'               # try
)

#   The following words are used as keywords in proposed extensions 
#   and are therefore reserved to allow for the possibility of 
#   future adoption of those extensions. 
future_keywords = (
    'CLASS',            # class
    'ENUM',             # enum
    'EXTENDS',          # extends
    'SUPER',            # super
    'CONST',            # const
    'EXPORT',           # export
    'IMPORT'            # import
)

#   The following tokens are also considered to be FutureReservedWords 
#   when they occur within strict mode code.
#   NB this parser defaults to strict mode.
future_strict_keywords = (
    'IMPLEMENTS',       # implements
    'LET',              # let
    'PRIVATE',          # private
    'YIELD',            # yield
    'PUBLIC',           # public
    'INTERFACE',        # interface
    'PACKAGE',          # package
    'PROTECTED',        # protected
    'STATIC'            # static
)

#
#   Punctuators
#
punctuators = (
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