from Node import Node
class MyQueue:
    def __init__(self,node=None):
        self.first=node
        self.last=node
    
    def add(self,val):
        node=Node(val)
        if self.last!=None:
            self.last.next=node
            self.last=node
        else:
            self.first=node
            self.last=node

    def remove(self):
        if self.first!=None:
            data=self.first.data
            self.first=self.first.next
            return data
        else:
            self.last=None
    
    def peek(self):
        if self.first!=None:
            return self.first.data
        else:
            return -1
    
    def isEmpty(self):
        return self.first==None
    
    def printAll(self):
        node=self.first
        if not self.isEmpty():
            print(node.data)
            while(node.next!=None):
                print(node.next.data)
                node=node.next
    
if __name__=='__main__':
    my_queue=MyQueue()
    my_queue.add(1)
    my_queue.add(2)
    my_queue.add(3)
    my_queue.add(4)
    print(my_queue.printAll())
    
    my_queue.remove()
    my_queue.remove()
    print('peek after 2 removes: ',my_queue.peek())
    my_queue.remove()
    my_queue.remove()
    print('peek into emtpy queue: ',my_queue.peek())
    print(my_queue.isEmpty())
    
    


