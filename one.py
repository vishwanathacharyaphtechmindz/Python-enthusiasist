# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def reset(self):
#         self.x,self.y = 0,0    
#         self.move(0,0)    
    
#     def move(self,a,b):
#          self.x = a
#          self.y = b
        
#     def move(self):
#         self.x = 8
    
#     def move(self):
#         self.y = 7


# p1 = Point(4,5)
# print(p1.x,p1.y)
# p1 = Point(0,0) 
# print(p1.x,p1.y)
# p1.move()
# print(p1.x)
# p1.move()
# print(p1.y)

#ABSTRACT METHOD

from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def makes_sound(self):
        print("Animal makes sound")
class Dog:
    def __init(Animal):
        pass
    def makes_sound(self):
        print("woff woff")

d = Dog()
d.makes_sound()  

#ENCAPSULATION
#ACCESS MODIFIER

#1.public access modifier
  
class Student:
    def __init__(self):
        self.name = "vijay"

s1 = Student()
print(s1.name)  

#2.protected access modifier

class Student2:
    def __init__(self):
        self._age = 21

s2 = Student2()
print(s2._age)

#3.private access modifier
class Student3:
    def __init__(self):
        self.__marks = 95

s3 = Student3()
print(s3._Student3__marks)

#code

class Queue:
    def

    

