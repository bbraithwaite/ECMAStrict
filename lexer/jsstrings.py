from ply.lex import TOKEN

"""
7.8.4 String Literals

StringLiteral ::
'SingleStringCharacters (opt) '

SingleStringCharacters ::
    SingleStringCharacter SingleStringCharacters (opt)

SingleStringCharacter ::
    SourceCharacter but not one of ' or \ or LineTerminator 
    \ EscapeSequence
    LineContinuation

LineContinuation ::
    \ LineTerminatorSequence

LineTerminatorSequence :: 
    <LF>
    <CR> [lookahead must be <LF> ] 
    <LS>
    <PS>
    <CR> <LF>
"""

line_continuation_re   = r'\\(\r\n|\n|\r)'
double_string_re       = r'"(([^"\\\n\r]+)|{LineContinuation})*"'.format(LineContinuation=line_continuation_re)
single_string_re       = r"'(([^'\\\n\r]+)|{LineContinuation})*'".format(LineContinuation=line_continuation_re)

@TOKEN(double_string_re)
def t_STRING_double_quotes(t):
    t.type = 'STRING_LITERAL'
    t.value = t.value[1:-1] # remove the encasing quotes
    return t

@TOKEN(single_string_re)
def t_STRING_single_quotes(t):
    t.type = 'STRING_LITERAL'
    t.value = t.value[1:-1] # remove the encasing quotes
    return t