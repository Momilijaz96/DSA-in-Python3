class Node:
    #Cosntructor for Node
    def __init__(self,data='',next=None):
        self.data=data
        self.next=next
    
    #Update data in node
    def update(self,new_data):
        self.data=new_data

    
if __name__=='__main__':
    key=3
    value='apple'
    node=Node((key,value))
    print("Old Node: ",node.data)
    node.update((4,'orange'))
    print("Node Updated: ",node.data)



