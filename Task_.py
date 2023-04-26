n= int(input("Number of items:"))
d = {}
for i in range(n):
    item = input("Enter the name and rate:").split()
    ip = int(item[-1])
    itm = " ".join(item[:-1])
    if d.get(itm):
        d[itm] += ip
    else:
        d[itm] = ip
for i in d.keys():
    print(i, d[i])
