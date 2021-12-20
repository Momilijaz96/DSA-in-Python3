from Node import Node
class LinkedList:
    #Constrcutor for linked list
    def __init__(self,node):
        self.head=node
        self.count=1
    
    #Function for adding new node with given data to linked list
    def addNode(self,data):
        head=self.head
        node=head
        end=Node(data)
        while(node.next!=None):
            node=node.next
        node.next=end
        self.head=head
        self.count+=1
    
    #Function to delete node with particular idx from linked list
    def deleteNode(self,k):
        head=self.head
        node=head
        node_idx=1
        '''
        Note: In a while loop like this over a linked list,
        always perform desired task from previous to desored node,
        otherwise last node will be skipped as while loop will break
        before runing code for last node, and deal with head node outside loop
        '''
        if k==1:
            head=head.next
        else:
            while(node.next!=None):
                if (node_idx==k-1):
                    node.next=node.next.next
                    break
                node_idx+=1
        self.head=head
        self.count-=1

    
    #Function to update k node, wher enode index starts at 1
    def updateNode(self,k,new_data):
        head=self.head
        node=head
        node_idx=1
        if k>self.count or k<0:
            print("Invalid index value for Node")
            return None
        elif k==1:
            head.update(new_data)
            self.head=head
        else:
            while(node.next!=None):
                if node_idx==k-1:
                    node.next.update(new_data)
                    self.head=head
                    print("Updated node")
                    break
                node=node.next
                node_idx+=1

    #Function to get list node by index, where node idx starts at 1
    def getNode(self,k):
        node=self.head
        node_idx=1
        if k>self.count or k<0:
            print("Invlaid index for Node")
            return None
        if k==1:
            return node.data
        else:
            while(node.next!=None):
                if node_idx==k-1:
                    return node.next.data
                node=node.next
                node_idx+=1

    #Function to traverse through all nodes
    def listAll(self):
        node=self.head
        print(node.data)#Print head node's data
        while(node.next!=None):
            print(node.next.data)
            node=node.next

if __name__=='__main__':
    list=LinkedList(Node(data=(0,'apple')))            
    #print("List Nodes: ")
    #list.listAll()
    #print("Node Count: ",list.count)

    #Add 5 nodes
    list.addNode((1,'ball'))
    list.addNode((2,'cat'))
    list.addNode((3,'orange'))
    list.addNode((4,'duck'))
    list.addNode((5,'egg'))
    #print("List Nodes after addition: ")
    #list.listAll()
    print("Latest Node Count: ",list.count)

    #Update 6th node
    list.updateNode(1,(1,'BALL'))
    print("Update Node: ",list.getNode(1))

    #Delete a node
    list.deleteNode(4)
    print("After deletion ")
    list.listAll()

