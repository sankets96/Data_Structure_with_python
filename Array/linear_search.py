n = int(input("N :"))
ls = []

for i in range(0,n):
    nn = int(input("Elements "))
    ls.append(nn)


pos = int(input("Search element "))
for i in range(0,n):
    if pos == ls[i]:
        print("Found in ",i+1)
    elif i==n:
        print('Enter valid element ')
    else :
        pass




