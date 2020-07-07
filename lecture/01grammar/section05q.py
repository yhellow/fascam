# Section05-3
# sequence quiz

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for s in q1:
    if s == "가을": 
        print(q1[s])
print()


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for s in q2: 
    if q2[s] == "사과":
        print("사과 있음")
        break
else:
    print('사과 없음')
print()


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
grade = 100
if grade > 80:
    print('A')
elif grade > 60:
    print('B')
elif grade > 40:
    print('C')
elif grade > 20:
    print('D')
else:
    print('E')
print()


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 12, 6, 18
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
print()


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
pid = '3030309'
if int(pid[0]) % 2 == 0:
    print('female')
else:
    print('male')
print()


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for q in q3:
    if q == '정':
        continue
    print(q)
print()
    # list comprehension
l6 = [x for x in q3 if x != '정']
print(l6)
print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
odds = []
# for i in range(1, 101):
#     if i % 2 == 1:
        # odds.insert(i-1, i)
        # odds.append(i)
# print(odds)
for i in range(1, 101):
    if i % 2 == 1:
        print(i, end=' ')
print()
print()
oddss = [x for x in range(1, 101) if x%2==1]
print(oddss)
print()


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for q in q4:
    if len(q) >= 5:
        print(q)
print()


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for q in q5:
    if q.islower():
        print(q)
print()


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
mod = []
for q in q6:
    if q.isupper():
        mod.append(q.lower())
    else:
        mod.append(q.upper())
print(mod)
print()



# list comprehension
    # doing "making a blank list to insert values with certain conditions" easily
    # !! list = [x(appendingValue) for x in y(iterable) if condition]
# e.g. making a list of 1 to 100
    # ordinary way 
insert = []
for i in range(1, 101):
    insert.append(i)
print(insert)
print()
    # list comprehension way
numbers = [x for x in range(1, 101)]
print(numbers)
