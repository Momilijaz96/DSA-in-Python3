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
    vals=[]
    while(len(stack)>0):
        if node: 
            vals.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        node=stack.pop()
    return vals

def InOrderTraversal_itr(node):
    if root==None: return None
    stack=[root]
    node=root
    vals=[]
    while(len(stack)>0):
        while(node):
            node=node.left
            if node: stack.append(node)
        node=stack.pop()
        vals.append(node.val)
        node=node.right
        if node: stack.append(node)
    return vals


if __name__=='__main__':
    root=BinaryNode(4)
    root.left=BinaryNode(2)
    root.right=BinaryNode(6)
    root.left.left=BinaryNode(1)
    root.left.right=BinaryNode(3)
    root.right.left=BinaryNode(5)
    root.right.right=BinaryNode(7)
    #Postorder tree example
    post_root=BinaryNode(7)
    post_root.left=BinaryNode(3)
    post_root.right=BinaryNode(6)
    post_root.left.left=BinaryNode(1)
    post_root.left.right=BinaryNode(2)
    post_root.right.left=BinaryNode(4)
    post_root.right.right=BinaryNode(5)

    print("Itr_PreOrder: ",PreOrderTraversal_itr(root))
    print("Itr_PostOrder: ",PostOrderTraversal_itr(post_root))
    print("Itr_InOrder: ",InOrderTraversal_itr(root))

