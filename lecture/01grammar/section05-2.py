# Section05-2
# 반복문 / 흐름제어 (제어문)

# for, while basics
    # difference: 
    #   while loop will do sth as long as the condition is met. 
    #   for loop will do soth to everything which i wish to iterate through.
c1 = 1

    # while
while c1 < 11:
    print("c1 is : ", c1)
    c1 += 1
print()

    # for
for c2 in range(10):
    print("c2 is : ", c2)
print()

for c3 in range(1, 11):
    print("c3 is : ", c3)
print()


# adding 1 to 100

    # for
i = 1
cm = 0
for i in range(101):
    cm = cm + i
    i += 1
print(cm)
print()

    # while
ii = 1
cmm = 0
while i <= 100:
    cm += i
    i += 1
print(cm)
print()

    # sum()
print(sum(range(0, 101)))
print(sum(range(0, 101, 2)))
print()


# sequence: 순서가 있는 자료형 반복
    # 자료형: 문자열, 리스트, 튜플, 집합, 사전
# iterable return functions: range, reversed, enumerate, filter, map, zip

names = ['chandler', 'monica', 'rachel', 'joey', 'phoebe', 'ross']
for name in names: 
    print("friends: ", name)
print()

character = "character"
for c in character:
    print('each letter in character: ', c)
print()


# for loops on dictionaries
client = {
    'name': 'anonymous',
    'age': '79',
    'location': 'seoul'
}
    # default
for k in client:
    print("client info: ", k)
    # key
for k in client.keys():
    print("client info: ", k)
    # value
for k in client.values():
    print("client info: ", k)
    # item
for k in client.items():
    print("client info: ", k)
for k , v in client.items():
    print("client info summary: ", k, v)
print()


#  q: for 'name = "CHANDler"' change uppercases and lowercases
name = 'CHANDler'
for n in name: 
    if n == n.upper():
        print(n.lower())
    else:
        print(n.upper())
print()

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())
print()


# break
    # breaking an iteration for a condition

    # finding 44
numbs = [14, 3, 8, 6, 44 ,25, 39, 23, 2, 9]
for numb in numbs:
    if numb == 44:
        print('found ', numb)
        break
    else:
        print('not found', numb)
else:
    print('no 44')
# the iteration won't continue after 44 because of 'break'
# the iteration will run for-else when 'break' wasn't met
print()


# continue
    # skipping the rest of the iteration

    # finding float
random = ["1", 2, 5, True, 4.3, complex(0)]
for r in random:
    if type(r) is float:
        print('found float', r)
        break
    else: 
        print('not a float but a ', type(r))
else: 
    print('there are no floats in the list')
print()

    # if float skip
for r in random:
    if r is float:
        continue
    print(r, 'is ', type(r))

