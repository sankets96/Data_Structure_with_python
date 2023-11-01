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

    


    
    def traverse(self):
        curr = self.head
        while(curr != None):
            print(curr.data)
            curr = curr.next


    def odd_sum(self):
        curr =self.head
        counter = 1
        sum = 0
        while curr != None:
            
            if counter%2 != 0:
                sum = sum+curr.data
            curr = curr.next
            counter = counter +1
        return sum

        






l = linkedlist()

l.insert_head(13)
l.insert_head(24)
l.insert_head(12)
l.insert_head(11)
l.traverse()
print('Odd position sum of elements ')
print("sum is ",l.odd_sum())
