# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ceil(self,root,x):
        ceil=None
        if root==None: return None
        if x==None: return None
        node=root
        while(node):
            if node.val==x: return x
            if node.val>=x: ceil=node #No need to check node.val<ceil.val bcz node.val can't be appear in 10,9 for a key 7
            if node.val>x: node=node.left
            elif node.val<x: node=node.right
        
        return ceil 
    
    def floor(self,root,x):
        floor=TreeNode(0)
        if root==None: return None
        if x==None: return None
        node=root
        while(node):
            if node.val==x: return x
            if node.val<=x and node.val>floor.val: floor=node
            if node.val>x: node=node.left
            elif node.val<x: node=node.right
        return floor
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0: return None
        if len(preorder)==1: return TreeNode(preorder[0])
        
        root=TreeNode(preorder.pop(0))
        while(len(preorder)>0):
            node=preorder.pop(0)
            added=False
            ceil=self.ceil(root,node)
            if ceil:
                if ceil.left==None:
                    ceil.left=TreeNode(node)
                    added=True
            if not added:
                floor=self.floor(root,node)
                floor.right=TreeNode(node)
                
            print(root)
        return root
    
    
        
        
        
        
        
        
        
        
        
