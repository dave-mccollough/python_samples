# String Slicing


my_str = 'testing'
print(my_str[0:2])
# Returns index of 0 and 1
# Returns te

# Can get indexes from middle of string
print(my_str[3:6])
# Returns tin

# Go from index to the end of the string
print(my_str[2:])
# returns sting'

# Step value
# my_str[starting_index : ending_index : step_value]
print(my_str[1:6:2])
# returns etn

# Starting with the first value
print(my_str[:6:2])
# Returns tsi

# Starting from a specific point to the end using a step vaule
print(my_str[1::2])
# returns etn

# Slicing with a negative step value reverses the screen
print(my_str[::-1])
# returns gnitset