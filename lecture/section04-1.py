# Section04
# data types and math operations

"""
    1. boolean
    2. number
    3. string (sequence)
    4. bytes
    5. list (sequence)
    6. tuple (sequence)
    7. set
    8. dictionary
        bytearray
        byte
        frozenset
"""

# variable_datatype
v_boo = False
v_float = 6.6
v_str1 = "string"
v_str2 = "cheese"
v_int = 9
v_list = [3, 5, 7]
v_tuple = 2, 4, 6
v_set = {1, 0, 9}
v_dict = {
    "key": "value",
    "here": "insert this"
}
    # type() is a command that gives the data type
print(type(v_boo))
print(type(v_float))
print(type(v_str1))
print(type(v_str2))
print(type(v_int))
print(type(v_list))
print(type(v_tuple))
print(type(v_set))
print(type(v_dict))
print()


#  operations e.g.
#  python math: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
i1 = 29
i2 = 929
bigi1 = 3333333333
bigi2 = 4444444444
f1 = 1.21312
f2 = 4.43141
f3 = .1231
f4 = 10.
    # multiply
print(i1 * i2)
print(bigi1 * bigi2)
    # division
    # / v // v %
print(10/3)
print(10//3)
print(10%3)
    # squared
print(f1 ** f2)
    # integer + float = float
print(f3 + i2)
    # int() on floats deletes decimal points
print(int(f3))
    # float() on integers adds '0.' at the front
print(float(f3))
    # floats include '.0' at the end for integers
print(float(f4))
print(int(f4))
print()
    # checking..
f3i2 = f3 + i2
print(f3i2)
def isfloat(x):
    if type(x) == float:
        print("yes")
    else:
        print("no")
    return
isfloat(f3i2)
    # for print(funcResult) python returns 'None' at the end
print(isfloat(f3i2))
print()


# changing data types
# int(), float(), complex()
a = 1.
b = 2
c = 3
print(type(a), type(b))
fint = a + b
print(fint)
print(type(fint))
    # from '9.0' to '9' v '9' to '9.0'
print(int(fint))
print(float(c))
    # int to complex
print(complex(b))
    # boolean as integers
    # False == 0 / True == 1
    # !! has to have capital first letter
print(int(False))
print(int(True))
    # string to integer
print(int('4'))
    # '0' as complex
print(complex(False))
print()


# repeatable operations
"""
    y = 100
    y = y + 100
    is equal to:
    y += 100
"""
    # !! operation comes before '=' 
y = 100
y = y + 100
print(y)
x = 100
x += 100
print(x)
print()


# complex operations
"""
    abs(x): absolute value or magnitude of x
    complex(re, im): a complex number with real part re, imaginary part im. im defaults to zero
    .conjugate(): conjugate of the complex number c
    divmod(x, y): the pair (x // y, x % y)
    pow(x, y): x to the power y
"""

# divmod()
dm = divmod(100,9)
    # as combination
print(dm)
    # as separate numbers
n, m = dm
print(n, m)
print()


# math module
import math
    # math.ceil(x): integer that is smallest but bigger than x
print(math.ceil(5.1))
    # math.floor(x): integer that is largest but smaller than x
print(math.floor(5.1))
print()

