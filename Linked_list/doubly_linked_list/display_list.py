class node:
    def __init__(self):
        self.data=None
        self.pre=None
        self.next=None
class Linked_list:
    def __init__(self):
        self.temp=None
        self.head=None
    def add(self,a):
        v=node()
        v.data=a
        if self.head==None:
            self.temp=v
            self.head=v
        else:
            self.temp.next=v
            v.pre=self.temp
            self.temp=v
    def display(self):
        print("\n")
        b=self.head
        while(b):
            print(b.data,end="->")
            b=b.next
        print("None")
    def reverse_display(self):
        print("\n")
        b=self.temp
        while(b):
            print(b.data,end="->")
            b=b.pre
        print("None")        
a=Linked_list()
a.add(1)
a.add(4)
a.add(5)
#display each element using head address
a.display()
#display each element using tail address
a.reverse_display()
