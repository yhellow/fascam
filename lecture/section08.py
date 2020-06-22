# Section08
# modules & packages


# directory path
    # .     current directory
    # ..    parent directory


# IMPORT 1
from pkg.fibonacci import Fibonacci
# from folder.file import class
Fibonacci.fib1(300)
print('1: ', Fibonacci.fib2(400))
print('1: ', Fibonacci().title)         # Fibonacci(): make instance


# IMPORT 2
    # import all packages 
from pkg.fibonacci import *
print('2: ', Fibonacci.fib2(800))


# IMPORT 3
    # making alias for the package
from pkg.fibonacci import Fibonacci as fb
print('3: ', fb.fib2(1000))


# IMPORT 4
import pkg.calculations as c
print('4: ', c.add(10, 100))
print('4: ', c.mul(20,2))
print('4: ', c.div(20,2))


# IMPORT 5
from pkg.calculations import div as d
print('5: ', int(d(100,10)))


# IMPORT 6
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))                # printout directory of builtins