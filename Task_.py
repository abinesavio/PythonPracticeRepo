# n= int(input("Number of items:"))
# d = {}
# for i in range(n):
#     item = input("Enter the name and rate:").split()
#     ip = int(item[-1])
#     itm = " ".join(item[:-1])
#     if d.get(itm):
#         d[itm] += ip
#     else:
#         d[itm] = ip
# for i in d.keys():
#     print(i, d[i])
# 2 ND WAY
order = {}
for _ in range(int(input("Enter the number:"))):
    item, space, price =input("Enter the item and price:").rpartition(" ")
    order[item] = order.get(item,0) + int(price)
for item ,price in order.items():
    print(item,price)