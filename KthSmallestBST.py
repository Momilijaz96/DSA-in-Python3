# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None: return None
        if k<0: return None
        
        count=0
        node=root
        stack=[node]
        while(len(stack)>0):
            while(node):
                node=node.left
                if node: stack.append(node)
            node=stack.pop()
            count+=1
            if count==k: 
                return node.val
            if node.right:
                node=node.right
                stack.append(node)
            else:
                node=None