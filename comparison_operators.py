# Comparison Operators

# Less than
print(1 < 2)
# Returns True

# Greater than
print(2 > 1)
# Returns True

# Greater than or equal
print(2 >= 1)
# Returns True

# Less than or equal
print(2 <= 1)
# Returns False

# Converts from floats to integers
print(2.0 > 3)
# Returns False

# Comparing letters - uses letter value in alphabet.
# you can get letter value by using ord() functions

print(ord('a'))
# Returns 97
print(ord('b'))
# Returns 98

print('a' > 'b')
# Returns False

print('b' > 'a')
# Returns True

# Everything is an object in Python
# Make sure you are comparing same types


# To validate if items are equal, use ==
print(1 == 1)
# Returns True


# To validate if items are no equal, use !=
print(1 != 1)
# Returns False


# To validate if items are the exact same object, use 'is'
print(1 is 2) 
# Returns False

print('a' is 'a') 
# Returns True

print(1 is 1.0) 
# Returns False since these are two different objects

# Use 'is not' to validate to exactly different objects
print (1 is not 1) 
# Returns False
print (1 is not 'a')
# Returns True 


# To see memory location of Python object, use the id() function
print(id('a'))
# returns 4483965744
# The 'is' and 'is not' functions compare id('a') == id('a') or id('a') != id('a')