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
            while(b.next!=self.head):
                print(b.next.data,end="->")
                b=b.next
a=linked_list()
a.add(1)
a.add(2)
a.add(8)
a.display()
