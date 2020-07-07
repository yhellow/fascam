# Section07-2
# class, inheritance


# basics
    # superclass(parent) / subclass(child) -> child can use all attributes and methods of the parent
    # code can be reused by inheriting class + reduce repetition 


# e.g.1
class Computer():
    """parent class"""
    def __init__(self, ty, color):
        self.ty = ty
        self.color = color
    def show(self):
        return 'Computer Class "show method"'

class samsung(Computer):                # using Computer class as parent
    """subclass"""
    def __init__(self, computer_name, ty, color):
        super().__init__(ty, color)
        self.computer_name = computer_name
    def show_model(self):
        return "your computer is: %s" % self.computer_name

class apple(Computer):                # using Computer class as parent
    """subclass"""
    def __init__(self, computer_name, ty, color):
        super().__init__(ty, color)
        self.computer_name = computer_name
    def show_model(self):
        return "your computer is: %s" % self.computer_name
    def show(self): 
        print(super().show())
        return 'car info: %s %s %s' %(self.computer_name, self.ty, self.color)



model1 = samsung('ios', 'air', 'spacegrey')

# general use
print(model1.color)                 # super
print(model1.ty)                    # super
print(model1.computer_name)         # sub
print(model1.show())                # super
print(model1.show_model())          # sub
print(model1.__dict__)
print()

# method overriding use
model2 = apple('window', 'galaxy', 'neonpurple')
print(model2.show())                # subclass 'show()' has overrided superclass 'show()'
print()

# parent method call
model3 = apple('ios', 'pro', 'gold')
print(model3.show())                # calling super method through 'super().function()'
print()

# inheritance info
    # '.mro()' : returns the inheritance info as a list format
    # source return
print(apple.mro())                  # [<class '__main__.apple'>, <class '__main__.Computer'>, <class 'object'>]
print(samsung.mro())                # from right to left <-- (object(super of all) -> Computer -> apple)
print()



# e.g.2
    # multiple inheritance
class X(object):                    # object is the super of the py doc
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class F(B, A, Z):
    pass


print(F.mro())                      # multiple inheritance of class X, Y, Z, A, B
print(A.mro())