# Section02-1
# basic grammar practice

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
    # must have equal number of % values 
    # use backslash to avoid ending strings when using '' or "" within the string
    # use %% for percentage use
print('today\'s the %s of june and it is %d degrees outside with %.2f%% humidity'%('first', 28, 10))
    # digit space before decimal is not overrided but after decimal point is overrided
    # if the number given is smaller than the assigned digit space, it takes up blank space
    # if the number after the assigned digit space is >= 5 it is automatically rounded up
print("today is %d degrees celsius and %2.2f degrees farenheit outside" %(0, 0))
print("today is %1d degrees celsius and %2.2f degrees farenheit outside" %(0, 0.0001))
print("today is %2d degrees celsius and %2.2f degrees farenheit outside" %(0, 0.004))
    # using "key"s
print("today is {0: 3d} degrees celsius and {1: 1.2f} degrees farenheit outside".format(0, 0))
print("today is {a: 3d} degrees celsius and {b: 1.2f} degrees farenheit outside".format(a= 0, b= 0))
print()


# escape
"""
    \n : new line
    \t : new tab
    \\ : string
    \' : string
    \" : string
    \r : carriage return
    \f : f-string
    \a : bell sound
    \b : backspace
    \000 : null
"""
    # '' inside '' is invalid syntax. instead use '' inside ""
    # single apostrophe gets recognized as string
print("'singles inside doubles'")
    # if singles have to be used outside use the escape
print('\'singles inside singles\'')
    # "" inside '' works 
    # if the apostrophes are different the inside gets recognized as string
print('"doubles inside singles"')
    # as long as they're differentiated
print("""'singles inside threes'""")
print('''"doubles inside threes"''')
    # backslashes act as escapers that help the python compiler understand the next codes as string 
    # print already has a default new line command so by adding \n at the end results in two new lines
print('what\'s\nnext\\\n')
print('what\'s\nnext\\\n\n')
print('one or two new lines?')
    # tabs
print('\t\thighlight the hidden tabs')
print()