#Return statenment

# def add2(a,b):
#     return "Vijay"
# print(add2(1,2))

# def add(a,b):
#     print(a+b)
# add(1,2)

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def main():
#     while True:
#         print("Welcome to simple calculator!!!!!")
#         choice = int(
#             input("Enter a choice:-\n1.Add\n2.Sub\n3.Mul\n4.div\n5.Exit\n:----"))
#         v = int(input("Enter a number:"))
#         i = int(input("Enter a number:"))
#         if choice == 1:
#             print(add(v,i))
#         elif choice == 2:
#             print(sub(v,i))
#         elif choice == 3:
#             print(mul(v,i))
#         elif choice == 4:
#             print(div(v,i))
#         elif choice == 5:
#             break
#         else:
#             print("Invalid choice:")
# main()

#Lambda Funtion 

z = lambda x,y : x+y
print(z(1,2))

#Product of  3 numbers
z = lambda x,y,z : x*y*z
print(z(1,2,3))

#square of a number

z = lambda x : x**2
print(z(5))   

#Square root of number

z = lambda x : x**0.5
print(z(25))

#Perimetre of circle

z = lambda r : 2 * 3.14 * r
print(z(6))

#Average of 5 number

z = lambda a,b,c,d,f : (a+b+c+d+f)/2
print(z(1,2,3,4,5))

#Full name of a person

Fullname = lambda fname,mname,lname: fname+' '+mname+' '+lname
print(Fullname("Robert","Dony","Xavier"))

#Ternary operator
check = lambda age : "eligible" if age >=18 else "not eligible"
print(check(21))