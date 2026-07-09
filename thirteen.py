# i = 1
# while i < 10 :
#     print(i)
#     i = i + 1


# i = 1
# sum = 0
# while i <= 10:
#     sum =  sum + i
#     i = i + 1
#     print(sum)

i = 1
even_sum = 0
odd_sum = 0

while i <= 100:
    if i % 2 == 0:
       even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
    i = i + 1
print(even_sum)
print(odd_sum)

