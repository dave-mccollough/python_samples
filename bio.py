name = input("What is your name? " )
color = input("What is your favorite color? " )
age = int(input("How old are you today? ")) # This is going to be a number so it can be typecasted 


# Using the end= operator
# Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’, i.e. the new line character. 
# You can end a print statement with any character/string using this parameter.
print(name, end=" ")
print("is " + str(age) + " years old", end="@ ")
print("and loves the color " + color + ".", end=" &")
# Returns Dave is 47 years old@ and loves the color Blue. &


# Using the sep= operator
# Print statement is sperated by commas then the ser argument
print(name, 'is', age, 'years old and loves the color', color, '.', sep=' ')
# Returns Dave is 47 years old and loves the color Blue. 
print(name, 'is', age, 'years old and loves the color', color, '.', sep='/')
# Dave/is/47/years old and loves the color/Blue/.

# return NAME is AGE years old and loves the color COLOR
print(f"{name} is {age} years old and loves the color {color}.")