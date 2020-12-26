"""
N
1^2 + 2^2 + 3^2 + .... + N^2
"""

n = int(input())

result = 0
i = 1

while i <= n:
    result += i ** 2
    i += 1

print(result)
