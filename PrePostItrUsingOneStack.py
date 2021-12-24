from DataStructures.BinaryTree import BinaryNode

def travAll(node):
    stack=[]
    preOrder=[]
    inOrder=[]
    postOrder=[]
    while(1):
        while(node):
            if node.right:
                stack.append((node.right,0))
            stack.append((node,0))
            preOrder.append(node.data)
            node=node.left
        node=stack.pop()
        if node[1]==0:
            inOrder.append(node[0].data)
        
        if len(stack)>0 and node[0].right==stack[-1][0]:
            rn=stack.pop()[0]
            stack.append((node[0],-1)) #This node is for post order trav
            node=rn
        else:
            postOrder.append(node[0].data)
            node=None

        if len(stack)==0: break
    print("PreOrder: ",preOrder)
    print("PostOrder: ",postOrder)
    print("InOrder: ",inOrder) 

if __name__=='__main__':
    root=BinaryNode(1)
    root.left=BinaryNode(2)
    root.right=BinaryNode(3)
    root.left.left=BinaryNode(6)
    root.left.right=BinaryNode(7)
    root.right.left=BinaryNode(4)
    root.right.left.right=BinaryNode(5)

    #Traverse nodes
    (travAll(root))


