name = "Thalapathy"
def add2(a,b):
    return a+b
print(add2(1,2))
# print(name)
# print(add2(1,2))

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(4))