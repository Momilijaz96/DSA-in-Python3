# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import time
class Solution:
    
    def isleaf(self,node):
        return node.left==None and node.right==None
            
    def myfunc(self,node,count):
        if node==None: return 0
        if self.isleaf(node): return count
        left=self.func(node.left,count*2)
        right=self.func(node.right,(count*2)+1)
        return max(left,right)
    
    def get_height(self,node,mode):
        if node==None: return 0
        height=0
        if mode=='L':
            while(node):
                node=node.left
                height+=1
            return height
        if mode=='R':
            while(node):
                node=node.right
                height+=1
            return height
    
    def comp_tree(self,node):
        if node==None: return 0
        if self.isleaf(node): return 1
        l=self.get_height(node.left,'L')
        r=self.get_height(node.right,'R')
        if l==r:
            return (2**(l+1))-1
        else:
            return 1+self.comp_tree(node.left)+self.comp_tree(node.right)
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None: return 0
        if root.left==None: return 1
        if root.right==None: return 2
        #my_res=self.myfunc(root,1)
        return self.comp_tree(root)
        
            
    
        
            
                
                
            
            
        