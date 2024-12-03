class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''class SLL:
    def __init__(self):
        self.head=None

    def display(self):
        

        if self.head is None:
            print('Linked List is Empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,'--->',end=' ')
                temp=temp.next
l=SLL()
n=Node(10)
l.head=n
n1=Node(20)
l.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
l.display()    
'''
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):    
        n= Node(data)
        if not self.head:     # if not false ---->True
            self.head = n
            return
        temp= self.head
        while temp.next:
            temp= temp.next
        temp.next=n

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        
l=SinglyLinkedList()
l.append(10)
l.append(20)
l.display()

