# Section04-4
# dictionary, set


# DICTIONARY
# dictionary: order X, duplicate X, modify O, delete O
    # key & value (json)
    # key + value = item


# declaring a dictionary
d1 = {}
d2 = {'name': 'chandler', 'number': '1111-1111', 'height': 178}
d3 = {0: 'keys', 1: 'are', 2: 'usually', 3: 'non-numerical'}
d4 = {'arr': [1, 2, 3, 4, 5]}
    # dictionary values can include strings, integers, lists, tuples


# indexing
    # directly returning the value
print(d2['name'])
print(d2.get('name'))

    # using .get()
    # prevents keyerror for if the key doesn't exist (returns none instead of error()
# print(d2['birthday'])
print(d2.get('birthday'))

    # slicing the list inside the value of a key
print(d4['arr'][0:2])
print()


# adding a key value
d2['address'] = 'monica\'s house'
print(d2)

d2['seasons'] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(d2)

d2['episodes'] = (1, 2, 'etc')
print(d2)
print()


# key / value / item
    # comes out LOOKING LIKE a list format

# key
print(d2.keys())
print(list(d2.keys()))
keys = list(d2.keys())
print(keys[0:3])

# value
print(d2.values())
print(list(d2.values()))
values = list(d2.values())
print(values[0:3])

# item
print(d2.items())
    # comes out as tuples nested in a list
print(list(d2.items()))
items = list(d2.items())
print(items[0:3])
print()


# dictionary functions
print(1 in d3)
print(1 in d2)
print(1 not in d3)
print(1 not in d2)
print()