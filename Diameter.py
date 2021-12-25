# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_dia(root)
        return self.diameter
    
    def get_dia(self,root):    
        if root==None:
            return 0
        left_depth=self.get_dia(root.left)
        right_depth=self.get_dia(root.right)
        if (left_depth+right_depth)>self.diameter:
            self.diameter=left_depth+right_depth
        return 1+max(left_depth,right_depth)