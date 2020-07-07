# Section05-1
# if flow statements
# 조건문 / 흐름제어 (제어문)


# boolean types
print(type(True))
print(type(False))
print()


# e.g.
if True:
    print("yes")

if False: 
    print("no")
else: 
    print("yesyes")
print()


# 관계연산자
    #  >, >=, <, <=, ==, !=
a = 2
b = 3
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print()


# boolean values
# True: 1, "non-empty string", [non-empty list], (non-empty tuple), {non-empty dictionary}, True
# False: 0, "empty string", [empty list], (empty tuple), {empty dictionary}, False
drink1 = ""
drink2 = "trevi"

def drink(drink):
    if drink: 
        print("True")
    else:
        print("False")
    # functions don't need the print() statement to show on terminal
print(drink(drink1))
print(drink(drink2))
drink(drink1)
drink(drink2)
print()


# 논리연산자
# and / or / not
a = 3
b = 6
c = 9
    # and
print('and: ', a<b and b<c)
print('and: ', a>b and b>c)
    # or
print('or: ', a>b or a>b)
print('or: ', a<b or a>b)
    # not
print('not: ', not a>b)
print('not: ', not a<b)
print(not True)
print(not False)
print()


# 산술, 관계, 논리연산자
# 산술 > 관계 > 논리연산자      순으로 적용
print('eg1: ', 1-0==1 and not 1-0==0)
pass1 = 90
pass2 = "A"
if pass1 >= 90 and pass2 == 'A':
    print('passed exams')
else: 
    print('failed exams')
print()


# 다중조건문
# if - elif - else/elif 
# else/elif : if the last statement includes a condition use elif
grade1 = 95
grade2 = 81
grade3 = 70
grade4 = 55
def average(grade):
    if grade >= 90:
        print("grade above average", grade)
    elif grade >= 80:
        print("grade is average", grade)
    elif grade >=70:
        print("grade below average", grade)
    else: 
        print("grade fail", grade)
average(grade1)
average(grade2)
average(grade3)
average(grade4)
print()


# 중첩조건문
temp = 30
humidity = 5
def weather(temp, humidity): 
    if temp < 30:
        if humidity <= 30:
            print("weather good")
        else:
            print("weather good but may rain")
    elif temp >= 30:
        if humidity < 30:
            print("weather too hot")
        else:
            print("weather humid and hot")
weather(temp, humidity)
print()