from DataStructures.BinaryTree import BinaryNode


def BFS(node):
    queue=[node]
    vals=[]
    while(len(queue)>0):
        node=queue.pop(0)
        if(node!=None):
            vals.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
    
    return vals

if __name__=='__main__':
    root=BinaryNode(1)
    root.left=BinaryNode(2)
    root.right=BinaryNode(3)
    root.left.left=BinaryNode(4)
    root.left.right=BinaryNode(5)
    root.right.left=BinaryNode(6)
    root.right.right=BinaryNode(7)

    print("BFS: ",BFS(root))
