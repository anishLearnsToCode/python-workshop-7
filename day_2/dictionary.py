"""
Dictionary / HashMap / Map

variable_name = {
    key[unique]: value[not unique]
}
"""

words = {
    'i': 290,
    'am': 100,
    'batman': 67,
    'gotham': 67
}
print(words)
print(type(words))

# accessing elements
print(words['gotham'])

# get method
print(words.get('hello', 0))

# check whether key is present or not
print('i' in words)

# update values
words['batman'] = 100
print(words)

# remove a key from dict
del words['i']
print(words)
