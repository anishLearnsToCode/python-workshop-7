def square_str(x):
    y = int(x)
    return y ** 2


# map(func, iterable)
numbers = list(map(square_str, input().split()))
print(numbers)
print(type(numbers))
