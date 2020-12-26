"""
While Loop

while condition:
    code
    code

condition (true) --> code --> condition (true) --> code --> condition (true) --> code --> condition (false) --> exit loop
"""

# infinite loop
# while True:
#     print('Hello World')

i = 0
while i < 5:
    print(i)
    i += 1 # i = i + 1

"""
output
0
1
2
3
4
"""

print('i am outside loop')
