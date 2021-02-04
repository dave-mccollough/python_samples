# Strings can be tokens

# .split()
phrase = 'This is a simple phrase'
words = phrase.split()
print(words)

# Split on character
url = 'https://example.com/users/dave'
user = url.split('/')
print(user)
# Splits in '/' character
# Returns the last item in the list

# .join()
url = 'https://example.com/users/dave'
user = url.split('/')
print('/'.join(user))

# .format()
template = "Hello, my name is {}, and I really enjoy {}.  Have a nice day!"
my_str = template.format('Dave', 'Python')
print(my_str)
# returns Hello, my name is Dave, and I really enjoy Python.  Have a nice day!


template_2 = "Hello, my name is {0}, and I really enjoy {1}.  Have a nice day!".format('Dave', 'Golang')
print(template_2)
# Returns Hello, my name is Dave, and I really enjoy Golang.  Have a nice day!