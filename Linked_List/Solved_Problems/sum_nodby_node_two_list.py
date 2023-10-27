class node:
    def __init__(self,val):
        self.data = val
        self.next = None



class linkedlist:

    def __init__(self):
        #create empty linked list
        self.head = None
        self.n = 0


    def __len__(self):
        return self.n


    def insert_head(self,val):
        #create new node
        new = node(val)
        new.next = self.head
        self.head = new
        self.n = self.n+1

    def clear(self):
        self.head = None
        self.n = 0
    

    def sumiing(self,l2):
        curr1 = self.head
        curr2 = l2.head
        if self.n == l2.n:
            while curr1 != None:
                d = curr1.data + curr2.data
                print(d)
                curr1 = curr1.next
                curr2 = curr2.next
        else :
            while curr1 != None or curr2 != None:
                if curr1  == None and curr2 != None:
                    print(curr2.data)
                    curr2=curr2.next
                elif curr1 != None and curr2 == None:
                    print(curr1.data)
                    curr1 = curr1.next
                    

                else:
                    d = curr1.data + curr2.data
                    print(d)
                    curr1 = curr1.next
                    curr2 = curr2.next

    


    
    def traverse(self):
        curr = self.head
        while(curr != None):
            print(curr.data)
            curr = curr.next




l = linkedlist()
l.insert_head(13)
l.insert_head(12)
l.insert_head(11)
l.traverse()
l2 = linkedlist()
print('second list ')
l2.insert_head(11)
l2.insert_head(21)
l2.insert_head(3)
l2.traverse()
print("summing ")
l.sumiing(l2)

print("summning not symmetry nodes 1")
l2.insert_head(90)
l.sumiing(l2)