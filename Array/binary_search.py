n = int(input("N :"))
ls = []

for i in range(0,n):
    nn = int(input("Elements "))
    ls.append(nn)

key = int(input("Enter the key "))
l = 0
r = n
while(l<=r):
    mid = round((l+r)/2)
    if ls[mid] == key:
        print("found")
        break
    elif ls[mid] > key:
        r = mid-1
    else:
        l = mid+1