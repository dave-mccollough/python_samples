# String Indexing

# Zero based index
# Last character is always length -1 (You can use the Len function for this)
my_str = 'testing'
print(id(my_str))
# ID 4361673968
my_other_string = my_str[4]
# Returns a new string i
print(id(my_other_string))
# 4361182000

# How to get last letter in string
last_value = my_str[len(my_str) - 1]
print(last_value)
# Returns g

# Get last letter using negative indexing
print(my_str[-1])
# Returns g





