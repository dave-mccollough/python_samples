# List Functions

my_list = [1, 2, 3]

# To append an item to the end of the list
my_list.append(4)
print(my_list)
# Returns [1, 2, 3, 4]

# To insert to the middle of a list
# my_list.insert(position we want to insert at, item)
my_list.insert(2, 'hello')
print(my_list)
# adds 'hello' to the second index
# Returns [1, 2, 'hello', 3, 4]

# To find the index of an object in the list
print(my_list.index('hello'))
# Returns 2


# To check if a value in a list

# item_your_checking for in my list
print(5 in my_list)
# Returns False

# item_your_checking for not in my list
print(5 not in my_list)
# Returns True

# Sorting
# Use the sorted method

my_new_list = [1, 8, 9, 14, 7]
sorted(my_new_list)
print(sorted(my_new_list))
# Returns [1, 7, 8, 9, 14]

# It doesn't change the list
print(my_new_list)
# Returns [1, 8, 9, 14, 7]

# To reversed a list
# use the reversed and list methods
# List changes this back into a list

list(reversed(my_new_list))

print(list(reversed(my_new_list)))


# To sort a list in reverse order
list(reversed(sorted(my_new_list)))
print(list(reversed(sorted(my_new_list))))
# Return [14, 9, 8, 7, 1]