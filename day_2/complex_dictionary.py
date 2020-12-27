complex_dict = {
    1: 'hello',
    'hello': 'world',
    'pi': 3.14,
    2.71828: 'e',
    'odd': [1, 3, 5, 7],

    'even': [2, 4, 6],
    'words': {
        'i': 100,
        'am': 200
    },
    range(1, 10): range(20),
    100: [1, 2, {
        'complex': 'OMG!!!!!'
    }]
}

# print(complex_dict['odd'])

complex_dict['odd'] += [9, 11, 13]

# print(complex_dict['odd'])

print(complex_dict[100][-1]['complex'])

complex_dict['mymy'] = 100
print(complex_dict)
