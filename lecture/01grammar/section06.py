# Section06
# function, lambda


# FUNCTION
    # makes modifications easy
    # less repetition for same task
    # one function for one task


# declaring function
def funcName(parameter):
    if parameter == 'para':
        pass
    # code


# using function
funcName('para')


# e.g.1
def hi(again):
    print(again, "says hi")
hi('me')
hi('you')
print()


# e.g.2
def hi2(again):
    val = 'hello ' + again
    return val
returned = hi2('you')
print(returned)
print()


# e.g.3 (multi returns)
def funcmul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3
    # return [y1, y2, y3]
    # return (y1, y2, y3)
        # returning as lists or tuples 
        # unlike 'y1, y2, y3', lists or tuples would be one result
        # - meaning only one value has to be assigned to the function result
val1, val2, val3 = funcmul(10)
print(val1, val2, val3)
# val = funcmul(10)
# print(val)


# e.g.4
# !!args, !!kwargs


# ARGS
    # with multiple iterable
    # returns into a tuple type
# 1
def args_func1(*args):
    print(args)
# 2
def args_func2(*args):
    for a in args:
        print(a)
    # note that a single input doesn't return a single output
args_func1('bing')
args_func1('bing', 'geller')
args_func1('bing', 'geller', 'green')
args_func2('bing')
args_func2('bing', 'geller')
args_func2('bing', 'geller', 'green')
print()
# 3 
    # enumerate: giving the iterable an index
    #   enumerate(a, b): a - index / b - value
def args_func3(*args):
    for i, v in enumerate(args):
        print(i, v)
args_func3('bing')
args_func3('bing', 'geller')
args_func3('bing', 'geller', 'green')
print()
# 4 (reference)
def argsargs(*args):
    for a, b in enumerate(range(10)):
        print(a, b)
argsargs('a')
argsargs()
print()


# KWARGS (keyword)
    # with multiple iterable
    # returns into a dictionary type
# 1
def kwargs_func1(**kwargs):
    print(kwargs)
kwargs_func1(name1= 'bing')
kwargs_func1(name1= 'bing', name2= 'geller', name3= 'green')
print()
# 2
def kwargs_func2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
kwargs_func2(name1= 'bing')
kwargs_func2(name1= 'bing', name2= 'geller', name3= 'green')


# combination
def example_mul(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)
    # *args and **kwargs don't have to be assigned
example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)
print()



# CLOSURE (--decorator)
    # nested function
def func(num):
    def nestfunc(num):
        print(num)
    print('in func')
    nestfunc(num + 10000)
# 1. prints 'print('in func')'
# 2. runs nestfunc(20000)
func(10000)
# !! cannot run the nested function independently
# nestfunc(1)
print()


# HINT
    # hint on the inserted parameter and the output type 
def hintfunc(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]
print(hintfunc(5))
print(hintfunc(5.0))
print()



# LAMBDA
    # memory efficient, readability, clean code
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화


# general function -> input parameter 
def one(num: int) -> int:
    return num * 10
var_func = one
print(var_func)
print(type(var_func))
    # shows how functions are given memory storage as an object
# running function
print(var_func(10))
print()


# lambda function
lambda_func = lambda num: num * 10 
print(lambda_func(10))

def ld(x, y, func):
    print(x * y * func(10))

ld(10, 10, lambda_func)
ld(10, 10, lambda x: x * 20)