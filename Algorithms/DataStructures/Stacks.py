from Node import Node

class Stack:
    def __init__(self,top_node=None):
        self.top=top_node
    
    def push(self,val):
        node=Node(val)
        node.next=self.top
        self.top=node     
    
    def pop(self):
        if self.top!=None:
            data=self.top.data
            self.top=self.top.next
            return data
        else:
            return -1

    def peek(self):
        if self.top!=None:
            return self.top.data
        else:
            return -1
        
    def isEmpty(self):
        return self.top==None

    def printAll(self):
        node=self.top
        if not self.isEmpty():
            print(node.data)
            while(node.next!=None):
                print(node.data)
                node=node.next

if __name__=='__main__':
    stack=Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    stack.pop()
    stack.pop()
    print(stack.peek())
    #stack.printAll()
    print(stack.isEmpty())
    
    