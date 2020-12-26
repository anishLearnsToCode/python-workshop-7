"""
if boolean_expression:
    code
    code
(optional)
elif condition_2:
    code
elif condition_3:
    code
...
...
...
(optional)
else:
    code
"""

number = int(input())
if number < 10:
    print('small number')
    print('this is puny!!!')
elif number < 20:
    print('okay number')
elif number < 30:
    print('mehhh')
elif number < 100:
    print('big number')

print('outside if else')
