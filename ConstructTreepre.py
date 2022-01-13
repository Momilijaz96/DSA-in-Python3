# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def myfunc(self,inorder,preorder):
        root=None
        if len(preorder)>0:
            root=preorder.pop(0)
            idx=inorder.index(root)
            root=TreeNode(root)
            left=inorder[:idx]
            right=inorder[idx+1:]
            if len(left)==0: root.left=None
            else:
                preorder,root.left=self.myfunc(left,preorder)
            if len(right)==0: root.right=None
            else:
                preorder,root.right=self.myfunc(right,preorder)

        return preorder,root 
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0 or len(preorder)==0: return None
        _,root=self.myfunc(inorder,preorder)
        return root
    
    