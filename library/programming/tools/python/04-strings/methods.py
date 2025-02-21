print('capitalize ->', 'capitalize'.capitalize()) # Capitalize

print('LOWER ->', 'LOWER'.lower()) # lower
print('CASEFOLD ->', 'CASEFOLD'.casefold()) # casefold
# simmilar to lower() but converts more chacarters to lowercase.

print('center ->', 'center'.center(10, '#')) # ##center##

print('count o in "taboo" =', 'taboo'.count('o')) # 2

print('encode ->', 'encode'.encode())
# returns a byte encoded string with the provided encoding, default to utf-8.

print('sky ends with y =', 'sky'.endswith('y')) # True
print('sky starts with s =', 'sky'.startswith('s')) # True

print('Hello\tWorld ->', 'Hello\tWorld!'.expandtabs(2)) # Hello World!
# defines the number of whitespaces per tab.

print('l index is =', 'abcdefghijklmnopqrstuvwxyz'.find('l')) # 11
# returns -1 if values doesn't exist.
print('l index is =', 'abcdefghijklmnopqrstuvwxyz'.index('l')) # 11
# raise an exception if value doesn't exist.
print('last l index is =', 'luan lopes'.rfind('l')) # 5
# returns the last index found for the element. -1 otherwise.
print('last l index is =', 'luan lopes'.rindex('l')) # 5
# same as rfind. raises exception if values doesn't exist.

print('l0pe2 is alphanumeric =', 'l0pe2'.isalnum()) # True

print('l0pe2 is in the alphabet =', 'l0pe2'.isalpha()) # False

print('is "¨" an ascii character =', '¨'.isascii()) # False

print('"12" has only decimal characters (0-9) =', '12.1'.isdecimal()) # True
print('"12AB34" has only digits =', '12.1'.isdigit()) # False
print('"12" is numeric (0-9) =', "12.1".isnumeric())
# isdecimal() == isdigit() == isnumeric(), isdecimal() has a more consistent 
# behavior through Python versions.

print('can i use "sky" as a variable name (identifier) =',
      'sky'.isidentifier()) # True

print('is this phrase lowercase =', 'lower'.islower()) # True

print('is this\tprintable =', 'is this\tprintable'.isprintable()) # False
# special character aren't printed.

print('this string is not made only of spaces =', 'asdf'.isspace()) # False

print('["s","k","y"] ->', ''.join(['s','k','y'])) # sky
# join elements of an iterable together.
# the base string is used as separator between the elements of the provided
# iterable.

print('"1234" left aligned =', '1234'.ljust(10, "#")) # 1234######
print('"asdf" right aligned =', 'asdf'.rjust(10, "#")) # ######asdf

print('  123  =',
      '  123  '.lstrip()
               .replace(" ", "#")) # 123  $ (remove spaces from left)
print('  123  =',
      '  123  '.rstrip()
               .replace(" ", "#")) #   123$ (remove spaces from right)
print('  123   =', 
      '  123  '.strip()
               .replace(" ", "#")) # 123$ (remove spaces from both sides)

translation_table = str.maketrans('A', 'a')
print(translation_table) # {65: 97}
# returns a dict mapping a ascii code to another, thise dict will be used
# to swap character in a translation.

print('"i am starving" partitioned in "am" =', 
      'i am starving'.partition('am')) # ('i ','am',' starving')

print('"i want an apple, apples are good" rpartitioned in "apple" =',
      "i want an apple, apples are good".rpartition('apple'))
# ('i want an apple, ', 'apple', 's are good')
# same as partition but searches for the last occurrence of the word.

print('replace "banana" for "strawberry" =', 
      'banana'.replace('banana', 'strawberry')) # stawberry

print('turn str "i am starving" into a list =',
      'i am starving'.split(" ")) # ['i', 'am', 'starving']

print('turn str "i am starving" into a list =',
      'i am starving'.rsplit(" ")) # ['i', 'am', 'starving']

# basicaly rsplit() and split() have the same behavior, rsplit()
# starts from the right side of the string, but apparently returns the 
# same result as split() and in the same order.

print('1\n2\n3\nto list =', '1\n2\n3'.splitlines()) # ['1', '2', '3']

print('Swap case =', 'Swap case'.swapcase()) # sWAP CASE

print('Title this string =', 'Title this string'.title()) # Title This String

src = 'TrAnslAte this bAsed in the trAnslAte tAble ='
print(src,
      src.translate(translation_table).replace(' =', ''))
# Translate this based in the translate table

print('upper ->', 'upper'.upper())

print("pad start with 0's until width 10 =", '50'.zfill(10)) #0000000050
