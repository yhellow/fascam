# Section07-1
# class, self, instance variable


# declaring class
    # naming: the first letter has to be uppercase
    # 속성 + 메소드 (attribute + method)로 구성
class ClassName:
    # func1
    # func2
    pass
    # functions are assigned to the relevant class
    # pass to prevent error



# e.g.1
    # class를 초기화할 때 구현되는 함수
    # can have or not have ()
class UserInfo:
    def __init__(self, name):               # function that is called when the instance is starting
        self.name = name
    def user_infoi(self):
        print("Name: ", self.name)

user1 = UserInfo("Chandler")
user1.user_infoi()
user2 = UserInfo("Monica")
user2.user_infoi()
    # print memory address
print(id(user1))
print(id(user2))
    # print namespace
print(user1.__dict__)
print(user2.__dict__)

# 인스턴스화를 해서 클래스를 활용, 인스턴스화된 변수들은 독립적인 namespace 에 저장
# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용
print()



# e.g.2
    # self
class Selftest(): 
    def function1():
        print('function1 called')
    def function2(self):
        print(id(self))
        print("function2 called")

selfself = Selftest()
    # without the self parameter in 'function1()' the 'selfself' instance cannot be applied
# selfself.function1()
selfself.function2()
Selftest.function1()
# Selftest.function2()
Selftest.function2(selfself)
print(id(selfself))
    # proven that the selfself instance has been given to 'function2()'
# SUMMARY
# with the 'self' parameter the instance info is given to the class function
# without the 'self parameter the instance info is not given to the class function 
#   and therefore the function has to be called from the class itself
print()



# e.g.3
    # class variable, instance variable

class Warehouse():
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1        # call from the class
    def __del__(self):                  # function that is run when the instance is ending
        Warehouse.stock_num -= 1

client1 = Warehouse('joey')
client2 = Warehouse('ross')
client3 = Warehouse('rachel')
client4 = Warehouse('phoebe')

print(client1.__dict__)
print(client2.__dict__)
print(client3.__dict__)
print(client4.__dict__)

print(Warehouse.__dict__)               # 'stock_num': 4 / class namespace / class variable global

print(client1.name)
print(client2.name)
print(client3.name)
print(client4.name)

print(client1.stock_num)                # if it's not in the instances namespace, it fetches from the class namespace
print(client2.stock_num)                # if it's not in both, then an error occurs
print(client3.stock_num)                
print(client4.stock_num)                

del client1
print(client2.stock_num)                # 'stock_num': 3
print(client3.stock_num)                
print(client4.stock_num) 