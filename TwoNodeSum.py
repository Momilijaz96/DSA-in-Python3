# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def exists(self,root,val,node_x):
        if root==None: return False
        if val==None: return False
        node=root
        while(node):
            if node.val==val and node!=node_x:
                return True
            if node.val>=val:
                node=node.left
            elif node.val<val:
                node=node.right
        return False
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root==None: return False
        if k==None: return False
        node=root
        stack=[node]
        while(len(stack)>0):
            node=stack.pop()
            if node:
                res=self.exists(root,(k-node.val),node)
                if res: return True
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        
        return False
            
            
            
            
            