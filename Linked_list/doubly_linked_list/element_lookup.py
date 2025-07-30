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
    def position(self,a):
        b=self.head
        pos=1
        while(b):
            if b.data==a:
                return pos                
            b=b.next
            pos=pos+1
    def search_element(self,a):
        b=self.head
        pos=1
        while(b):
            if pos==a:
                return b.data
            pos=pos+1
            b=b.next            
a=Linked_list()
a.add(1)
a.add(4)
a.add(5)
a.add(9)
print("Element 5 at the position =",a.position(5))
print("2nd position element =",a.search_element(2))
