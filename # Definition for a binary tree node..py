# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxoffset_val(self,lvl_q):
        lvl_q.sort(key=lambda x: x[1])
        return lvl_q[0][1].data
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None: return []
        if root.left==None and root.right==None: return [root.val]
        #Return val with max offset at each level
        val=[]
        lvl_offset={0:root.val}
        offset=0
        q=[(root,offset)]
        right_view=[]
        while(len(q)>0):
            lvl_nodes=len(q)
            right_view.append(self.maxoffset_val(q))
            for _ in range(lvl_nodes):
                node,offset=q.pop(0)
                if node.left:
                    l_off=offset-1
                    q.append((node.left,l_off))
                if node.right:
                    r_off=offset+1
                    q.append((node.right,r_off)
        return right_view         
                
        