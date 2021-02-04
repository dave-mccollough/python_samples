# Tuples are created using parantheses delimited by a comma
# Tuples are an immutable type
# Tuples have a fixed length and can't be changed once created

point = (1.0, 2.0)

# To add item to tuple:
point_3d = point + (3.0,)
# Make sure you include the trailing comma

# If you want to break up or unpack a tuple
x, y, z = point_3d
print(x)
# Returns 1.0 since it's the first item in the list
print(y)
# Returns 2.0 since it's the second item in the list
print(z)
# Returns 3.0 since it's the third item in the list


# You can use tuples instead of a list if you know the data never going to change and will always be a specific size
# for example, if you have a person variable and it will always contain three objects:  name, age, phone number
person = ('Joe Smith', 47, '555-555-1234')

# You can imbed lists in tuples and tuples in lists
my_list = [1, 2, 3]
my_tuple = (my_list, 1)
print(my_tuple)
# returns ([1, 2, 3], 1)
other_list = [1,2, my_tuple]
print(other_list)
# Returns [1, 2, ([1, 2, 3], 1)]