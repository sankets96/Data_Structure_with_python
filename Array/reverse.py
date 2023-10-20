n = int(input("N :"))
ls = []

for i in range(0,n):
    nn = int(input("Elements "))
    ls.append(nn)
#thiw iw direct method
# print("This is direct method")
# ls.reverse()

# print(ls)

l=0
r=n-1
while(l<=r):
    temp = ls[l]
    ls[l] = ls[r]
    ls[r] = temp

    l = l+1
    r = r-1

print("Indirect method ")
print(ls)
