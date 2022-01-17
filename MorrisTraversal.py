# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None: return None
        parent=None
        node=root
        vals=[]
        count=0
        while(node or parent):
            while(node):
                left=node.left
                node.left=parent
                parent=node
                node=left
            node=parent
            vals.append(node.val)
            if node.right and parent!=root:
                node=node.right
                parent=parent.left
            elif node.right and parent==root:
                node=node.right
                parent=None
            else:
                parent=node.left
                node=None
            print("Parent: ", "NONE" if not parent else parent.val)
            print("Child: ", "NONE" if not node else node.val)
        return vals