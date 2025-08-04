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
    def swap(self):
	b=self.head
        i=0
        temp=None
	while(b.node):
            if i==0:
                temp=b
                x=b.node
                b.node=b.node.node
                x.node=b
                self.head=x
                i=1
            else:                    
            	x=b.node                    
                b.node=b.node.node
                temp.node=x
                x.node=b
                temp=b
            b=b.node 
a=linked_list()
a.add(1)
a.add(4)
a.add(2)
a.add(3)
a.swap()
a.display()
