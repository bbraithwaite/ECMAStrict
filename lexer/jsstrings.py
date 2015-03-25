from jsnumbers import hex_digit_re
from ply.lex import TOKEN

"""
7.8.4 String Literals
"""

line_terminator_sequence_re = r'(\r\n|\n|\r)'
single_escape_character_re  = r'[\'\"\\bfnrtv]'
non_escape_character_re     = r'[^\'\"\\bfnrtv0-9xu\n\r]'

hex_escape_sequence_re      = r'x{HexDigit}{HexDigit}'\
                                    .format(HexDigit=hex_digit_re)

unicode_escape_sequence_re  = r'u{HexDigit}{HexDigit}{HexDigit}{HexDigit}'\
                                    .format(HexDigit=hex_digit_re)

character_escape_sequence_re = r'{SingleEscapeCharacter}|{NonEscapeCharacter}'\
                                    .format(SingleEscapeCharacter=single_escape_character_re,
                                        NonEscapeCharacter=non_escape_character_re)

escape_sequence_re          = r'{UnicodeEscapeSequence}|{HexEscapeSequence}'\
                                    .format(CharacterEscapeSequence=character_escape_sequence_re,
                                        HexEscapeSequence=hex_escape_sequence_re,
                                        UnicodeEscapeSequence=unicode_escape_sequence_re)

line_continuation_re        = r'\\{LineTerminatorSequence}'\
                                    .format(LineTerminatorSequence=line_terminator_sequence_re)

double_string_characters_re = r'"(([^"\\\n\r]+)|(\\{EscapeSequence})|{LineContinuation})*"'\
                                     .format(LineContinuation=line_continuation_re,
                                         EscapeSequence=escape_sequence_re)

single_string_characters_re = r"'(([^'\\\n\r]+)|(\\{EscapeSequence})|{LineContinuation})*'"\
                                     .format(LineContinuation=line_continuation_re,
                                         EscapeSequence=escape_sequence_re)

@TOKEN(double_string_characters_re)
def t_STRING_literal_double(t):
    t.type = 'STRING_LITERAL'
    t.value = t.value[1:-1] # remove the encasing quotes
    return t

@TOKEN(single_string_characters_re)
def t_STRING_literal_single(t):
    t.type = 'STRING_LITERAL'
    t.value = t.value[1:-1] # remove the encasing quotes
    return t
