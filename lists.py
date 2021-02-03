# List type

# List is a comma seperated collection of other items
# Lists are mutable and can be modified
# list items can be different types
# Lists are 0 based
my_list = [1, 2.0, 'strings', False]
print(my_list)
# returns [1, 2.0, 'strings', False]

# To get items from a list, use indexing
# T0 get the first item from a list
print(my_list[0])
# returns 1

# Slicing
print(my_list[0:2])
# Returns a list:  [1, 2.0]

# step values work as well
print(my_list[0:4:2])
# Returns [1, 'strings']

# Modify the list in place
my_list[1] = 'another string'
print(my_list)
# Returns [1, 'another string', 'strings', False]

# Adding to list
print(my_list + [8, 9, 10])
# returns [1, 'another string', 'strings', False, 8, 9, 10]
# my_list is unchanged though
print(my_list)
# Returns [1, 'another string', 'strings', False]

# Create a new list and reassign it
my_list += [8, 9, 10]
print(my_list)
# Returns [1, 'another string', 'strings', False, 8, 9, 10]

# Use slicing to reassign list values
my_list[1:2] = [7, 12]
print(my_list)
# Returns [1, 7, 12, 'strings', False, 8, 9, 10]

# if you need to reinsert items into a certain part of a list
my_list[3:5] = [7, 12, 'insert', True]
print(my_list)
# Returns [1, 7, 12, 7, 12, 'insert', True, 8, 9, 10]


# Remove items from a list
my_list = ['a', 'b', 'c', 1, 2, 3, False]
# if we want to remove everything after c
my_list[3:] = []
print(my_list)
# Returns ['a', 'b', 'c']

