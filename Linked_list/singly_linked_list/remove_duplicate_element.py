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
    def remove_duplicate(self):
        b=self.head
        dump=[b.element]
        while b:
            if b.node!=None:
                if b.node.element in dump:
                    b.node=b.node.node
                else:
                    dump.append(b.node.element)
            b=b.node
a=linked_list()
a.add(1)
a.add(4)
a.add(2)
a.add(3)
a.add(4)
a.add(1)
#Removing duplicate element 4,1
print("After removing duplicate element")
a.remove_duplicate()
a.display()
