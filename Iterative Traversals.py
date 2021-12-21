from DataStructures.BinaryTree import BinaryNode

def PostOrderTraversal_itr(node): #Using 2 stacks
    stack=[node]
    vals_stack=[] #put values in a stack
    if node!=None:
        while(len(stack)>0):
            #Appending nodes as Root-l-r on stack
            vals_stack.append(node.data)
            if node.left!=None:
                stack.append(node.left)
            if node.right!=None:
                stack.append(node.right)
            node=stack.pop()
    vals_stack.reverse()
    return vals_stack

def PreOrderTraversal_itr(node):
    stack=[node]
    vals=[] #Put values in a list
    if node!=None:
        while(len(stack)>0):
            vals.append(node.data)
            #Appending nodes as Root-r-l on stack
            if node.right!=None:
                stack.append(node.right)
            if node.left!=None:
                stack.append(node.left)
            node=stack.pop()
    return vals

def InOrderTraversal_itr(node):
    stack=[node]
    vals=[]
    while(len(stack)>0):
        #Left
        while(node.left!=None):
            stack.append(node.left)
            node=node.left
        #Root
        node=stack.pop()
        vals.append(node.data)
        #Right
        if (node.right!=None):
            stack.append(node.right)
            node=node.right
    return vals


if __name__=='__main__':
    root=BinaryNode(4)
    root.left=BinaryNode(2)
    root.right=BinaryNode(6)
    root.left.left=BinaryNode(1)
    root.left.right=BinaryNode(3)
    root.right.left=BinaryNode(5)
    root.right.right=BinaryNode(7)

    print("Itr_PreOrder: ",PreOrderTraversal_itr(root))
    print("Itr_PostOrder: ",PostOrderTraversal_itr(root))
    print("Itr_InOrder: ",InOrderTraversal_itr(root))

