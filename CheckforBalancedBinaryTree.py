# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,node):
        if node==None: return 0
        left_depth=self.check(node.left)
        right_depth=self.check(node.right)
        diff=abs(left_depth-right_depth)
        if diff>1 or left_depth==-1 or right_depth==-1:
            return -1
        return 1+max(left_depth,right_depth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root)!=-1