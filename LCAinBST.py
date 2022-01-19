# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p==None or q==None: return None
        elif root==None: return None
        elif (p.val>root.val and q.val<root.val) or (q.val>root.val and p.val<root.val):
            return root
        elif p==q:
            return p
    
        node=root
        while(node):
            if node.val<p.val and node.val<q.val:
                node=node.right
            elif node.val>p.val and node.val>q.val:
                node=node.left
            else:
                return node
        