passage = input()

"""
passage 
hello world i am so amazing i wanna learn cool stuff hello world again
[hello, world, i, am, so, amazing, i, wanna, learn, cool, stuff, hello, world, again]
result = {
    hello: 2
    world: 2
    i: 2
    am: 1
    so: 1
    amazing: 1
    wanna: 1
    learn: 1
    cool: 1
    stuff: 1
    again: 1
}
"""

# string (word) --> integer (frequency)
words = {}

for word in passage.split():
    words[word] = words.get(word, 0) + 1    # --> words[word] = word.get(word, 0) + 1

print(words)
