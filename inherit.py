#INHERITANCE

# class Person1:
#     pass
# def walk(self):
#     print("person can walk")
# def smile(self):
#     print("person can smile")

# class Person2(Person1):

#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read")
#     def read(self):
#         print("person can read")
#     def speak(self):
#         print("person can speak")

# class Person3(Person2):

#     def __init__(self):
#         pass 
#     def sleep(self):
#         print("person can sleep")
#     def swim(self):
#         print("person can swim")
#     def speak(self):
#         print("person3 can speak")

# class Person4(Person3):

#     def __init__(self):
#         pass 
#     def sleep(self):
#         print("person can sleep")
#     def eat(self):
#         print("person can eat")
#     def speak(self):
#         print("person4 can speak")

# p4 = Person3()
# p4.speak()
# p4 = Person4()
# p4.speak()

#Multiple inheritance

# class Person1:
#     pass
# def walk(self):
#     print("person can walk")
# def smile(self):
#     print("person can smile")

# class Person2(Person1):

#     def __init__(self):
#         pass
#     def read(self):
#         print("person can read")
#     def read(self):
#         print("person can read")
#     def speak(self):
#         print("person can speak")

# class Person3(Person2):

#     def __init__(self):
#         pass 
#     def sleep(self):
#         print("person can sleep")
#     def swim(self):
#         print("person can swim")
#     def speak(self):
#         print("person3 can speak")

# class Person4(Person3,Person2,Person1):

#     def __init__(self):
#         pass 
#     def sleep(self):
#         print("person can sleep")
#     def eat(self):
#         print("person can eat")
#     def speak(self):
#         print("person4 can speak")
#         super().speak()

# p4 = Person4()
# p4.speak()

#Method overloading
#operator overloading

#operator overloading

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self,otr):
#         return self.m1+self.m2,otr.m1+otr.m2
# s1 = Student(7,8)
# s2 = Student(6,10)
# print(s1+s2)

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __sub__(self,otr):
        return self.m1-self.m2,otr.m1-otr.m2
s1 = Student(7,8)
s2 = Student(6,10)
print(s1-s2)

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __mul__(self,otr):
        return self.m1*self.m2,otr.m1*otr.m2
s1 = Student(7,8)
s2 = Student(6,10)
print(s1*s2)

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __truediv__(self,otr):
        return self.m1/self.m2,otr.m1/otr.m2
s1 = Student(7,8)
s2 = Student(6,10)
print(s1/s2)

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __gt__(self,otr):
        return self.m1<self.m2,otr.m1>otr.m2
s1 = Student(7,8)
s2 = Student(6,10)
print(s1>s2)


#Method overloading

class ABCD:
    def __init__(self):
        pass
    def xyz(self,a):
        print(a)
    def xyz(self,b):
        print(b)
    def xyz(self,c):
        print(c)
xyz = a        

#method overriding  

class A:
    def __init__(self):
        pass
    def hello(self):
        print("A hello")

class B:
    def __init__(self):
        pass
    def hello(self):
        print("a hello") 

b = B()
b.hello()                     
a = A()
a.hello()