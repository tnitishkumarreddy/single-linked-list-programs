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

    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def delete_end(self):
        prev=self.head
        cur=self.head.next

        while cur.next is not None:
            cur=cur.next
            prev=prev.next
        prev.next=None

    def delete_pos(self,pos):
        prev=self.head
        cur=self.head.next

        for i in range(1,pos-1):
            cur=cur.next
            prev=prev.next

        prev.next=cur.next
        

    def display(self):
        cur=self.head

        while cur:
            print(cur.data,end=' ')
            cur=cur.next

l=sll()
l.append(10)
l.append(20)
l.append(30)
#l.insert_begin(5)
#l.insert_end(4)
#l.insert_pos(23,1)
l.append(40)
l.append(50)
#l.delete_begin()
#l.delete_pos(3)
l.delete_end()
l.display()

