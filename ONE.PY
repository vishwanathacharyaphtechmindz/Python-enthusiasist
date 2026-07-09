# fruits = {"Banana,apple,blueberry,cherry"}
# for i in fruits:
#     print(i)

# set funtction 

# a = {1,2,4,3,5,6}
# b = {6,5,4,3,2,1}
# print(a==b)

# a = [1,2,3,4,5]
# b = [5,4,3,2,1]
# print(a==b)

#mutable
#union
# intersection
# diffrence

#union
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))

#intersection

# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# print(a.intersection(b))

# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# print(a-b)

# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
# print(b-a)

# dictionary value

# userdata = {"Name":"vijay","age":"52","Name":Joseph","email":"vijay@gmail.com","Phone":"8951879045"}
# print(userdata)

# userdata = {"Name":"vijay","age":"52","email":"vijay@gmail.com","Phone":"8951879045"}
# print(userdata)
# print(userdata["Name"])
# print(userdata["Phone"])

# data = {}
# data["name"] = "vijay"
# data["email"] = "vijay@gmail.com"
# data["location"] = "chennai"
# data["phone"] = "8951879045"
# data["name"] = "vishwa"
# print(data)

# a = {"name":"vijay","age":"52","email":"vijay@gmail.com","Phone":"8951879045"}
# print(a.get("name"))
# print(a["Phone"])
# print(a.keys())
# print(a.values())
# print(a.items())
# a.update({'name':'vishwa'})

 # data = {"name":"vijay","age":"52","email":"vijay@gmail.com","Phone":"8951879045"}
 # for i in data:
 #     print(i,data[i])

# data = {"name":"vijay","age":"52","email":"vijay@gmail.com","Phone":"8951879045"}
# for i,j in data.items():
#     print(i,j)

a = 'hello my name is vijay'
b = a.split()
print(b)


a = 'hello my name is vijay'
word = ""
b = []
for i in a:
    if i!= '':
        word = word + i
else:
    b.append(word)
    word = ""
    b.append(word)
    print(b)