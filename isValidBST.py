# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root==None: return True
        node=root
        stack=[node]
        last=None
        while(len(stack)>0):
            while(node):
                node=node.left
                if node: stack.append(node)
            node=stack.pop()
            if last==None: last=node.val
            elif last>=node.val: return False
            last=node.val
            if node.right:
                node=node.right
                stack.append(node)
            else:
                node=None
        return True
            
        
