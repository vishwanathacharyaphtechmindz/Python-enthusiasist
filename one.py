#Decorators

# def saymyname(fun):
#     def wrapper():  #inner function 
#         print("say my name")
#         fun()
#         print("you are right")
#     return wrapper

# @saymyname
# def add():
#     print("add 2 numbers")

# @saymyname
# def hello():
#     print("Hello vijay")

# hello()
# add()

#ARGUMENTS
# def add(*args):
#     return args()
# print((1,2,3,4,5,6,7,8,9,0))

# #KEYWORD ARGUMENTS
# def add(**kargs):
#     return kargs()
# print(("fname:","vishwa","mname:","Acharya","lname:","P H"))

# def fullname(*args,**kwargs):
#     print(kwargs)
# fullname(fname="vishwa",mname="Acharya",lname="P H")



# import time
# print(time.time())
# print(time.ctime(1784183944.0896819))
# print(time.time())
# start = time.time()
# for i in range(1,11):
#     print(i)
#     time.sleep(1)
# stop = time.time()
# print("total time:",stop-start)


import time

def totaltime(fun):
    def inner(fun):
        def wrapper(*args,**kwargs):
            start = time.time()
            fun(*args,**kwargs)
            stop = time.time()
            print(f"total time : {stop-start}")
        return wrapper
    return inner
@totaltime(10)
def myname(n):
    for i in range(n):
        print(i)
        time.sleep(1)
myname(5)