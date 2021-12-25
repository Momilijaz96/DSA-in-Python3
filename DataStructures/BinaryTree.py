

class BinaryNode:
    def __init__(self,data=None,left=None,right=None):
        self.data=data #data to be stored in this node
        self.left=left
        self.right=right

if __name__=='__main__':
    root=BinaryNode(2)
    root.left=BinaryNode(3)
    root.right=BinaryNode(4)

    #Second level
    root.left.left=BinaryNode(7)
    root.left.right=BinaryNode(8)
    root.right.left=BinaryNode(5)
    root.right.right=BinaryNode(6)

    #Third level
    root.left.right=BinaryNode(9)
    root.right.right=BinaryNode(10)

    print(root)
