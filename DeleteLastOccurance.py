# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, root, target):
        if target==None:
            return None
        if root==None:
            return root
        if root.next==None and root.val==target: return None
        node=root
        par_target=None
        
        while(node.next):
            if node.next.val==target:
                par_target=node
            node=node.next
        if par_target:
            par_target.next=par_target.next.next
        elif target==root.val:
            return root.next
        
        return root
