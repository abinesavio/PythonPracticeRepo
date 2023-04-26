# n = input("Enter the word")
# m = n.swapcase()
# print(m)

#second method
k = ''
n = input("Enter the word")
for i in n:
    if i.islower():
        k += i.upper()
    else:
        k +=  i.lower()
print(k)

