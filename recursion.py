#Recursion funtion 
# def counttozero(n):
#     print(n)
#     # if n == 0:
#         # return
#     return counttozero(n)
# counttozero(10)

#Sum of 10 numbers

# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1)
# print(sum(10))

#Factorial 

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(6))

#Scope of variable
name = "Joseph" #Gloabal Scope
def myname():
    name = "Vijay" #Local Scope
    print(name)
    def surname():
        name = "Thalapathy"
        print(name)
    surname()
myname()


