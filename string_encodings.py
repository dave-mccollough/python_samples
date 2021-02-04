# Python String Encoding

# Unicode UTF-8
# UTF - Unicode Transformation Format
# 8 Values are stored in 8 bits

# to return unicode integer/code points of string character use ord function
ord('A') 
print(ord('A'))
# Returns 65

# Trademark character
ord('™')
print(ord('™'))
# Returns 8482

# ASCII
# Older format that can only handle letters, numnbers and punctuation
# Extended ASCII can hold 256 code points

# If we write something in Hexadecimal, Python will always return integer
print(0x2122)
# Returns 8482


# Shorthand for Unicode
ord('\u2122')
print('\u2122')
# Returns trademark symbol ™


# Convert Unicode to String
chr(8482)
print(chr(8482))
# Returns trademark symbol ™

# Use ord to convert to unicode
# Use chr to convert from unicode to string