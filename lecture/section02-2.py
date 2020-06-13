# Section02-2
# basic coding practice


# python philosophy
# import this
print()


# os
import os
print(os.getcwd)
print()


# python basic encoding
# "env": {
#       "PYTHONIOENCODING": "UTF-8"
#   }
import sys
# input
print(sys.stdin.encoding)
# output
print(sys.stdout.encoding)
# platform
print(sys.platform)
print()


# print statement
print('printout statement')
print()


# variable
thisfile = 'coding practice'
print(thisfile)
print()


# conditional statement
if thisfile == 'coding practice':
    print('it is')
print()


# repeat statement
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' %(i,j), i*j)
print()


# function 
def hi():
    print("hello")
hi()
print()    


# class
# == class cookie():
class cookie: 
    pass


# create object (객체)
cookie = cookie()
print(id(cookie))
print(dir(cookie))
print()

