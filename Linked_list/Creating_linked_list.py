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
a=linked_list()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
