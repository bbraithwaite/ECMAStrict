from jsidentifiers import identifier_part_re
from ply.lex import TOKEN

"""
7.8.5 Regular Expression Literals
"""

reg_ex_backslash_sequence_re = r'\\[^\n\r]'

reg_ex_flags_re         = r'({IdentifierPart})*'\
                            .format(IdentifierPart=identifier_part_re)

reg_ex_class_char_re    = r'[^\n\r\]\\]|{RegularExpressionBackslashSequence}'\
                            .format(RegularExpressionBackslashSequence=reg_ex_backslash_sequence_re)

reg_ex_class_re         = r'\[({RegularExpressionClassChar})*\]'\
                            .format(RegularExpressionClassChar=reg_ex_class_char_re)

reg_ex_char_re          = r'[^/\\\[\n\r]|{RegularExpressionBackslashSequence}|{RegularExpressionClass}'\
                            .format(RegularExpressionBackslashSequence=reg_ex_backslash_sequence_re,
                                    RegularExpressionClass=reg_ex_class_re)

reg_ex_chars_re         = r'({RegularExpressionChar})*'\
                            .format(RegularExpressionChar=reg_ex_char_re)

reg_ex_first_char_re    = r'[^\*/\\\[\n\r]|{RegularExpressionBackslashSequence}|{RegularExpressionClass}'\
                            .format(RegularExpressionClass=reg_ex_class_re,
                                    RegularExpressionBackslashSequence=reg_ex_backslash_sequence_re)

reg_ex_body_re          = r'({RegularExpressionFirstChar}){RegularExpressionChars}'\
                            .format(RegularExpressionFirstChar=reg_ex_first_char_re,
                                    RegularExpressionChars=reg_ex_chars_re)

reg_ex_literal_re       = r'/({RegularExpressionBody})/{RegularExpressionFlags}'\
                            .format(RegularExpressionBody=reg_ex_body_re,
                                    RegularExpressionFlags=reg_ex_flags_re)

@TOKEN(reg_ex_literal_re)
def t_REGEX_literal(t):
    t.type = 'REGEX_LITERAL'
    return t