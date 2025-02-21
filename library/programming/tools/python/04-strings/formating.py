# Formated strings literals / F-strings:
# Lets you include the value of Python expressions inside a string 
# by prefixing the string with f or F and writing expresions as {expression}.
# An optional format specifier can follow the expression.

# Format specification Mini-Language:
# format_spec     ::=  [[fill]align]
#                      [sign] ["z"] ["#"] ["0"]
#                      [width]
#                      [grouping_option]
#                      ["." precision]
#                      [type]

# fill            ::=  <any character> defaults to space

# align           ::=  "<" | 
#                      ">" | 
#                      "=" | - can be used to expand an expression to the 
#                              text of the expression.
#                      "^"
# Note that unless a minimum field width is defined, the field width will 
# always be the same size as the data to fill it.

# prints positive_value surouded by $ until reaches length 10.
print(f'{1:$^10}') 

# sign            ::=  "+" | - sign should be used for all numbers.
#                      "-" | - (default) sign should be used for negative 
#                              numbers.
#                      " " - leading space for positive numbers, minus sign
#                            on negative numbers

# prints positive_value with a leading space as it's positive.
print(f'{1: }')

# 'z'             ::= In Python, there is a distinction between positive 
#                     zero (0) and negative zero (-0). The z option in the 
#                     format specification is used to normalize negative 
#                     zero values to positive zero when formatting numbers.
#                     This option is only valid for floating numbers.

# prints negative floating-point zero without negative sign.
print(f'{-0.0:z}')

# '#'             ::= it activates the "alternate form" of formatting for 
#                     integers, floats, and complex numbers.
#                     For integers, if the number is not decimal based 
#                     prepend the number with its base system.

#prints decimal number 10 in base octal with base prefix.
print(f'{10:#o}')

# width           ::=  digit+
# Is a decimal integer defining the minimum total field width, including 
# any prefixes, separators, and other formatting characters. If not 
# specified, then the field width will be determined by the content.

# align different width text to a same width at the right.
print(f'{"align this":>20}')
print(f'{"align those":>20}')

# grouping_option ::=  "_" | - uses underscore for thousands separator.
#                      "," - uses comma for thousands separator.

# replace thousands separator by an underscore.
print(f'{1000:_}')

# precision       ::=  digit+
# The precision is a decimal integer indicating how many digits should be 
# displayed after the decimal point for presentation types 'f' and 'F', or 
# before and after the decimal point for presentation types 'g' or 'G'. For 
# string presentation types the field indicates the maximum field size - in 
# other words, how many characters will be used from the field content. The 
# precision is not allowed for integer presentation types.

# prints only 2 characters from the string
print(f'{"cat":.2}')

# type            ::=  "b" | - binary format. outputs number in base 2.
print(f'{10:b}') # converts 10 to binary.
#                      "c" | - character. converts integers to corresponding
#                              character before printing.
print(f'{65:c}') # converts 65 to its ASCII character.
#                      "d" | - decimal integer. outputs number in base 10.
print(f'{0xa:d}') # converts a hex value to its decimal form.
#                      "e" | - scientific notation. It represents a 
#                              floating-point number in the form 
#                              a.bbbbbe+/-xx, where a is the coefficient, 
#                              bbbbb are the significant digits, e indicates 
#                              scientific notation, and xx is the exponent.
print(f'{0.0312:e}') # prints floating-point number with scientif notation.
#                      "E" | - same as 'e' but uses 'E' as separator.
print(f'{0.0312:E}') # prints floating-point number with scientif notation.
#                      "f" | - fixed point notation. For a given precision p
#                              formats the number as a decimal number with 
#                              exactly p digits following the decimal point.
print(f'{0.123456:.2f}') # print float number with 2 digits precision.
#                      "F" | - same as 'f' but uses NAN for nan and INF
#                              for inf.
print(f'{float("nan"):.2F}') # print nan with upper case.
#                      "g" | - general format. For a given precision p >= 1, 
#                              this rounds the number to p significant digits 
#                              and then formats the result in either 
#                              fixed-point format or in scientific notation, 
#                              depending on its magnitude.
#                              For floating-point numbers, if its scientific
#                              notation exponent is bigger than 4, displays 
#                              as scientific-notation, floating-point
#                              otherwise. For decimal representation, if the
#                              number has more than 6 digits, displays it as
#                              scientific-notation.
#                              Positive and negative infinity, positive and 
#                              negative zero, and nans, are formatted as 
#                              inf, -inf, 0, -0 and nan respectively
print(f'{0.000012:g}') # print float number as scientific-notation.
#                      "G" | - general format. Same as 'g' except switches 
#                              to 'E' if the number gets too large. The 
#                              representations of infinity and NaN are 
#                              uppercased, too.
print(f'{1234567:G}') # print big number with scientific-notation.
#                      "n" | - number. Same as 'g', except that it uses the
#                              current locale setting to insert the
#                              appropriate number separator characters.
#                      "o" | - octal format. Outputs number in base 8.
print(f'{10:o}') # print 10 in base 8.
#                      "s" | - (default) format to string.
print(f'{10}') # print 10 as a string.
#                      "x" | - hex format. Outputs number in base 16, using
#                              lower case letters.
print(f'{10:x}') # print 10 in base 16.
#                      "X" | - hex format. Outputs number in base 16, using
#                              upper case letters.
print(f'{10:X}') # print 10 in base 16. Using uppercase letters.
#                      "%" - percentage. Multiplies the number by 100 and
#                            displays in 'f' format, followed by a percent
#                            sign.
print(f'{0.05:.2%}') # print float 0.05 as percentage with precision 2.
