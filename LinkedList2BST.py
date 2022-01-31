# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def toBST(self,nodes):
        if len(nodes)==1:
            return Tree(nodes[0])
        if len(nodes)==0:
            return None
        l=len(nodes)
        k=math.floor(l/2)
        root=Tree(nodes[k])
        root.left=self.toBST(nodes[:k])
        root.right=self.toBST(nodes[k+1:])
        return root

    def solve(self, root):
        if root==None: return None
        node=root
        nodes=[]
        while(node):
            nodes.append(node.val)
            node=node.next
        
        res=self.toBST(nodes)
        return res
        
            






