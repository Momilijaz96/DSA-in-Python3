# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def myfunc(self,inorder,postorder):
        root=None
        if len(postorder)>0:
            root=postorder.pop()
            idx=inorder.index(root)
            root=TreeNode(root)
            left=inorder[:idx]
            right=inorder[idx+1:]
            if len(right)==0: root.right=None
            else:
                postorder,root.right=self.myfunc(right,postorder)
            
            if len(left)==0: root.left=None
            else:
                postorder,root.left=self.myfunc(left,postorder)
        return postorder,root    
            
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0 or len(postorder)==0: return None
        _,root=self.myfunc(inorder,postorder)
        return root
        