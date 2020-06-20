# Section 04-3
# list, tuples, indexing, slicing
    # making data storage comfortable, efficient, and compact
    # LIFO: last in first out
    

# LIST
# list: order, duplicate, modify, delete


# declaring a list
l1 = []
l2 = list('cheeseburger')
l3 = [1, 2, 3, 4]
l4 = [10, 100, 'non', 'integers']
l5 = ['a', 'list', ['within', 'a', 'list']]
    # list() : changes a string into a list of the components in the string 
print(l2)
    # lists can have both integers and strings
print(l4)
    # list inside list
print(l5)
print()


# indexing
print(l4[3])
print(l4[2])
    # integers and strings cannot be attached
print(l4[2] + l4[3])
# print(l4[1] + l4[4])
    # returning a component inside a list of a list
print(l5[2][2])
print(l5[-1][-1])
print()


# slicing
print(l4[0:-1])
print(l5[::-1])
    # take caution of the numerical position
print(l5[:-1])
print(l5[-2:-1])
print()


# list operation
    # addition
    # adds lists into a single list
print(l2 + l3)
    # multiplication
    # extends the list n times
print(l3 * 3)
    # string + integer
    # str() for numerals
print(l2[0] + 'hi')
print(str(l3[0]) + 'hi')
print()


# list modify and delete
    # modify a specific index
print(l3)
l3[0] = 9
print(l3)
    # modify a slicing of a list
print(l2)
l2[1:3] = ['n', 'o', 'n']
print(l2)
    # nesting: changing one index into a list
l3[0] = ['l', 'i', 's', 't']
print(l3)
print()


# deleting an index or slicing
    # deleting an index
del l3[0]
print(l3)
    # deleting a slicing
del l2[0:7]
print(l2)
print()


# list operations
"""
        # note the difference for .append() - list is nested into for .extend() - list is extended into a single list
    .append()    adding to the end
    .insert(x, y)   adding y value to index x
    .pop()          deleting the last index
    .index()     finding the index of a specific component (returns error if nonexistent)
        # note that for del - delete a specific index, for .remove() - delete a specific value
    .remove()    removes 'a' (only the first)
    .extend(otherList)  inserting a list inside a list
    .sort()         sorts the list into increasing value
    .reverse()      reversing the indexes
    .count('c')
"""
z = [1, 4, 6, 4, 3]
z.append(0)
print(z)

z.pop()
print(z)

z.sort()
print(z)

z.reverse()
print(z)

z.insert(2, 8)
print(z)

z.remove(8) 
print(z)

print(z.count(1))

ex = [2, 2]
# z.extend(ex)
# z.append(ex)
print(z)

print()



# TUPLE
# tuple: order, duplicate, modify x, delete x


# declaring a tuple
t1 = ()
t2 = (1,)
t3 = (1, 2, 3, 4)
t4 = (10, 100, ('a', 'b', 'c'))
    
    # cannot use del, .pop(), .remove()
# del t3[0]


# indexing
print(t3[2])
print(t4[2])
print(t4[2][2])
print()


# slicing
print(t3[2:])
print(t4[2][0:1])
print()


# operations
    # addition
print(t3 + t4)
    # multiplication
print(t3 * 3)
print()


# tuple functions
print(t3)
print(3 in t3)
print(t3.index(3))
print(t3.count(1))
print()