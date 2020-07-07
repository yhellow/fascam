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



# SET
# set: order X, duplicate X, modify O, delete O
    # can use indexing or slicing after changing data type


# declaring set
s1 = set()
s2 = set([1, 2, 3, 4])
s3 = set([1 ,4, 5 , 6, 6])
s4 = set([5, 6, 7, 8])
s5 = {'cannon', 'be', 'empty'}
    # empty {} are recognized as dictionaries
    # no duplicates
print(s3)
    # changing sets into tuples or lists
ts2 = list(s2)
ts3 = tuple(s3)
print(ts2)
print(ts3)
print()


# set functions
    # 교집합
print(s2.intersection(s3))
print(s2.intersection(s4))
print(s2 & s3)
print(s2 & s4)
    # 합집합
print(s2.union(s3))
print(s2.union(s4))
print(s2 | s3)
print(s2 | s4)
    # 차집합
    # a.difference(b) : a-b
print(s2.difference(s3))
print(s3.difference(s2))
print(s2 - s3)
print(s3 - s2)
print()

# add and remove
    # add
    # duplicate is automatically filtered
s2.add(0)
s2.add(4)
print(s2)
    # update: add more than one
s2.update([6, 7, 8])
print(s2)
    # remove
s2.remove(0)
print(s2)
print()