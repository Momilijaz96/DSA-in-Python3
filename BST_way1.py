# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None: return TreeNode(val)
        if val==None: return root
        inserted=False
        node=root
        while(not inserted and node):
            if val<node.val:
                if (node.left==None):
                    node.left=TreeNode(val) 
                    inserted=True
                node=node.left
            elif val>node.val:
                if node.right==None:
                    node.right=TreeNode(val)
                    inserted=True
                node=node.right
        return root
    