'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''


def findCeil(root, x):
    if root==None: return -1
    if x==None: return -1
    node=root
    path=[]
    while(node):
        if x==node.data: return node.data
        if node: path.append(node.data)
        if node.data>x: #get as close to key as posble so go less
            node=node.left
        elif node.data<x: #get as close to key as posbl, go more
            node=node.right
        
            
    for p in path[::-1]:
        if p>=x:
            return p
    return -1
