import random

a, b = -100, 100

# print(int((b - a) * random.random() + a))

x, y = random.randint(a, b), random.randint(a, b)
print(x)
print(y)

"""
(0, 1)
(0, b - a)
(0, b - a) + a
(a, b - a + a)
(a, b)
"""
