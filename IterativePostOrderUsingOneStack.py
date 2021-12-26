from DataStructures.BinaryTree import BinaryNode

'''
The idea is to move down to leftmost node using left pointer.
While moving down, push root and root’s right child to stack.
Once we reach leftmost node, print it if it doesn’t have a right child.
If it has a right child,
then change root so that the right child is processed before.  
'''
#PostOrder using one stack 2
def PostOrderOneStack2(node):
    if root==None: return None
    vals=[]
    stack=[]
    node=root
    while(1):
        while(node):
            if node.right: stack.append(node.right)
            stack.append(node)
            node=node.left
        node=stack.pop()
        if len(stack)>0 and node.right==stack[-1]:
            rn=stack.pop()
            stack.append(node)
            node=rn
        else:
            vals.append(node.val)
            node=None
        
        if len(stack)==0:
            break
    return vals

#This approach uses left-right-Root soln, which increases the if else checks in code
def PostOrderOneStack(node):
    stack=[node]
    while(node!=None and len(stack)>0):
        
        while(node.left!=None):
            #Get left most node and push right and left above root
            if node.right:
                stack.append(node.right)
            node=node.left
            stack.append(node)
        #print("Leftmost Node:",node.data)
        #Check if node is leaf
        if node.right==None:
            print(node.data)
            temp=stack.pop()
            
            if len(stack)>0:
                #if current node was right child of node below it
                if temp==stack[-1].right:
                    stack[-1].right=None
                    node=stack[-1]
                #or if current node was left chid of node above it,break connection
                elif temp==stack[-1].left:
                    stack[-1].left=None
                    node=stack[-1]
                #otherwise it's left sibling of the popped node
                else:
                    #Break connection of this child from parent, which is one node above sibling
                    r_sibling=stack.pop() #remove right sibling
                    stack[-1].left=None #breack conn from parent
                    stack.append(r_sibling) #put r_ibling back
                    node=stack[-1]

        else:
            stack.append(node.right)
            node=node.right
#Alternative soln: GeeksforGekks: code is smaller, samle logic but order is left-Root-right
#https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
            
if __name__=='__main__':
    #Example 1 - ans: 654328(10)971
    root=BinaryNode(1)
    root.left=BinaryNode(2)
    root.right=BinaryNode(7)
    root.left.left=BinaryNode(3)
    root.left.left.right=BinaryNode(4)
    root.left.left.right.right=BinaryNode(5)
    root.left.left.right.right.right=BinaryNode(6)
    root.right.left=BinaryNode(8)
    root.right.right=BinaryNode(9)
    root.right.right.right=BinaryNode(10)


    #Postorder tree example 2 - ans: 1234567
    post_root=BinaryNode(7)
    post_root.left=BinaryNode(3)
    post_root.right=BinaryNode(6)
    post_root.left.left=BinaryNode(1)
    post_root.left.right=BinaryNode(2)
    post_root.right.left=BinaryNode(4)
    post_root.right.right=BinaryNode(5)

    #Traverse the tree
    PostOrderOneStack(post_root)
