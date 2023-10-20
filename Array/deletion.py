n = int(input("N :"))
ls = []

for i in range(0,n):
    nn = int(input("Elements "))
    ls.append(nn)


pos = int(input("position Deletion "))
for i in range(pos,n):
    ls[i-1] = ls[i]

n = n-1
for i in range(0,n):
    print(ls[i])
