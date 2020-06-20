# Section04-5
# data type quiz

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print('1. ', len(q1))
print()

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('2. ', 'apple;orange;banana;lemon')
print()

# 3. 화면에 * 기호 100개를 표시하세요.
print('3. ', '*' * 100)
print()

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
i = int("30")
f = float("30")
c = complex("30")
s = str("30")
print('4. ',i, f, c, s)
print()

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
nm = "Niceman"
print('5. ', nm[-3:])
print('5. ', nm[4:7])
print('5. ', nm[4:])
man = nm.index('man')
print('5. ', nm[man:man+3])
print()

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
given = "Strawberry"
print('6. ', ('').join(reversed(list(given))))
# print(('').join(list(given).reverse()))
print('6. ', given[::-1])
print()

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
number = "010-7777-9999"
ns = list(number)
ns.remove('-')
ns.remove('-')
nss = ('').join(ns)
print('7. ', nss)
    # 정규표현식
import re
print('7. ', re.sub('[^0-9]', '', number))
print()

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
link = "http://daum.net"
print('8. ', link[7:])
print()

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
nm = "NiceMan"
print('9. ', nm.lower())
print('9. ', nm.upper())
print('9. ', nm.capitalize())
print()

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
abc = "abcdefghijklmn"
print('10. ', abc[2:5])
print()

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
fruits = ["Banana", "Apple", "Orange"]
fruits.remove("Apple")
print('11. ', fruits)
print()

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
t = (1,2,3,4)
l = list(t)
print('12. ', l)
print()

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
costs = {'성인': 100000, '청소년': 70000, '아동': 30000}
print('13. ', costs)
print()

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
costs['소아'] = 0
print('14. ', costs)
print()

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print('15. ', costs.keys())
print('15. ', list(costs.keys()))
print()

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print('16. ', costs.values())
print('16. ', list(costs.values()))
print()