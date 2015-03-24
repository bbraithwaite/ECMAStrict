from jsnumbers import hex_digit_re
from ply.lex import TOKEN

variable = (
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

#
# The following words are used as keywords in proposed extensions and are therefore reserved to allow for 
# the possibility of future adoption of those extensions. 
#
future_keywords = (
    'CLASS',            # class
    'ENUM',             # enum
    'EXTENDS',          # extends
    'SUPER',            # super
    'CONST',            # const
    'EXPORT',           # export
    'IMPORT'            # import
)

#
# The following tokens are also considered to be FutureReservedWords when they occur within strict mode code.
#
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
#   Literals (7.8)
#
literal_keywords = (
    'NULL',             # null
    'TRUE',             # true
    'FALSE',            # false
    'NUMBER',           # number literal
    'STRING'            # string literal
)

"""
IdentifierName :: 
    IdentifierStart
    IdentifierName IdentifierPart

IdentifierStart :: 
    UnicodeLetter
    $
    _
    \ UnicodeEscapeSequence


IdentifierPart :: 
    IdentifierStart
    UnicodeCombiningMark 
    UnicodeDigit 
    UnicodeConnectorPunctuation 
    <ZWNJ>
    <ZWJ>
"""
unicode_letter_re                = r'[a-zA-Z]'  # TODO: extend with all values for unicode letter categories
unicode_digit_re                 = r'[0-9]'     # TODO: extend with all values for unicode digit
unicode_connector_punctuation_re = r'[-_]'      # TODO: extend with all values for unicode connectors

unicode_escape_sequence_re       = r'u{HexDigit}{HexDigit}{HexDigit}{HexDigit}' \
                                        .format(HexDigit=hex_digit_re)

identifier_start_re              = r'{UnicodeLetter}|[$_]|(\\{UnicodeEscapeSequence})' \
                                        .format(UnicodeLetter=unicode_letter_re, \
                                                UnicodeEscapeSequence=unicode_escape_sequence_re)

identifier_part_re               = r'{IdentifierStart}|{UnicodeDigit}|{UnicodeConnectorPunctuation}' \
                                        .format(IdentifierStart=identifier_start_re, \
                                                UnicodeDigit=unicode_digit_re, \
                                                UnicodeConnectorPunctuation=unicode_connector_punctuation_re)

identifier_name                  = r'({IdentifierStart})({IdentifierPart})*' \
                                        .format(IdentifierStart=identifier_start_re, \
                                                IdentifierPart=identifier_part_re)

@TOKEN(identifier_name)
def t_IDENTIFIER(t):
    v = t.value.upper() 
    if v in keywords:
        t.type = t.value.upper()

    if v in future_keywords:
        t.type = t.value.upper()
        
    if v in future_strict_keywords:
        t.type = t.value.upper()

    if v in literal_keywords:
        t.type = t.value.upper()

    return t
