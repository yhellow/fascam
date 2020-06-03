# Section02-1

# print basics
print('hello printer')
print("hello printer")
print("""hello printer""")
print('''hello printer''')
    # output is the same
print()
    # if nothing is inserted, works as a new line (\n)


# separator
print('p', 'r', 'i', 'n', 't')
print('p', 'r', 'i', 'n', 't', sep= '')
    # separator gives a preferred value between the objects
print('2020', '01', '01', sep= '')
print('2020', '01', '01', sep= '.')
    # can put in any str value
print('someonesemail', 'gmail.com', sep= '@')
print()


# end
print('welcome to', end= ' ')
print('the black paradise', end= ' ')
print('in light')
    # doesn't end with the new line command but rather ends with the inserted end object
print()


# format
    # formats in order
print('{} and {}'.format('like', 'subscribe'))
    # place orders on the objects = mapping
print('please {0} and {1} if you {0}d the video'.format('like', 'subscribe'))
    # place placeholders for objects
print('please {a} and {b} for more related videos'.format(a= 'like', b= 'subscribe'))
    # using %s:string / %d:decimal / %f:float
print('today\'s the %s of june and it is %d degrees outside with %.2f%% humidity'%('first', 28, 10))
    # must have equal number of % values 
    # use backslash to avoid ending strings when using '' or "" within the string
    # use %% for percentage use


