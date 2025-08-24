class node:
    def __init__(self):
        self.data=None
        self.next=None
class linked_list:
    def __init__(self):
        self.temp=None
        self.head=None
    def add(self,a):
        v=node()
        v.data=a
        if self.head==None:
            self.head=self.temp=v
        else:
            self.temp.next=v
            self.temp=v
        v.next=self.head
    def display(self):
        b=self.head
        if b:
            print(b.data,end="->")
            b=b.next
            while(b!=self.head):
                print(b.data,end="->")
                b=b.next
    def delet_element(self,data):
        b=self.head
        if b.data==data:
            self.head=b.next
            self.temp.next=self.head
        else:
            while(b.next!=self.head):
                if b.next.data==data:
                    b.next=b.next.next
                    break
                b=b.next
a=linked_list()
a.add(1)
a.add(2)
a.add(8)
a.delet_element(8)
a.display()
