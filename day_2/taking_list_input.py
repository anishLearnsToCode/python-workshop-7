numbers = input()
numbers = numbers.split()

# convert every item from str --> integer
for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

print(numbers)
print(type(numbers))
