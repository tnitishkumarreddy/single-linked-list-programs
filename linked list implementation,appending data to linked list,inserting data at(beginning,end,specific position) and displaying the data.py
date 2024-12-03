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

        ns=Node(data)

        ns.next=self.head
        self.head=ns

    def insert_end(self,data):

        ne=Node(data)

        t=self.head
        while t.next:
            t=t.next
        t.next=ne

    def insert_pos(self,data,pos):

        np=Node(data)

        tem=self.head

        for i in range(pos-1):
            tem=tem.next
        np.data=data
        np.next=tem.next
        tem.next=np

    def display(self):
        cur=self.head

        while cur:
            print(cur.data,end=' ')
            cur=cur.next

l=sll()
l.append(10)
l.append(20)
l.append(30)
l.insert_begin(5)
l.insert_end(4)
l.insert_pos(23,1)
l.display()

