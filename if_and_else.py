
# If/else
if 'a' > 'b':
    print("It's still true!")
else:
    print("It's flalse now")    


# if/elif
if 'a' > 'b':
    print("First condition is true")
elif 'c' < 'd':
    print("Second condition is true")    
else:
    print("No condition is true")    


# Conditionals

name = input('What is your name? ')
if len(name) >= 6:
    print('Your name is long')
elif len(name) == 5:
    print('Your name is 5 characters long.')
elif len(name) >= 4:
    print('Your name is 4 or more characters')
else:
    print('Your name is short')


# Pass 
# Pass does nothing
name = 'Keith'
if name == 'Kevin':
    print('Hello Kevin')
else:
    pass