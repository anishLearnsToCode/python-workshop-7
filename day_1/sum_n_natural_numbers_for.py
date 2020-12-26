"""
f(N) = 1 + 2 + 3 + ... + N
f(0) = 0
f(1) = 1
"""

n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)
