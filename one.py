#Exception 
#Events that affect the excution of our programm

#errors

# try:
#     a = 5
#     b = 0
#     print(a/b)
# except Exception as e:
#     print("You have an error ",e)
# print("vijay")

# try:
#     a = int(input("enter : -"))
#     b = 5
#     print(a/b)
# except ZeroDivisionError:
#     print("you cannot divide a number with zero")
# except ValueError:
#     print("check values")
# except TypeError:
#     print("check types")
# finally:
#     print("This will always excute")

# class MyError(Exception):
#     pass
# name = "das"
# if name == "das":
#     raise MyError("Name should not be das")
# a = 5
# del(a)
# print(a)

#File Handling


# file1 = open("data.txt","r")
# print(file1.read())
# file1.close()

# file2 = open("myfile.txt", "a")
# file2.write("this month iis july!!!!!!!!!")
# file2.close()

# file3 = open("myfile.txt","a")
# file3.write("\nVijay")
# file3.close()

# file5 = open("myfile.txt","a")
# for i in range(1,10000):
#     file5.write(f"\nVijay {i}")
# file5.close()

#OS

import os
os.mkdir("images")
os.remove("data.txt")
os.rename("myfile.txt","demo.txt")
path = "C:\\Users\\sshab\\OneDrive\\Desktop\\june 2026"    
if os.path.exists(path):
    if os.path.isfile(path):
        print("file exists")
    elif os.path.isdir(path):
        print("folder exists")