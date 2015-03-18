import ply.lex as lex 

tokens = (
    'IDENTIFIER',       # identifier
    # Keywords
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
    'TRY',              # try
    # Future Keywords
    'CLASS',            # class
    'ENUM',             # enum
    'EXTENDS',          # extends
    'SUPER',            # super
    'CONST',            # const
    'EXPORT',           # export
    'IMPORT',           # import
    # Future Strict Keywords
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

def t_single_line_comment(t):
    # Only single line comments are supported
    r'^//.*'
    pass

#   The following tokens are ECMAScript keywords and may not be 
#   used as Identifiers in ECMAScript programs.
keywords = [
    'break', 
    'case', 
    'catch', 
    'continue', 
    'debugger', 
    'default', 
    'delete', 
    'do',
    'else', 
    'finally',
    'for',
    'function',
    'if',
    'in',
    'instanceof',
    'typeof',
    'new',
    'return',
    'var', 
    'void',
    'switch',
    'while',
    'this',
    'with',
    'throw',
    'try'
]

#   The following words are used as keywords in proposed extensions 
#   and are therefore reserved to allow for the possibility of 
#   future adoption of those extensions.  
future_keywords = [
    'class', 
    'enum', 
    'extends', 
    'super',
    'const',
    'export',
    'import'
]

#   The following tokens are also considered to be FutureReservedWords 
#   when they occur within strict mode code.
#   NB this parser defaults to strict mode.
future_strict_keywords = [
    'implements', 
    'let', 
    'private',
    'public',
    'yield',
    'interface',
    'package',
    'protected',
    'static'    
]

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
    if t.value in keywords:
        t.type = t.value.upper()

    if t.value in future_keywords:
        t.type = t.value.upper()
        
    if t.value in future_strict_keywords:
        t.type = t.value.upper()

    return t

t_ignore                = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)    

# Build the lexer
lexer = lex.lex()