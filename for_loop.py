

# for TEMP_VAR in SEQUENCE:

# Iterate through a list
colors = ['blue', 'green', 'red', 'purple']

for color in colors:
    print(color)


# Iterate through a tuple
points = (1, 2, 3)
for point in points:
    print(point)

# Iterate through dictionary
# Dictionaries return the key by default.  To get the value
ages = {'Kevin' : 60, 'Bob' : 49, 'Jerry' : 23}
for key in ages:
    print(key)

# To iterate through both the key and the value
for key,value in ages.items():
    print(f'{key} is {value} years old')


# Iterate through a string
for letter in 'my string':
    print(letter)

