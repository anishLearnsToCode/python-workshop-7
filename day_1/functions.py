"""
Functions

def func_name(parameter_1, parameter_2, ... paramketer=dv1, param=dv2...):
    code
    code

    return [optional] value
"""


def hello():
    print('hello')


# parameters
def full_name(first_name, last_name, middle_name=''):
    if middle_name:
        return first_name + ' ' + middle_name + ' ' + last_name
    return first_name + ' ' + last_name


# arguments
print(full_name('John', 'Wick'))
print(full_name('Ada', 'Lovelace'))
print(full_name('Wolfgang', 'Mozart', 'Amadeus'))

# named arguments
print(full_name(middle_name='Sebastian', last_name='Bach', first_name='Johanass'))

# print('hello world', end='  -----  ')
