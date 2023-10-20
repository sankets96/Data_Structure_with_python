#list is dynamic array
ls = []
for i in range(0,50):
    ls.append(i)
    print(i," ",)



#Acessing the list
ls[1]=5
print("New list")
#list is mutable so above iter is valid
for i in range(0,50):
    
    print(ls[i])
