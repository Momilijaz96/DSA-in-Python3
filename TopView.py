from DataStructures.BinaryTree import BinaryNode


#TopView of tree suing inOrder traversal
def topView(node):
    if root==None: return None
    if root.left==None and root.right==None: return root.data
    
    stack=[]
    f=0 #Offset
    maxf= -10000000 #Max offset, start with a very high neg number to store first lef tmost offset node
    while(1):
        while(node):
            stack.append((node,f))
            f-=1
            node=node.left
        node,f=stack.pop()
        #If there is a node is stack, with same offset, then dont print this one
        #but the one below it 
        overlap_child=False
        if len(stack)>0:
            if f==stack[-1][1]:
                overlap_child=True
        if (f>maxf) and (not overlap_child): #print only the node with offset greater than maxoffset so far
            print(node.data)
            maxf=f #Keep track of max offset printed so far
        #Check if node has a right
        if node.right:
            node=node.right
            f=f+1
        else:
            node=None

        #Break the loop if stack is  empty and no more nodes to be appended
        if len(stack)==0 and node==None:
            break

if __name__=='__main__':
    root=BinaryNode(1)
    root.left=BinaryNode(2)
    root.right=BinaryNode(5)
    root.left.left=BinaryNode(3)
    root.left.right=BinaryNode(4)
    root.left.left.left=BinaryNode(10)
    root.right.left=BinaryNode(6)
    root.right.right=BinaryNode(7)
    root.right.right.right=BinaryNode(8)
    root.right.right.right.left=BinaryNode(9)
    #Answer of top view is: 10,3,2,1,5,7,8

    print("Tree 1 top view: ") 
    topView(root)

    #Tree test 2
    root2=BinaryNode(1)
    root2.left=BinaryNode(2)
    root2.right=BinaryNode(3)
    root2.left.left=BinaryNode(4)
    root2.left.right=BinaryNode(5)
    root2.right.left=BinaryNode(6)
    root2.right.right=BinaryNode(7)
    #Answer of top view is:42137
    print("Tree 2 Top view: ")
    topView(root2)



         

        
