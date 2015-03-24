import re

"""
Hex Integer Literal
"""
def t_NUMBER_hex(t):
    r'0[x|X][0-9a-fA-F]+'
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

"""
Decimal Literal

***Note:*** Regex can be condensed. Separate for now to correspond with spec grammar.

"""
def t_NUMBER_integer_literal_exponent(t):
    # DecimalIntegerLiteral ExponentPart
    r'[0-9]+[eE](-|\+)?[0-9]+'

    if check_single_leading_zero(t):
        leading_zero_error(t)
        return None

    t.type = 'NUMBER'
    t.value = float(t.value)
    return t

def t_NUMBER_decimal_integer_literal_digits_exponent(t):
    # DecimalIntegerLiteral . DecimalDigits ExponentPart
    r'[0-9]+\.[0-9]+[eE](-|\+)?[0-9]+'

    if check_single_leading_zero(t):
        leading_zero_error(t)
        return None

    t.type = 'NUMBER'
    t.value = float(t.value)
    return t

def t_NUMBER_decimal_integer_literal_exponent(t):
    # DecimalIntegerLiteral . ExponentPart
    r'[0-9]+\.[eE](-|\+)?[0-9]+'

    if check_single_leading_zero(t):
        leading_zero_error(t)
        return None

    t.type = 'NUMBER'
    t.value = float(t.value)
    return t

def t_NUMBER_decimal_integer_literal_digits(t):
    # DecimalIntegerLiteral . DecimalDigits
    r'[0-9]+\.[0-9]*'

    if check_single_leading_zero(t):
        leading_zero_error(t)
        return None

    t.type = 'NUMBER'
    t.value = float(t.value)
    return t

def t_NUMBER_integer_literal(t):
    # DecimalIntegerLiteral    
    r'[0-9]+'

    if check_single_leading_zero(t):
        leading_zero_error(t)
        return None

    t.type = 'NUMBER'
    t.value = float(t.value)
    return t

def leading_zero_error(t):
    print("'%s' has unexpected number" % t.value)
    t.lexer.skip(1) 

def check_single_leading_zero(t):
    # invalid decimal e.g. 00.01
    return re.match('0[0-9]+', t.value)
