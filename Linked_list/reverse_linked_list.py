class store:
    def __init__(self):
        self.element=None
        self.node=None    
class linked_list:
    def __init__(self):
        self.head=None
        self.current=None
    def add(self,a):
        address=store()
        address.element=a
        if self.head==None:            
            self.current=address
            self.head=address
        else:
            self.current.node=address
            self.current=address
    def display(self):
         b=self.head
         while b:
             print(b.element,end="->")
             b=b.node
    def reverse(self):
        pre=None
        curr=self.head
        while curr:
            dump=curr.node
            curr.node=pre
            pre=curr
            curr=dump
        self.head=pre 
a=linked_list()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.display()
a.reverse()
print("\n\treversed_list")
a.display()
