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
         print("\n")
    def  insert_element(self,a,pos):
        k=1
        b=self.head
        while b:
            if pos-1==0:
                address=store()
                self.head=address
                address.element=a
                address.node=b
                break  
            if pos-1==k:
                address=store()
                c=b.node
                b.node=address
                address.element=a
                b.node.node=c
                break
            b=b.node
            k=k+1
a=linked_list()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.display()
a.insert_element(6,2)
print("After inserting element 6  at the position 2\n")
a.display()
