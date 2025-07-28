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
a=Linked_list()
a.add(1)
a.add(4)
a.add(5)
