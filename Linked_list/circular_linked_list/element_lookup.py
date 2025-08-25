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
    def position(self,a):
        b=self.head
        i=1
        while(b.next!=self.head):
            if a==b.data:
                return i
            i=i+1
            b=b.next
        if b.data==a:
            return i
        print("\n invalid value\n")
    def search_element(self,pos):
        b=self.head
        i=1
        while(b.next!=self.head):
            if i==pos:
                return b.data
            i=i+1
            b=b.next
        if i==pos:
            return b.data
        print("\n invalid postion \n")
a=linked_list()
a.add(1)
a.add(2)
a.add(8)
print("Elemen 8 at the  position ",a.position(8))
print("2nd position the element is  ",a.search_element(2))
a.display()
