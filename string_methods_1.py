# String Methods

# You can append string methods to the end of strings

'This'.lower()
print('This'.lower())
# Returns this

my_str = 'TeSTiNG STriNg'

#.lower()
my_str.lower()
print(my_str.lower())
# Returns testing string

#.upper()
my_str.upper()
print(my_str.upper())
# Returns TESTING STRING

#.capitalize()
# Capitalize the first letter and lowercase the rest
my_str.capitalize()
print(my_str.capitalize())
# Returns Testing string


# .title()
# Capitalize the first letter of each unique word
my_title = 'this is the title of my new book'
my_title.title()
print(my_title.title())
# Returns This Is The Title Of My New Book


# Checking string contents for patterns

# Checking if all values can be returned as ascii
my_str.isascii()
print(my_str.isascii())
# Returns True

# Checking if all values are capitalized
my_str.isupper()
print(my_str.isupper())
# Returns False

# You can chain string methods
my_str.title().istitle()
print(my_str.title().istitle())
# Returns True

# Check for spaces
my_space = ' '
my_space.isspace()
print(my_space.isspace())
# Returns True

# isdecimal()
# isdigit()
# isnumeric()
# If the string you are working with only contains numbers, these should return true.  If they include decimals or floats, they will return false

# isalpha()
my_str.isalpha()
# checks if all characters in string are alphabetical

# isalnum()
my_str.isalnum()
# checks if characters in string are alpha numeric

# isidentifier()
# checks if string could be used as a variable or constant
'1bear'.isidentifier()
# returns false

'word'.isidentifier()
# Returns true since it could be used as a identifier

# isprintable()
# checks if the string can be printed.  If a escape character exixts it will return false


