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
        b=self.head
        while(b):
            print(b.data,end="->")
            b=b.next
        print("None")
    def insert_element(self,a,pos):
        v=node()
        v.data=a
        if (pos==1):
            self.head.pre=v
            v.next=self.head
            self.head=v
            return None
        a=2
        b=self.head
        while(b):
            if pos==a:
                v.next=b.next
                v.pre=b
                b.next=v
                v.next.pre=v
            a=a+1
            b=b.next
a=Linked_list()
a.add(1)
a.add(4)
a.add(5)
a.display()
# Insert the new element at specific position
a.insert_element(8,2)
print("\n___After inserting element 8 at position 2___\n")
a.display()
