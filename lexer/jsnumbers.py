from ply.lex import TOKEN

"""
7.8.3 Numeric Literals

DecimalLiteral ::
    DecimalIntegerLiteral . DecimalDigits (opt) ExponentPart (opt)
    DecimalIntegerLiteral ExponentPart (opt)

DecimalIntegerLiteral :: 
    0
    NonZeroDigit DecimalDigits (opt)

"""

hex_digit_re            = r'[0-9a-fA-F]'  
hex_integer_literal_re  = r'0[x|X]' + hex_digit_re + '+'

@TOKEN(hex_integer_literal_re)
def t_NUMBER_hex_integer_literal(t):
    t.type = 'NUMBER'
    mv = 0 # mathematical value
    for hex_digit in t.value[2:]:
        mv = mv * 16
        if hex_digit.isdigit():
            mv += int(hex_digit)
        elif hex_digit.upper() == 'A':
            mv += 10
        elif hex_digit.upper() == 'B':
            mv += 11
        elif hex_digit.upper() == 'C':
            mv += 12
        elif hex_digit.upper() == 'D':
            mv += 13
        elif hex_digit.upper() == 'E':
            mv += 14
        elif hex_digit.upper() == 'F':
            mv += 15

    t.value = mv
    return t

decimal_digit_re            = r'[0-9]'
decimal_digits_re           = r'[0-9]+'
non_zero_digit_re           = r'[1-9]'
decimal_integer_literal_re  = '0|({NonZeroDigit}{DecimalDigit}*)'.format(NonZeroDigit=non_zero_digit_re, DecimalDigit=decimal_digit_re)
exponent_indicator_re       = r'[eE]'
signed_integer_re           = r'[-+]?{DecimalDigits}'.format(DecimalDigits=decimal_digits_re)
exponent_part_re            = '({ExponentIndicator}{SignedInteger})'.format(ExponentIndicator=exponent_indicator_re, SignedInteger=signed_integer_re)
decimal_literal_re          = '({DecimalIntegerLiteral}\.({DecimalDigits})?{ExponentPart}?)|(\.{DecimalDigits}{ExponentPart}?)|({DecimalIntegerLiteral}{ExponentPart}?)'.format(DecimalIntegerLiteral=decimal_integer_literal_re, DecimalDigits=decimal_digits_re, ExponentPart=exponent_part_re)

@TOKEN(decimal_literal_re)
def t_NUMBER_decimal_literal(t):
    t.type = 'NUMBER'
    t.value = float(t.value)
    return t
