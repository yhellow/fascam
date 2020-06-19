# Section04
# data types

"""
    1. boolean
    2. number
    3. string
    4. bytes
    5. list
    6. tuple
    7. set
    8. dictionary
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


