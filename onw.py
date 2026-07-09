#  class Car:
#     def start():
#         print("Car has started")
#     def stop():
#         print("Car has stopped")
# # c1 = Car
# c2 = Car
# # c4 = Car
# # c5 = Car
# c2.start()
# c2.stop()

#constructor

# class Car:
#     def __init__(self,n,c):
#         self.name = n
#         self. colour = "red"
#     def start(self):
#         print(f"{self .name} has started")
#     def stop(self):
#         print("Car stoped")
# c1 = Car("Rollsroyce","Black")
# c2 = Car("BMW","white")
# c1.start()

class Student:
    def __init__(self,name,m1,m2,m3,m4,m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m3
        self.m5 = m5
    def sum_marks(self):
        return self.m1 + self.m2 + self.m3 +self.m4 + self.m5
    def avg_marks(self):
        return self.sum_marks()/5
    def display(self):
        print("Student name:",self.name)
        print("Mark1:",self.m1)
        print("Mark2:",self.m2)
        print("Mark3:",self.m3)
        print("Mark4:",self.m4)
        print("Mark5:",self.m5)
        print("Total marks:",self.sum_marks())
        print("Average Marks:",self.sum_marks()/5)
s1 = Student("Vishwa",85,95,75,90,40)
s1.display()


# class Student:
#     def __init__():
