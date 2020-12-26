"""
Factorial
N! = 1 * 2 * 3 * ... * N
0! = 1! = 1
"""

n = int(input())

result = 1
i = 1

# result = 15
# i = 4
while i <= n:
    result *= i
    i += 1

print(result)

"""
input: 3

"""

