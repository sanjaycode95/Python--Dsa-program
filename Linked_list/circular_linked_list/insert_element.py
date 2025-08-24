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
    def insert_element(self,data,pos):
        v=node()
        v.data=data
        if pos==1:
            v.next=self.head
            self.head=v
            self.temp.next=self.head
        else:
            b=self.head
            i=2
            while(b.next!=self.head):
                if i==pos:
                    v.next=b.next
                    b.next=v
                b=b.next
                i=i+1
                
        
a=linked_list()
a.add(1)
a.add(2)
a.add(8)
a.insert_element(4,1)
a.insert_element(3,2)
a.display()
