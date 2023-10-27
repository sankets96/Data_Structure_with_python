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
    
    
    def maxno(self):
        maxnum = 0
        curr = self.head
        while curr != None:
            if curr.data > maxnum:
                maxnum = curr.data
            curr = curr.next

        print(maxnum," -> this is max number")
    
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
l.maxno()