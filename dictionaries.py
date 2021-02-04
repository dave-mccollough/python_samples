# Dictionaries

# Dictionaries have a key and value
# Keys should be immutable types
# Each key has to be unique
# Dictionaries are mutable types and can be added to

ages = { 'Kevin' : 59, 'Alex' : 37, 'Bob' : 40}
print(ages)
# Returns {'Kevin': 59, 'Alex': 37, 'Bob': 40}

# Use the key to get the value
print(ages['Kevin'])
# Returns 59

# To add a key/value to a dictionary
ages['Jen'] = 48
print(ages)
# returns {'Kevin': 59, 'Alex': 37, 'Bob': 40, 'Jen': 48}

# To reassign a key/value
ages['Kevin'] = 60
print(ages)
# Returns {'Kevin': 60, 'Alex': 37, 'Bob': 40, 'Jen': 48}

# To delete a key/value
del ages['Kevin']
print(ages)
# Returns {'Alex': 37, 'Bob': 40, 'Jen': 48}

# del ages would remove the entire variable

# To check if key exists
'Kevin' in ages
print('Kevin' in ages)
# Returns False

'Alex' in ages
print('Alex' in ages)
# Returns True

# Ways to create a dictionary
#Using the dict function
weights = dict(Joe=160, Jerry=210, Kim=125)
print(weights)
# Returns {'Joe': 160, 'Jerry': 210, 'Kim': 125}

# Using Tuples
colors = dict([('Kevin', 'Blue'), ('Bob', 'Green'), ('Heather', 'Red')])
print(colors)
# Returns {'Kevin': 'Blue', 'Bob': 'Green', 'Heather': 'Red'}

# To get all keys in method, use the keys() method
ages_2 = { 'Kevin' : 59, 'Alex' : 37, 'Bob' : 40}
print(ages_2.keys())
# Returns dict_keys(['Kevin', 'Alex', 'Bob'])

# To cast keys into a list
ages_list = list(ages_2.keys())
print(ages_list)
# Returns ['Kevin', 'Alex', 'Bob']

# To get all values in method, use the values() method
print(ages_2.values())
# returns dict_values([59, 37, 40])

# To cast values into a list
ages_list = list(ages_2.values())
print(ages_list)
# Returns [59, 37, 40]

# To return dictionary as a list of tuples
weights = dict(Joe=160, Jerry=210, Kim=125)
print(weights.items())
# Returns dict_items([('Joe', 160), ('Jerry', 210), ('Kim', 125)])

# .items will give you key and value
# .value will give you value
# .key will give you just the key

