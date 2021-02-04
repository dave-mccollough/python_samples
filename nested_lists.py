# Nest a list within a list to create a two dimensional data structure
# Two dimensional object has rows and columns
# 1 2 3
# 4 5 6

# To create in Python
my_matrix = [[1,2,3],[4,5,6]]
print(my_matrix)
# Returns [[1, 2, 3], [4, 5, 6]]

# To get row count
row_count = len(my_matrix)
print(row_count)
# Returns 2 - There are two rows

# To get Column count
column_count = len(my_matrix[0])
print(column_count)
# Returns 3

# To interact with a single item inside a matrix
print(my_matrix[1][2])
# returns 6

# square
# 1 2
# 3 4

# Cube
# Same number of columns as rows
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# Matrix is a list within a list