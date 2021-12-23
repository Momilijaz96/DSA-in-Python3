from DataStructures.BinaryTree import BinaryNode
import numpy as np

#Get binary tree depth recursively
def Depth_rec(node):
    if node==None: # or (node.left==None and node.right==None):
        return 0
    else:
        return 1+ max(Depth_rec(node.left),Depth_rec(node.right))

#Depth of tree from BFS
def BFS_depth(node):
    queue=[node]
    num_nodes=0
    while(len(queue)>0):
        num_nodes+=1
        node=queue.pop(0)
        if node!=None:
            queue.append(node.left)
            queue.append(node.right)
        
    return np.ceil(np.log2(num_nodes) - 1)

def BFS_nolog(node):
    queue=[node]
    num_nodes=len(queue)
    depth=0
    while(len(queue)>0):
        for _ in range(num_nodes):
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth+=1
        num_nodes=len(queue)
    return depth

if __name__=='__main__':
    #Tree sample
    post_root=BinaryNode(7)
    post_root.left=BinaryNode(3)
    post_root.right=BinaryNode(6)
    post_root.left.left=BinaryNode(1)
    post_root.left.right=BinaryNode(2)
    post_root.right.left=BinaryNode(4)
    post_root.right.right=BinaryNode(5)

    print("BFS depth: ",BFS_depth(post_root))
    print("Rec depth: ",Depth_rec(post_root))
    print("BFS no log depth: ",BFS_nolog(post_root))

