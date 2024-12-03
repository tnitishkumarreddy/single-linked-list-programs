
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class sll:

    def __init__(self):
        self.head=None

    def append(self,data):

        node=Node(data)

        if not self.head:
            self.head=node
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=node

    def insert_begin(self,data):
        nb=Node(data) # data to be insert at begining
        nb.next=self.head   # current node address should be the adress of next node which is self.head
        self.head=nb   # now change the head position to the new node nb which is at start

    def insert_end(self,data):
        ne=Node(data)

        temp=self.head

        while temp.next:
            temp=temp.next
        temp.next=ne

    def insert_pos(self,pos,data):

        ns=Node(data)

        temp=self.head

        for i in range(pos-1):
            temp=temp.next
        ns.data=data
        ns.next=temp.next
        temp.next=ns

    def display(self):

        cur=self.head

        while cur:
            print(cur.data,end=' ')
            cur=cur.next
l=sll()
l.append(10)
l.append(20)
l.append(30)
l.insert_end(30)
l.insert_begin(5)
l.insert_pos(2,100)
l.display()
