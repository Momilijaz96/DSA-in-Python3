# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxP=[]
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.getmaxPathSum(root)
        return max(self.maxP)    
    
    
    def getmaxPathSum(self,node):
        if node==None: return 0
        elif node.left==None and node.right==None: 
            self.maxP.append(node.val)
            return node.val
        LmaxP=self.getmaxPathSum(node.left)
        RmaxP=self.getmaxPathSum(node.right)
        local_maxP=max(node.val,node.val+RmaxP,node.val+LmaxP)
        self.maxP.append(node.val+RmaxP+LmaxP)
        self.maxP.append(local_maxP)
        return local_maxP