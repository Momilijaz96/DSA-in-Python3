# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None: return []
        q=[root]
        node=root
        vals=[]
        while(len(q)>0):
            vals.append(q[-1].val)
            nodes=len(q)
            for _ in range(nodes):
                node=q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return vals
        