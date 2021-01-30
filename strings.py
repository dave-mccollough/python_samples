# Strings

# Single Quoted String - String Literal
my_str = 'single quoted string'
print(my_str)
# returns single quoted string

# Double Quoted String 
my_str = "double quoted string"
print(my_str)
# returns double quoted string

# Multiline Strings
my_str = '''This is a 
multiline string'''
print(my_str)
# returns This is a 
# multiline string


# Operations

# plus(+) operator
# concatenate a string
my_str = "pass" + "word"
print(my_str)
# returns password

# Multiplication(*) operator
# Mulptiples string by numeric value
my_str = "Ha" * 4
print(my_str) 
# Returns HaHaHaHa
# Also works in the reverse
my_str = 4 * "Ha"
# Returns HaHaHaHa

# Objects
# Encapsulates State and Behavior
# In a string, state is the sequence of characters
# Behavior is the functionality tied to string
# This is demostrated using methods 

# This is the find method
my_str = "this is a string"
print(my_str.find('t'))
# Returns 0 since 't' is the first letter of the string

#this is the lower() method
my_str = ("THIS IS A STRING").lower()
print(my_str)
# returns: this is a string

# To add a tab to a string
print("Tab\tDelimted")
# Returns Tab     Delimted

# To add a new line to a string
print("New\nLine")
# Returns 
# Line

# Single Quoted String inside double quoted string
my_str = "'single quoted string'"
print(my_str)
# Returns 'single quoted string'

# Double Quoted String inside single quoted string
my_str = '"single quoted string"'
print(my_str)
# Returns "double quoted string"



# Errors
# Start with a single or double quote and end with same
