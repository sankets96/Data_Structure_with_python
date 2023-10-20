n = int(input("N :"))
ls = []

for i in range(0,n):
    nn = int(input("Elements "))
    ls.append(nn)

nm = int(input("Element insertion "))
pos = int(input("position insertion "))
for i in range(n-1,pos-1):
    ls[i+1] = ls[i]

ls[pos-1] = nm

print(ls)
