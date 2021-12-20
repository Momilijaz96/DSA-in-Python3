from DataStructures.BinaryTree import BinaryNode

def InOrderTraversal(node):
    if node!=None:
        InOrderTraversal(node.left)
        print(node.data)
        InOrderTraversal(node.right)
    
def PreOrderTraversal(node):
    if node!=None:
        print(node.data)
        PreOrderTraversal(node.left)
        PreOrderTraversal(node.right)
    
def PostOrderTraversal(node):
    if node!=None:
        PostOrderTraversal(node.left)
        PostOrderTraversal(node.right)
        print(node.data)
    

if __name__=='__main__':
    ######Make binary tree########
    root=BinaryNode(2)
    root.left=BinaryNode(3)
    root.right=BinaryNode(4)
    #Second level
    root.left.left=BinaryNode(7)
    root.left.right=BinaryNode(8)
    root.right.left=BinaryNode(5)
    root.right.right=BinaryNode(6)
    #Third level
    root.left.right.left=BinaryNode(9)
    root.right.right.right=BinaryNode(10)

    #########Traverse##########
    print("INORDER TRAVERSAL") #Should be 7 3 9 8 2 5 4 6 10
    InOrderTraversal(root)
    print('\n')

    print("PREORDER TRAVERSAL") #Should be 2 3 7 8 9 4 5 6 10
    PreOrderTraversal(root)
    print('\n')

    print("POSTORDER TRAVERSAL") #Should be 7 9 8 3 5 10 6 4 2
    PostOrderTraversal(root)
    print('\n')

