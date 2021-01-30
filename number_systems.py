# Number Systems

# There's more than one way to represent a number

# Decimal:  15
# Binary: 1111

# Number systems are specified by the base number
# Decimal is base 10: 0-9
# binary is base 2: 0-1
# Octal is base 8: 0-7
# Hexadecimal is base 16: 0 - F (0 - 9 + A - F)


# To convert Binary to decimal, use 0b prefix
my_num = 0b101
print(my_num)
# Returns 5


# To convert Octal to decimal, use 0o prefix
my_num = 0o7242
print(my_num)
# Returns 3746

# To convert Hexadecimal to decimal, use 0x prefix
my_num = 0xFF012
print(my_num)
# Returns 1044498

# Converting the Decimal value 15 to binary
# Divide the decimal number by the base of the system we want to convert it into
# binary has a base of 2, so divide 15 / 2
# 15 / 2 = 7 with a remainder of 1
# Continue to divide the result till you reach 0
# 7 / 2 = 3 with a remainder of 1
# 3 / 2 = 1 with a remainder of 1
# 1 / 2 = 0 with a remainder of 1

# The binary result is 1111

