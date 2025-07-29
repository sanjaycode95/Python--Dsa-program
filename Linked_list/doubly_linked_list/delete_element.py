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
    def delete_element(self,a):
        b=self.head
        dump=0
        if b.data==a:
            b.next.pre=None
            self.head=b.next
            dump=1
        else:
            while(b.next):
                if (b.next.next):
                    if b.next.data==a:
                        b.next.next.pre=b
                        b.next=b.next.next
                        dump=1
                        break
                b=b.next
            if(b and dump==0):
                if(b.data==a):
                    b.pre.next=b.next
                    self.temp=b.pre
                    dump=1
        if dump==0:
            print("element not exist")
a=Linked_list()
a.add(1)
a.add(4)
a.add(5)
a.display()
#delete the specific element at any position
a.delete_element(5)
print("After deleting element 5")
a.display()
