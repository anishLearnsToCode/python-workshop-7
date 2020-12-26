def factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result


# nPr = n! / (n - r)!
# 4 r=2
def permutation(n, r):
    return factorial(n) // factorial(n - r)


# nCr = nPr / r!
def combination(n, r):
    return permutation(n, r) // factorial(r)


print(combination(4, 0))
print(combination(4, 1))
print(combination(4, 2))
print(combination(4, 3))
print(combination(4, 4))
