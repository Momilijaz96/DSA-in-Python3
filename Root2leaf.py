# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def output_format(self,arr):
        arr=[str(a.val) for a in arr]
        return '->'.join(arr)
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack=[]
        curr=[]
        res=[]
        node=root
        while(1):
            while(node):
                stack.append(node)
                curr.append((node))
                node=node.left
            node=stack.pop()
            if node.right:
                if node in curr:
                    curr=curr[:curr.index(node)+1]
                node=node.right
            else:
                if node.left==None and node.right==None:
                    res.append(self.output_format(curr))
                    curr.pop()
                node=None
            
            if len(stack)==0 and node==None: break
        return res