
def floorInBST(root, x):

    floor=-1
    if root==None: return -1
    if x==None: return -1
    node=root
    while(node):
        if node.data==x: return x
        if node.data<=x and node.data>floor: floor=node.data
        if node.data>x: node=node.left
        elif node.data<x: node=node.right
    return floor
    
