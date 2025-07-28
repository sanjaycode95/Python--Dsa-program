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
    def element_pos(self,a):
        b=self.head
        n=1
        while b:
            if b.element==a:
                return n
            b=b.node
        return "Element not found in list"
    def search_element(self,a):
        b=self.head
        n=1
        while b:
            if n==a:
                return b.element
            n=n+1
            b=b.node
        return "Invalid position"
a=linked_list()
a.add(7)
a.add(8)
a.add(5)
a.add(4)
print(a.element_pos(3)) #5
print(a.element_pos(7)) #Element not found list
print(a.search_element(2)) #8
print(a.search_element(6)) #Invalid position
