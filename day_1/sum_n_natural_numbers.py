"""
N
1 + 2 + 3 + ... + N
0: 0
1: 1
2: 3
"""

n = int(input()) # 0
result = 0
i = 1

while i <= n:
    result += i
    i += 1

print(result)
